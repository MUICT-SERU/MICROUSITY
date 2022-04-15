const path = require('path');
const fs = require('fs');
const { workerData, parentPort } = require('worker_threads');
const { spawn } = require('child_process')

let { grammar, dict, settings, token, runMode } = workerData;
let scriptPath = path.resolve(__dirname, '../script/zeek');
let ifacePath = path.resolve(scriptPath, process.env.IFACE);
let dualIfacePath = path.resolve(scriptPath, process.env.SECOND_IFACE);
if (!fs.existsSync(ifacePath)) {
    fs.mkdirSync(ifacePath);
}
if (!fs.existsSync(dualIfacePath)) {
    fs.mkdirSync(dualIfacePath);
}
console.log(grammar);
let zeek_process = spawn(
    "zeek",
    ["-C", "-i", process.env.IFACE, "../track.zeek", "track::bff_port=" + process.env.BFF_PORT + '/tcp'],
    {
        cwd: ifacePath
    }
)
let zeek_process_two;
if(runMode === "dual") {
    zeek_process_two = spawn(
        "zeek",
    ["-C", "-i", process.env.SECOND_IFACE, "../track.zeek", "track::bff_port=" + process.env.BFF_PORT + '/tcp'],
    {
        cwd: dualIfacePath
    }
    )
}
zeek_process.stdout.on("data", (data) => {
    console.log(new TextDecoder().decode(data));
})
zeek_process.stderr.on("data", (data) => {
    console.log(new TextDecoder().decode(data));
})
let restler_cmd = "dotnet"
let restler_argv = [
    "bin/restler/restler.dll", "fuzz-lean",
    "--grammar_file", grammar,
    "--dictionary_file", dict,
    "--settings", settings,
    "--no_ssl"
]
if (token) {
    restler_argv.push(
        "--token_refresh_command", token,
        "--token_refresh_interval", 3600
    )
}
setTimeout(
    function () {
        let restler_process = spawn(
            restler_cmd,
            restler_argv,
            {
                cwd: path.resolve(__dirname, "..")
            }
        );
        if(zeek_process_two) {
            zeek_process_two.stdout.on("data", (data) => {
                console.log(new TextDecoder().decode(data));
            })
        }
        restler_process.stderr.on("data", (data) => {
            console.log(new TextDecoder().decode(data));
        })
        restler_process.stdout.on("data", (data) => {
            console.log(new TextDecoder().decode(data));
        })

        restler_process.on("exit", () => {
            console.log("exit restler");
            zeek_process.kill('SIGINT');
            if(zeek_process_two) zeek_process_two.kill('SIGINT');
            process.exit();
        });
    },
    30000
)

