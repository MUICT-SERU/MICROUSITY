const path = require('path');
const fs = require('fs');
const { workerData, parentPort } = require('worker_threads');
const { spawn } = require('child_process')

let { grammar, dict, settings } = workerData;
let token = workerData.token ?? null;
let scriptPath = path.resolve(__dirname, '../script/zeek');
let ifacePath = path.resolve(scriptPath, process.env.IFACE);
if (!fs.existsSync(ifacePath)) {
    fs.mkdirSync(ifacePath);
}
let zeek_process = spawn(
    "zeek",
    ["-C", "-i", process.env.IFACE, "../track.zeek", "track::bff_port=" + 8060 + '/tcp'],
    {
        cwd: ifacePath
    }
)
let restler_cmd = "dotnet"
let restler_argv = [
    "bin/restler/restler.dll", "fuzz-lean",
    "--grammar_file", grammar,
    "--dictionary_file", dict,
    "--settings", settings,
    "--no_ssl"
]
if (token) {
    restler_argv.push([
        "--token_refresh_command", token,
        "--token_refresh_interval", 3600
    ])
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
        restler_process.stderr.on("data", (data) => {
            console.log(new TextDecoder().decode(data));
        })
        restler_process.stdout.on("data", (data) => {
            console.log(new TextDecoder().decode(data));
        })

        restler_process.on("exit", () => {
            console.log("exit restler");
            zeek_process.kill('SIGINT');
            process.exit();
        });
    },
    10000
)

