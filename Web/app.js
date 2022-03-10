require('dotenv').config();
//import to use
const express = require("express");
const app = express();
const fs = require("fs");
const session = require("express-session");
const md5 = require("md5");
const EventEmitter = require("events");
const { Worker } = require("worker_threads");
const https = require('https');
const cytoscape = require('cytoscape');
const dagre = require('cytoscape-dagre');
//const
const SESSION_AUTH_USER = "session-auth-user";
let key,cert;
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

const { MongoClient } = require("mongodb");
const path = require("path");
const uri =
  "mongodb+srv://micro1:micro1@cluster0.u4edv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = client.db("userDB");
const collection = db.collection("user");
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

//middleware for auth
app.use(function isAuth(req, res, next) {
  req.user = getUser(req);
  next();
});
//Function when we know that the user is not login yet
// function notauth(req, res) {
//   if (!isLogin(req)) {
//     let query = qureystring.stringify({
//       fromUrl: req.originalUrl,
//     })
//     res.redirect('/login')
//     return true
//   }
//   return false
// }

//main home page
app.get("/", (req, res) => {
  if (req.user === null) {
    res.render("homeNotAuth");
    return;
  }
  let user = getUser(req);
  res.render("home", {
    user,
  });
});
app.get("/home", (req, res) => {
  if (req.user === null) {
    res.render("homeNotAuth");
    return;
  }
  let user = getUser(req);
  res.render("home", {
    user,
  });
});
let isTesting = false;
app.post("/launch", async (req, res) => {
  if (isTesting === true) {
    res.sendStatus(409);
    return;
  }
  res.sendStatus(200);
  events.emit("TESTSTARTED");
});

events.on("TESTSTARTED", () => {
  isTesting = true;
  const worker = new Worker("./worker.js");
  worker.once("exit", () => {
    isTesting = false;
  });
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
    .find({ email: username, password: md5(password) })
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
    password: md5(password),
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
  if(req.user === null) {
    res.redirect('/login');
    return;
  }
  res.render("content", {
    user: req.user,
  });
});

//testing tool page
app.get("/testingtool", (req, res) => {
  if (req.user === null) {
    res.redirect("/login");
    return;
  }
  res.render("testingtool", {
    user: req.user,
  });
});

app.get("/result", (req, res) => {
  // if (notauth(req, res)) return;
  if(req.user === null) {
    res.redirect('/login');
    return;
  }  //fs.readFile('../example/output5.json', 'utf8', (err, data) => {

    fs.readFile("../output/output.json", "utf8", (err, data) => {
    if (err) {
      return console.log("File read failed:", err);
    }
    var resultList = JSON.parse(data);
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
          subrequest.status_code >= 500 &&
          subrequest.status_code < 600
        ) {
          sub5xx += 1;
          //if (result.request.status_code < 500 || result.request.status_code >= 600) {
          trackId.push({ id: result.request.subrequest });
          //}
        }
      }
      countReq++;
    }

    for (let result of resultList) {
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

    res.render("result", {
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
      user: req.user,
    });
    console.log(removeDupId(coreLeakId));
    console.log(removeDupId(bffLeakId));
    console.log(removeDupId(bothLeakId));
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

//print page
app.get("/print", (req, res) => {
  res.render("print2");
});

app.get("/pdf", (req, res) => {
  if (req.user === null) {
    res.status(403).send("not authorized");
    return;
  }
  let user = req.user;
  let fname = user.fname;
  let lname = user.lname;
  // Import dependencies
  const moment = require("moment");
  const PDFDocument = require("pdfkit");

  collection.updateOne(
    { email: user.email },
    {
      $set: { pass: "TRUE" },
    },
    function (err) {
      if (err) throw err;
      console.log("Updated Status");
    }
  );

  // Create the PDF document
  const doc = new PDFDocument({
    layout: "landscape",
    size: "A4",
  });

  // The name
  const name = fname + " " + lname;

  // Pipe the PDF into an name.pdf file
  doc.pipe(fs.createWriteStream(`public/certificate/certificate.pdf`));

  // Draw the certificate image
  doc.image("public/Pic/certificate.PNG", 0, 0, { width: 842 });

  // Draw the name
  doc.fontSize(60).text(name, 90, 320, {
    align: "center",
  });

  // Draw the date
  doc.fontSize(15).text(moment().format("MMMM Do YYYY"), 175, 420, {
    align: "center",
  });

  // Finalize the PDF and end the stream
  doc.end();
  console.log("The certificate was created!");

  res.end("This message will be sent back to the client!");
  //res.redirect('/quiz')
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
        const fs = require("fs");
        const moment = require("moment");
        const PDFDocument = require("pdfkit");
        // Create the PDF document
        const doc = new PDFDocument({
          layout: "landscape",
          size: "A4",
        });

        // The name
        const name = fname + " " + lname;

        // Pipe the PDF into an name.pdf file
        doc.pipe(fs.createWriteStream(`public/certificate/certificate.pdf`));

        // Draw the certificate image
        doc.image("public/Pic/certificate.PNG", 0, 0, { width: 842 });

        // Draw the name
        doc.fontSize(60).text(name, 90, 320, {
          align: "center",
        });

        // Draw the date
        doc.fontSize(15).text(moment().format("MMMM Do YYYY"), 175, 420, {
          align: "center",
        });

        // Finalize the PDF and end the stream
        doc.end();
        console.log("The certificate was created!");
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



//contact us  page
app.get("/graph/:id", (req, res) => {
  if (req.user === null) {
    res.redirect('/login');
    return;
  }
  let id = req.params['id']
  //fs.readFile('../example/output5.json', 'utf8', (err, data) => {

  fs.readFile("../output/output.json", "utf8", (err, data) => {
    if (err) {
      return console.log("File read failed:", err);
    }
    
    var resultList = JSON.parse(data);
    //console.log(resultList);
    var trackSeq = [];
 
    for (let result of resultList) {
    
      if (result.request.subrequest == id) {
        trackSeq.push(result);
      } 
    
    }

    res.render("graph", {
      results: resultList,
      trackSeqs: trackSeq,
      user: req.user,
    });
    console.log(trackSeq);
   
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