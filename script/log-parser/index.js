const fs = require("fs");
const readline = require("readline");

const file = readline.createInterface({
  input: fs.createReadStream("http.log"),
  terminal: false,
});
let separator,
  setSeparator,
  emptyField,
  unsetField,
  path,
  open,
  fields,
  types,
  log = [];
let linenum = 0;
file.on("line", function (input) {
  if (linenum === 0) {
    separator = String.fromCharCode(input.substring(13, 15));
  }
  const currentLine = input.split(separator);
  const first = currentLine[0];
  if (first.charAt(0) === "#") {
    if (first.localeCompare("#set_separator") === 0) {
      setSeparator = currentLine[1];
    } else if (first.localeCompare("#empty_field") === 0) {
      emptyField = currentLine[1];
    } else if (first.localeCompare("#unset_field") === 0) {
      unsetField = currentLine[1];
    } else if (first.localeCompare("#path") === 0) {
      path = currentLine[1];
    } else if (first.localeCompare("#open") === 0) {
      open = currentLine[1];
    } else if (first.localeCompare("#fields") === 0) {
      fields = currentLine.slice(1);
    } else if (first.localeCompare("#types") === 0) {
      types = currentLine.slice(1);
    }
  } else {
    log.push(handleLog(currentLine));
  }
  linenum++;
});

function handleLog(line) {
  let column = {};
  for (let i = 0; i < line.length; i++) {
    if (line[i] === emptyField) line[i] = null;
    switch (types[i]) {
      case "time":
        column[fields[i]] = new Date(Number(line[i]) * 1000);
        break;
      case "port":
      case "count":
      case "int":
        column[fields[i]] = Number(line[i]);
        break;
      default:
        column[fields[i]] = line[i];
        break;
    }
  }
  return column;
}
const mapping = new Map();
let bffPort = [3000];
file.on("close", () => {
  mapBffToSubrequest();
  let output = [];
  mapping.forEach((value) => {
    const errorCode = value["request"]["status_code"];
    const statusInside = value["subrequest"].map((x) => x["status_code"]);
    const errorCodeInside = statusInside.filter((x) => x > 200);
    let bffError = errorCode > 200;
    if (errorCodeInside.length > 0 || bffError) {
        output.push(value);
    }
  });
  fs.writeFileSync('output.json', JSON.stringify(output));
});

function mapBffToSubrequest() {
  let javaExceptionRegex = /\S*Exception/;
  for (let index = 0; index < log.length; index++) {
    const element = log[index];
    const javaException = javaExceptionRegex.exec(element["post_body"]);
    if(javaException !== null) element["exception"] = javaException[0];
    const requestNo = element["subrequest"];
    const isBffRequest = bffPort.includes(element["id.resp_p"]);
    if (!mapping.has(requestNo)) {
      mapping.set(requestNo, {
        request: null,
        subrequest: [],
      });
    }
    const value = mapping.get(requestNo);
    if (isBffRequest) {
      value["request"] = element;
    } else {
      value["subrequest"].push(element);
    }
  }
}
