const fs = require('fs');
const readline = require('readline');

async function readLog(path, interface='') {
    const rl = readline.createInterface(
        {
            input: fs.createReadStream(path),
            terminal: false
        }
    );
    let separator,
        setSeparator,
        emptyField,
        unsetField,
        path_zeek,
        open,
        fields,
        types,
        log = [];
    let linenum = 0;
    for await (const line of rl) {
        if (linenum === 0) {
            separator = String.fromCharCode(line.substring(13, 15));
        }
        const currentLine = line.split(separator);
        const first = currentLine[0];
        if (first.charAt(0) === "#") {
            if (first.localeCompare("#set_separator") === 0) {
                setSeparator = currentLine[1];
            } else if (first.localeCompare("#empty_field") === 0) {
                emptyField = currentLine[1];
            } else if (first.localeCompare("#unset_field") === 0) {
                unsetField = currentLine[1];
            } else if (first.localeCompare("#path") === 0) {
                path_zeek = currentLine[1];
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
    }
    return log;
    function handleLog(line) {
        let column = {};
        for (let i = 0; i < line.length; i++) {
            if (line[i] === emptyField) {
                line[i] = null;
                continue;
            };
            if (line[i] === unsetField) {
                continue;
            }
            const setVectorRegex = /(?:set|vector)\[(\w+)\]/;
            let type = types[i];
            let match = setVectorRegex.exec(types[i]);
            let tempArray = [];
            if (match !== null) {
                tempArray = line[i].split(setSeparator);
                type = match[1];
                switch (type) {
                    case "time":
                        column[fields[i]] = tempArray.map(element => {
                            return {
                                rawEpoch: Number(element),
                                date: new Date(Number(element) * 1000)
                            };
                        });
                        break;
                    case "port":
                    case "count":
                    case "int":
                        column[fields[i]] = tempArray.map(element => {
                            return Number(element);
                        });
                        break;
                    default:
                        column[fields[i]] = tempArray;
                        break;
                }
                continue;
            }
            switch (type) {
                case "time":
                    column[fields[i]] = {
                        rawEpoch: Number(line[i]),
                        date: new Date(Number(line[i]) * 1000)
                    };
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
        if(interface !== '') {
            column['interface'] = interface;
        }
        return column;
    }
}

module.exports = readLog;