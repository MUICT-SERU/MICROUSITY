const fs = require("fs");
const readline = require("readline");
const path = require("path");
const readLog = require('./read.js');

const javaExceptionRegex = /\S*Exception/;

let bffPort = [Number(process.env.BFF_PORT)];
let excludedPort = [443, 80];
let getIfaceLog = (async (iface) => {
  let result = await readLog(path.resolve('../script/zeek/' + iface + '/http.log'), iface);
  return result;
});

function singleIfaceMapping(first) {
  let result = [];
  let bffRequest = [];
  let subRequest = [];
  for (let index = 0; index < first.length; index++) {
    const element = first[index];
    if (excludedPort.includes(element["id.resp_p"])) {
      continue;
    }
    const javaException = javaExceptionRegex.exec(element["post_body"]);
    if (javaException !== null) element["exception"] = javaException[0];
    const requestNo = element["subrequest"];
    const isBffRequest = bffPort.includes(element["id.resp_p"]);
    if (isBffRequest) {
      bffRequest.push(element);
    } else {
      if(requestNo > subRequest.length) {
        subRequest.push([element]);
      }
      else {
        subRequest[requestNo - 1].push(element);
      }
    }
  }
  for(let i = 0;i < bffRequest.length;i++) {
    result.push({
      'request': bffRequest[i],
      'subrequest': subRequest[i]
    })
  }
  return result;
}

function dualIfaceMapping(main, secondary, primary_iface) {
  let result = [];
  let merged = main.concat(secondary);
  merged.sort(
    (a,b) => a.ts.rawEpoch - b.ts.rawEpoch
  );
  let subrequest = -1;
  for(i = 0; i < merged.length; i++) {
    if (excludedPort.includes(merged[i]["id.resp_p"])) {
      continue;
    }
    let isBffRequest = false;
    if (merged[i]["interface"] === primary_iface) {
      isBffRequest = true;
      subrequest++;
    }
    merged[i].subrequest = subrequest;
    const javaException = javaExceptionRegex.exec(merged[i]["post_body"]);
    if (javaException !== null) merged[i]["exception"] = javaException[0];
    if(isBffRequest) {
      result.push(
        {
          "request": merged[i],
          "subrequest": []
        }
      )
    }
    else {
      result[merged[i]["subrequest"]]["subrequest"].push(merged[i]);
    }
  }
  return result;
}
module.exports = { getIfaceLog, singleIfaceMapping, dualIfaceMapping };