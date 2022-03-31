const readLog = require("./read")
const fs = require("fs")
const { dualIfaceMapping } = require("./index")

let a = readLog("../../script/zeek/lo0/http.log", "lo0")
let b = readLog("../../script/zeek/utun2/http.log", "utun2")

Promise.all([a,b]).then(
    result => {
        let final = dualIfaceMapping(result[0], result[1], "lo0");
        console.log(final);
    }
)