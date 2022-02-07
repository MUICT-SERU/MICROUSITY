const { parentPort } = require('worker_threads');
const path = require('path');
const {spawnSync, fork} = require('child_process');

let pathDir = path.resolve(process.cwd() + '/..' + '/script')
let scriptPath = path.resolve(pathDir + '/launch-example/test.sh');
spawnSync(scriptPath, {
    cwd: path.resolve(pathDir, 'launch-example'),
    stdio: ['ignore', 'inherit', 'inherit']
});
fork("log-parser/index.js", {
    cwd: pathDir
});
process.exit();