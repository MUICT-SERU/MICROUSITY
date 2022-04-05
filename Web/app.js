require('dotenv').config();
//import to use
const express = require("express");
const app = express();
const fs = require("fs");
const session = require("express-session");
const bcrypt = require("bcrypt");
const EventEmitter = require("events");
const { Worker } = require("worker_threads");
const https = require('https');
const cytoscape = require('cytoscape');
const dagre = require('cytoscape-dagre');
const moment = require("moment");
const formidable = require('formidable');
const PDFDocument = require("pdfkit");
const { singleIfaceMapping, dualIfaceMapping, getIfaceLog } = require('./log-parser/index')

//const
const SESSION_AUTH_USER = "session-auth-user";
let key, cert;
try {
  key = fs.readFileSync(process.env.KEY);
  cert = fs.readFileSync(process.env.CERT);
}
catch (err) {
  console.log('Cert not found, will run as http');
}
let events = new EventEmitter();

//setting
app.use(express.static("public"));
app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(
  session({
    secret: "my-session",
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false },
  })
);

const { MongoClient, ObjectId } = require("mongodb");
const path = require("path");
const { get } = require('http');
const uri =
  "mongodb+srv://micro1:micro1@cluster0.u4edv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = client.db("userDB");
const collection = db.collection("user");
const resultCollection = db.collection("testResult");
client.connect((err) => {
  if (err) console.error(err);
  else console.log("Connected successfully to server");
});

//Setting for ejs
app.set("view engine", "ejs");
app.set("views", "./views");

//Set user function
function setUser(req, user) {
  req.session[SESSION_AUTH_USER] = user;
}

//Get user function
function getUser(req) {
  return req.session[SESSION_AUTH_USER] || null;
}

//Clear user function
function clearUser(req) {
  setUser(req, null);
}

//remove duplicate id
function removeDupId(arr) {
  return (arr = arr.filter(
    (value, index, self) => index === self.findIndex((t) => t.id === value.id)
  ));
}

//get certificate function
function getCertificate(name, date) {
  // Create the PDF document
  const doc = new PDFDocument({
    layout: "landscape",
    size: "A4",
  });

  // Pipe the PDF into an certificate.pdf file
  doc.pipe(fs.createWriteStream(`public/certificate/certificate.pdf`));

  // Draw the certificate image
  doc.image("public/Pic/certificate.PNG", 0, 0, { width: 842 });

  // Draw the name
  doc.fontSize(60).text(name, 90, 320, {
    align: "center",
  });

  // Draw the date
  doc.fontSize(15).text(date, 175, 420, {
    align: "center",
  });

  // Finalize the PDF and end the stream
  doc.end();
  console.log("The certificate was created!");
}

//result render
function getResult(data, fromFile) {
  if (fromFile == true) {
    var resultList = JSON.parse(data);
  } else {
    var resultList = data.result;
  }
  var main5xx = 0;
  var main4xx = 0;
  var main3xx = 0;
  var main2xx = 0;
  var sub5xx = 0;
  var sub4xx = 0;
  var sub3xx = 0;
  var sub2xx = 0;
  var countReq = 0;

  var bffLeak = false;
  var coreLeak = false;

  var trackId = [];
  var bffLeakId = [];
  var coreLeakId = [];
  var bothLeakId = [];

  for (let result of resultList) {
    if (result.request === null) {
    } else if (
      result.request.status_code >= 200 &&
      result.request.status_code < 300
    ) {
      main2xx += 1;
    } else if (
      result.request.status_code >= 300 &&
      result.request.status_code < 400
    ) {
      main3xx += 1;
    } else if (
      result.request.status_code >= 400 &&
      result.request.status_code < 500
    ) {
      main4xx += 1;
    } else if (
      result.request.status_code >= 500 &&
      result.request.status_code < 600
    ) {
      main5xx += 1;
      trackId.push({ id: result.request.subrequest });
    }
    for (let subrequest of result.subrequest) {
      if (subrequest.status_code >= 200 && subrequest.status_code < 300) {
        sub2xx += 1;
      }
      if (subrequest.status_code >= 300 && subrequest.status_code < 400) {
        sub3xx += 1;
      }
      if (subrequest.status_code >= 400 && subrequest.status_code < 500) {
        sub4xx += 1;
      } else if (
        subrequest.status_code >= 500 && subrequest.status_code < 600) {
        sub5xx += 1;
        //if (result.request.status_code < 500 || result.request.status_code >= 600) {
        trackId.push({ id: result.request.subrequest });
        //}
      }
    }
    countReq++;
  }

  for (let result of resultList) {
    if (result.request === null) {
    } else {
      //for (let id of trackId) {
      bffLeak = false;
      coreLeak = false;
      //if (result.request.subrequest == id.id) {
      if (result.request === null) {
      } else if (result.request.exception) {
        bffLeak = true;
        //console.log(id.id)

      }
      if (result.subrequest.length == 0) {
        //console.log(result.subrequest.length)
        if (bffLeak == true) {
          bffLeakId.push({ id: result.request.subrequest });
        }
      } else {
        for (let subrequest of result.subrequest) {
          if (subrequest.exception) {
            coreLeak = true;
          }
        }
      }
      if (coreLeak && bffLeak) {
        bothLeakId.push({ id: result.request.subrequest });
      } else if (coreLeak && !bffLeak) {
        coreLeakId.push({ id: result.request.subrequest });
      } else if (!coreLeak && bffLeak) {
        bffLeakId.push({ id: result.request.subrequest });
      }
      //}
      //}
    }

  }
  return {
    results: resultList,
    main4xxs: main4xx,
    main5xxs: main5xx,
    sub4xxs: sub4xx,
    sub5xxs: sub5xx,
    sum3xxs: main3xx + sub3xx,
    sum2xxs: main2xx + sub2xx,
    countReqs: countReq,
    trackIds: removeDupId(trackId),
    coreLeakIds: removeDupId(coreLeakId),
    bffLeakIds: removeDupId(bffLeakId),
    bothLeakIds: removeDupId(bothLeakId),
  }

}

//result render
function getSpeccov(data, fromFile) {
  if (fromFile == true) {
    var jsonCoverages = JSON.parse(data);
  } else {
    var jsonCoverages = data.coverage;
  }

  let invalid = 0;
  let valid = 0;

  for (let jsonCoverage in jsonCoverages) {
    if (jsonCoverages[jsonCoverage].valid == 0) {
      invalid++;
    } else {
      valid++;
    }
  }

  return {
    speccovs: jsonCoverages,
    valid: valid,
    invalid: invalid,
  }

}

//middleware for auth
app.use(function isAuth(req, res, next) {
  req.user = getUser(req);
  next();
});


//main home page
app.get("/", (req, res) => {
  if (req.user === null) {
    res.render("home", {
      user: null,
    });
    return;
  }
  let user = getUser(req);
  res.render("home", {
    user: user,
  });
});
app.get("/home", (req, res) => {
  if (req.user === null) {
    res.render("home", {
      user: null,
    });
    return;
  }
  let user = getUser(req);
  res.render("home", {
    user: user,
  });
});
let isTesting = false;
app.post("/launch", async (req, res) => {
  if (isTesting === true) {
    res.sendStatus(409);
    return;
  }
  let mode = req.body.mode;

  if (mode === 'single') {
    events.emit("TESTSTARTED", 'single', "/Users/pumipat/SP2021-TRITECH/grammar/grammar.py", "/Users/pumipat/SP2021-TRITECH/grammar/dict.json", "/Users/pumipat/SP2021-TRITECH/grammar/restler_user_settings.json");
  }
  else if (mode === 'dual') {
    events.emit("TESTSTARTED", "dual");
  }
  else {
    res.status(400).send("invalid mode");
    return;
  }
  res.sendStatus(200);
});

events.on("TESTSTARTED", (mode, grammar, dict, settings, token) => {
  isTesting = true;
  let worker;
  switch (mode) {
    case "single":
      worker = new Worker('./worker_no_shell.js', {
        workerData: {
          grammar,
          dict,
          settings,
          token
        }
      })
      break;
    case "dual":
      worker = new Worker('./worker.js');
      break;
    case "custom":
      if (token !== undefined) {
        worker = new Worker('./worker_custom_script.js', {
          workerData: {
            grammar,
            dict,
            settings,
            token
          }
        });
      }
      else {
        worker = new Worker('./worker_custom_script.js', {
          grammar,
          dict,
          settings
        })
      }
      break;
    default:
      console.log("invalid case");
      isTesting = false;
      return;
  }
  worker.once("exit", () => {
    isTesting = false;
    let first = getIfaceLog(process.env.IFACE);
    let second;
    if (mode !== 'single') second = getIfaceLog(process.env.SECOND_IFACE);
    let trick_email = "pooh99191@gmail.com"
    if (mode === 'single') {
      Promise.resolve(first)
      .then(
        // res => dualIfaceMapping(res[0], res[1], process.env.IFACE)
        res => singleIfaceMapping(res)
      )
      .then(
        res => {
          let pathTo = path.resolve(__dirname, '../FuzzLean/RestlerResults');
          let specPath = path.resolve(pathTo, fs.readdirSync(pathTo)[0], 'logs/speccov.json');
          let coverage = fs.readFileSync(specPath, 'utf-8');
          var myobj = {
            email: trick_email,
            time: moment().format('D MMMM YYYY, h:mm:ss a'),
            result: res,
            coverage: JSON.parse(coverage)
          };
          collection.find({ email: trick_email }).toArray(function (err, users) {
            resultCollection.insertOne(myobj, function (err) {
              if (err) throw err;
              console.log("1 result inserted");
            });
          });
          fs.writeFileSync("../output/output.json", JSON.stringify(res));
          console.log("written result");
        });
    }
    else {
      Promise.resolve(first, second)
      .then(
        res => dualIfaceMapping(res[0], res[1], process.env.IFACE)
      )
      .then(
        res => {
          let pathTo = path.resolve(__dirname, '../FuzzLean/RestlerResults');
          let specPath = path.resolve(pathTo, fs.readdirSync(pathTo)[0], 'logs/speccov.json');
          let coverage = fs.readFileSync(specPath, 'utf-8');
          var myobj = {
            email: trick_email,
            time: moment().format('D MMMM YYYY, h:mm:ss a'),
            result: res,
            coverage: JSON.parse(coverage)
          };
          collection.find({ email: trick_email }).toArray(function (err, users) {
            resultCollection.insertOne(myobj, function (err) {
              if (err) throw err;
              console.log("1 result inserted");
            });
          });
          fs.writeFileSync("../output/output.json", JSON.stringify(res));
          console.log("written result");
        });
    }
  })
});

app.get("/test_status", (req, res) => {
  res.set('Content-Type', 'text/plain')
  if (isTesting) {
    res.send("LOCKED");
    return;
  } else {
    res.send("UNLOCKED");
  }
});

//login page
app.get("/login", (req, res) => {
  res.render("login", {
    invalid: req.query["invalid"] || false,
    fromUrl: req.query["fromUrl"] || "/login",
  });
});

//When click login
app.post("/login", (req, res) => {
  let { username, password, fromUrl } = req.body;
  collection
    .find({ email: username, password: bcrypt.hash(password, 10) })
    .toArray(function (err, users) {
      if (err || users.length != 1) {
        return res.redirect("/login?invalid=1");
      }
      let user = users[0];
      delete user.password;
      setUser(req, user);
      res.redirect("/home");
    });
});

//register page
app.get("/register", (req, res) => {
  res.render("register", {
    Uinvalid: req.query["Uinvalid"] || false,
    fromUrl: req.query["fromUrl"] || "/register",
  });
});

//When click register
app.post("/register", (req, res) => {
  let fname = req.body["fname"];
  let lname = req.body["lname"];
  let email = req.body["email"];
  let password = req.body["password"];
  var myobj = {
    fname: fname,
    lname: lname,
    email: email,
    password: bcrypt.hash(password, 10),
    pass: "FALSE",
  };

  collection.find({ email: email }).toArray(function (err, users) {
    if (err || users.length !== 0) {
      res.redirect("/register?Uinvalid=1");
    } else {
      collection.insertOne(myobj, function (err) {
        if (err) throw err;
        console.log("1 user inserted");
        res.redirect("/login");
      });
    }
  });
});

//lesson page
app.get("/content", (req, res) => {
  if (req.user === null) {
    res.redirect('/login');
    return;
  }
  res.render("content", {
    user: req.user,
  });
});

//sandbox page
app.get("/testingtool", (req, res) => {
  if (req.user === null) {
    res.redirect("/login");
    return;
  }
  res.render("testingtool", {
    user: req.user,
  });
});

//sandbox page
app.get("/testingtool2", (req, res) => {
  // if (req.user === null) {
  //   res.redirect("/login");
  //   return;
  // }
  res.render("testingtool2", {
    user: req.user,
  });
});

//testing tool page
app.post("/upload", (req, res) => {
  var form = new formidable.IncomingForm();
  form.parse(req, function (err, fields, files) {
    var outputPath = path.resolve(__dirname, '../outtest/');
    console.log(outputPath);
    var oldGrammarPath = files.grammar.filepath;
    var oldDictPath = files.dict.filepath;
    var oldUserSettingPath = files.userSetting.filepath;
    var oldTokenPath = files.token.filepath ?? null;
    var newGrammarPath = path.resolve(outputPath, 'grammar.py');
    var newDictPath = path.resolve(outputPath, 'dict.json');
    var newUserSettingPath = path.resolve(outputPath, 'restler_user_settings.json');
    var newTokenPath = path.resolve(outputPath, 'token');
    fs.rename(oldGrammarPath, newGrammarPath, function (err) {
      if (err) throw err;
    });
    fs.rename(oldDictPath, newDictPath, function (err) {
      if (err) throw err;
    });
    fs.rename(oldUserSettingPath, newUserSettingPath, function (err) {
      if (err) throw err;
    });
    if (oldTokenPath !== null) {
      fs.rename(oldTokenPath, newTokenPath, function (err) {
        if (err) throw err;
      });
      fs.chmod(newTokenPath, 0o744, (err) => {
        if (err) throw err;
      });
    }
    if (err) {
      throw err;
    } else {
      console.log('File uploaded and moved!');
      res.redirect('/history');
      events.emit("TESTSTARTED", "custom", newGrammarPath, newDictPath, newUserSettingPath, newTokenPath);
    }
  });

});


//save result history
app.get("/save", (req, res) => {
  // if (req.user === null) {
  //   res.redirect("/login");
  //   return;
  // }
  let user = req.user;
  fs.readFile('../example/output99.json', 'utf8', (err, data) => {
    //fs.readFile("../output/output.json", "utf8", (err, data) => {
    if (err) {
      return console.log("File read failed:", err);
    }
    fs.readFile('../example/speccov.json', 'utf8', (err, coverage) => {
      if (err) {
        return console.log("File read failed:", err);
      }
      var resultList = JSON.parse(data);
      var myobj = {
        email: "pooh99191@gmail.com",
        time: moment().format('D MMMM YYYY, h:mm:ss a'),
        result: resultList,
        coverage: JSON.parse(coverage)
      };
      collection.find({ email: user.email }).toArray(function (err, users) {
        resultCollection.insertOne(myobj, function (err) {
          if (err) throw err;
          console.log("1 result inserted");
          res.redirect("/home");
        });

      });

    });

  });

});

//result history
app.get("/history", (req, res) => {
  if (req.user === null) {
    res.redirect("/login");
    return;
  }
  let user = req.user;

  resultCollection.find({ email: user.email }).toArray(function (err, data) {
    res.render("history", {
      data: data
    });
  });

});

//result testing tool
app.get("/resulthis/:id", (req, res) => {

  if (req.user === null) {
    res.redirect('/login');
    return;
  }

  let id = req.params['id']
  resultCollection.findOne({ "_id": new ObjectId(id) }, function (err, data) {
    let result = getResult(data, false);
    let coverage = getSpeccov(data, false)
    res.render("result", {
      results: result.results,
      main4xxs: result.main4xxs,
      main5xxs: result.main5xxs,
      sub4xxs: result.sub4xxs,
      sub5xxs: result.sub5xxs,
      sum3xxs: result.sum3xxs,
      sum2xxs: result.sum2xxs,
      countReqs: result.countReqs,
      trackIds: result.trackIds,
      coreLeakIds: result.coreLeakIds,
      bffLeakIds: result.bffLeakIds,
      bothLeakIds: result.bothLeakIds,
      speccovs: coverage.speccovs,
      valid: coverage.valid,
      invalid: coverage.invalid,
      user: req.user,
      resultid: id,
    });
    // console.log(removeDupId(coreLeakId));
    // console.log(removeDupId(bffLeakId));
    // console.log(removeDupId(bothLeakId));

  });

});

//result sandbox
app.get("/result", (req, res) => {

  // if (req.user === null) {
  //   res.redirect('/login');
  //   return;
  // }
  //fs.readFile('../example/output5.json', 'utf8', (err, data) => {
  fs.readFile("../output/output.json", "utf8", (err, data) => {
    if (err) {
      return console.log("File read failed:", err);
    }
    fs.readFile('../example/speccov.json', 'utf8', (err, specCoverage) => {
      if (err) {
        return console.log("File read failed:", err);
      }

      let result = getResult(data, true);
      let coverage = getSpeccov(specCoverage, true)
      res.render("result", {
        results: result.results,
        main4xxs: result.main4xxs,
        main5xxs: result.main5xxs,
        sub4xxs: result.sub4xxs,
        sub5xxs: result.sub5xxs,
        sum3xxs: result.sum3xxs,
        sum2xxs: result.sum2xxs,
        countReqs: result.countReqs,
        trackIds: result.trackIds,
        coreLeakIds: result.coreLeakIds,
        bffLeakIds: result.bffLeakIds,
        bothLeakIds: result.bothLeakIds,
        speccovs: coverage.speccovs,
        valid: coverage.valid,
        invalid: coverage.invalid,
        user: req.user,
        resultid: null
      });
    });

    //console.log(removeDupId(coreLeakId));
    //console.log(removeDupId(bffLeakId));
    //console.log(removeDupId(bothLeakId));
  });
});

//save dict to file
app.get("/saveDict_json", (req, res) => {
  try {
    fs.writeFileSync("../grammar/dict.json", req.query.data);
    console.log("dict written");
  } catch (error) {
    console.log(err);
  }
  res.sendStatus(200);
});

//save dyn to file
app.get("/saveDyn_json", (req, res) => {
  try {
    fs.writeFileSync("../grammar/restler_user_settings.json", req.query.data);
    console.log("engine settings written");
  } catch (error) {
    console.log(err);
  }
  res.sendStatus(200);
});


app.get("/pdf", (req, res) => {
  if (req.user === null) {
    res.status(403).send("not authorized");
    return;
  }
  let user = req.user;
  let fname = user.fname;
  let lname = user.lname;

  collection.updateOne(
    { email: user.email },
    {
      $set: { pass: "TRUE", date: moment().format("MMMM Do YYYY") },
    },
    function (err) {
      if (err) throw err;
      console.log("Updated Status");
    }
  );

  const name = fname + " " + lname;
  getCertificate(name, moment().format("MMMM Do YYYY"));

  res.end("This message will be sent back to the client!");

});

//quiz page
app.get("/quiz", (req, res) => {
  if (req.user === null) {
    res.redirect('/login');
    return;
  }
  let user = req.user;
  let fname = user.fname;
  let lname = user.lname;
  collection
    .find({ email: user.email, pass: "TRUE" })
    .toArray(function (err, users) {
      if (err || users.length !== 0) {
        const name = fname + " " + lname;
        const date = users[0].date;
        getCertificate(name, date);
        res.render("quiz", {
          user,
          pass: "TRUE",
        });
      } else {
        res.render("quiz", {
          user,
          pass: "FALSE",
        });
      }
    });
});


//testingtool graph
app.get("/graph2/:id/:resultid", (req, res) => {
  if (req.user === null) {
    res.redirect('/login');
    return;
  }
  let id = req.params['id']
  let resultId = req.params['resultid']
  let error;
  if (req.query["error"] == 'true') {
    error = true;
  } else {
    error = false;
  }

  resultCollection.findOne({ "_id": new ObjectId(resultId) }, function (err, data) {
    if (err) {
      return console.log("File read failed:", err);
    }

    var resultList = data.result;
    //console.log(resultList);
    var trackSeq = [];

    for (let result of resultList) {
      if (result.request === null) {

      } else {
        if (result.request.subrequest == id) {
          trackSeq.push(result);
        }
      }

    }

    res.render("graph", {
      results: resultList,
      trackSeqs: trackSeq,
      user: req.user,
      resultId: resultId,
      error: error
    });
  });
});


//sandbox graph
app.get("/graph/:id", (req, res) => {
  if (req.user === null) {
    res.redirect('/login');
    return;
  }
  let id = req.params['id']
  let error;
  if (req.query["error"] == 'true') {
    error = true;
  } else {
    error = false;
  }

  //fs.readFile('../example/output5.json', 'utf8', (err, data) => {

  fs.readFile("../output/output.json", "utf8", (err, data) => {
    if (err) {
      return console.log("File read failed:", err);
    }

    var resultList = JSON.parse(data);
    //console.log(resultList);
    var trackSeq = [];

    for (let result of resultList) {
      if (result.request === null) {

      } else {
        if (result.request.subrequest == id) {
          trackSeq.push(result);
        }
      }

    }

    res.render("graph", {
      results: resultList,
      trackSeqs: trackSeq,
      user: req.user,
      resultId: null,
      error: error
    });

  });
});

//contact us  page
app.get("/aboutus", (req, res) => {
  res.render("aboutus");
});

//When logout
app.get("/logout", (req, res) => {
  clearUser(req);
  res.redirect("/home");
});

//run
if (key === undefined) {
  app.listen(8080, () => {
    console.log('listening as http at 8080');
  });
} else {
  https.createServer({ key: key, cert: cert, passphrase: '1234' }, app).listen(443, () => {
    console.log('listening w/ https');
  });
}