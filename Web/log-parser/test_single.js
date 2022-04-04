const readLog = require("./read")
const { singleIfaceMapping } = require("./index")

let a = readLog("../../script/zeek/lo0/http.log", "lo0")

a.then(
    res => {
        let array = singleIfaceMapping(res);
        require('fs').writeFileSync("aaaa.json", JSON.stringify(array));
        return array;
    }
)