const { parentPort } = require('worker_threads');
const path = require('path');
const { spawnSync } = require('child_process');

let pathDir = path.resolve(process.cwd() + '/..' + '/script')
let scriptPath = path.resolve(pathDir + '/launch-example/test.sh');
let iface_argv = [];
if(process.env.IFACE) iface_argv.push(process.env.IFACE);
if(process.env.SECOND_IFACE) iface_argv.push(process.env.SECOND_IFACE);
if(process.env.BFF_PORT) iface_argv.push(process.env.BFF_PORT + '/tcp');
spawnSync(scriptPath, iface_argv, {
    cwd: path.resolve(pathDir, 'launch-example'),
    stdio: ['ignore', 'inherit', 'inherit']
});
process.exit();