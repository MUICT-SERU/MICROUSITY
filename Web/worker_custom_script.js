const path = require('path');
const { spawnSync } = require('child_process');
const { workerData } = require('worker_threads')

let { grammar, dict, settings, token } = workerData;
let pathDir = path.resolve(process.cwd() , '..' , 'script')
let scriptPath = path.resolve(pathDir , 'launch-example/test_custom.sh');
let iface_argv = [];
if(process.env.IFACE) iface_argv.push(process.env.IFACE);
if(process.env.SECOND_IFACE) iface_argv.push(process.env.SECOND_IFACE);
if(process.env.BFF_PORT) iface_argv.push(process.env.BFF_PORT + '/tcp');
iface_argv.push(grammar, dict, settings);
if(token) iface_argv.push(token);
let result = spawnSync(scriptPath, iface_argv, {
    cwd: path.resolve(pathDir, 'launch-example'),
    stdio: ['ignore', 'inherit', 'inherit']
});
console.log(scriptPath);
console.log(result.output);
process.exit();