//import to use
const express = require("express");
const app = express();
const dotenv = require("dotenv");
const fs = require('fs');
const session = require('express-session');
const qureystring = require('querystring');
const spawn = require('child_process').spawn;
const fork = require('child_process').fork;
const md5 = require('md5')

//const
const SESSION_AUTH_USER = 'session-auth-user'

//setting
app.use(express.static("public"));
app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(session({
  secret: 'my-session',
  resave: false,
  saveUninitialized: true,
  cookie: { secure: false }
}))


const { MongoClient } = require('mongodb');
const path = require("path");
const uri = "mongodb+srv://micro1:micro1@cluster0.u4edv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
const db = client.db("userDB");
const collection = db.collection("user");
client.connect(err => {

  if (err) console.error(err)
  else console.log('Connected successfully to server');

});



//Setting for ejs
app.set("view engine", "ejs");
app.set("views", "./views");
dotenv.config();

//Set user function
function setUser(req, user) {
  req.session[SESSION_AUTH_USER] = user
}

//Get user function
function getUser(req) {
  return req.session[SESSION_AUTH_USER] || null
}

//Clear user function
function clearUser(req) {
  setUser(req, null)
}

//Function to check if the user login or not
function isLogin(req) {
  return getUser(req) != null
}

//Function when we know that the user is not login yet
function notauth(req, res) {
  if (!isLogin(req)) {
    let query = qureystring.stringify({
      fromUrl: req.originalUrl,
    })
    res.redirect('/login')
    return true
  }
  return false
}

//Function when we know that the user is not login yet
function notauthHome(req, res) {
  if (!isLogin(req)) {
    let query = qureystring.stringify({
      fromUrl: req.originalUrl,
    })
    res.redirect('/homein')
    return true
  }
  return false
}

//main home page
app.get("/", (req, res) => {
  if (notauthHome(req, res)) return;
  let user = getUser(req)
  res.render('home', {
    user,
  });
});
app.get("/home", (req, res) => {
  if (notauthHome(req, res)) return;
  let user = getUser(req)
  res.render('home', {
    user,
  });
});

app.get("/homein", (req, res) => {
  res.render('homeNotAuth')
});

app.get("/launch", async (req, res) => {
  res.send("testing");
  let pathDir = path.resolve(process.cwd() + '/..' + '/script')
  let scriptPath = path.resolve(pathDir + '/launch-example/test.sh');
  const x = spawn(scriptPath, {
    cwd: path.resolve(pathDir, 'launch-example'),
    stdio: ['ignore', 'inherit', 'inherit']
  });
  x.on("exit", () => {
    fork("log-parser/index.js", {
      cwd: pathDir
    });
  });
})

//login page
app.get('/login', (req, res) => {
  res.render('login', {
    invalid: req.query['invalid'] || false,
    fromUrl: req.query['fromUrl'] || '/login'
  })
})

//When click login
app.post('/login', (req, res) => {
  let { username, password, fromUrl } = req.body
  collection.find({ email: username, password: md5(password) }).toArray(function (err, users) {
    if (err || users.length != 1) {
      return res.redirect('/login?invalid=1')
    }
    let user = users[0]
    delete user.password
    setUser(req, user)
    res.redirect('/home')

  });

})

//register page
app.get("/register", (req, res) => {
  res.render("register", {
    Uinvalid: req.query['Uinvalid'] || false,
    fromUrl: req.query['fromUrl'] || '/register'
  });
});

//When click register
app.post('/register', (req, res) => {

  let fname = req.body['fname']
  let lname = req.body['lname']
  let email = req.body['email']
  let password = req.body['password']
  var myobj = { fname: fname, lname: lname, email: email, password: md5(password), pass: "FALSE" };

  collection.find({ email: email }).toArray(function (err, users) {
    if (err || users.length !== 0) {

      res.redirect('/register?Uinvalid=1');

    } else {
      collection.insertOne(myobj, function (err) {
        if (err) throw err;
        console.log("1 user inserted");
        res.redirect('/login')
      });
    }

  });

})

//lesson page
app.get("/content", (req, res) => {
  if (notauth(req, res)) return;
  let user = getUser(req)
  res.render('content', {
    user,
  });
});

//testing tool page
app.get("/testingtool", (req, res) => {
  if (notauth(req, res)) return;
  let user = getUser(req)
  res.render('testingtool', {
    user,
  });
});

app.get("/result", (req, res) => {
  // if (notauth(req, res)) return;
  let user = getUser(req)
  fs.readFile('../output/output.json', 'utf8', (err, data) => {
    if (err) {
      return console.log("File read failed:", err)
    }
    var resultList = JSON.parse(data);
    var main5xx = 0;
    var main4xx = 0;
    var sub5xx = 0;
    var sub4xx = 0;

    var trackId = [];


    for (let result of resultList) {
      if (result.request === null) {

      }
      else if (result.request.status_code >= 400 && result.request.status_code < 500) {
        main4xx += 1;
      } else if (result.request.status_code >= 500 && result.request.status_code < 600) {
        main5xx += 1;
        trackId.push({ id: result.request.subrequest });

      }
      for (let subrequest of result.subrequest) {
        if (subrequest.status_code >= 400 && subrequest.status_code < 500) {
          sub4xx += 1;
        }
        else if (subrequest.status_code >= 500 && subrequest.status_code < 600) {
          sub5xx += 1;
          trackId.push({ id: result.request.subrequest });
        }
      }
    }
    console.log(trackId);
    res.render('result', {
      results: resultList,
      main4xxs: main4xx,
      main5xxs: main5xx,
      sub4xxs: sub4xx,
      sub5xxs: sub5xx,
      trackIds: trackId,
      user
    })
    //console.log(data)
  });

});

//save dict to file
app.get("/saveDict_json", (req, res) => {
  fs.writeFile("../grammar/dict.json", req.query.data, function (err) {
    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
    res.end("This message will be sent back to the client!");
  });
  var data = req.query.data;
  console.log(data);
});

//save dyn to file
app.get("/saveDyn_json", (req, res) => {
  fs.writeFile("../grammar/restler_user_settings.json", req.query.data, function (err) {
    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
    res.end("This message will be sent back to the client!");
  });
  var data = req.query.data;
  console.log(data);
});

//print page
app.get("/print", (req, res) => {
  res.render("print2");
});


app.get("/pdf", (req, res) => {
  if (notauth(req, res)) return;
  let user = getUser(req);
  let fname = user.fname;
  let lname = user.lname;
  // Import dependencies
  const fs = require("fs");
  const moment = require("moment");
  const PDFDocument = require("pdfkit");

  collection.updateOne({ email: user.email },
    {
      $set: { "pass": "TRUE" },
    }, function (err) {
      if (err) throw err;
      console.log("Updated Status");

    });



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
    align: "center"
  });

  // Draw the date
  doc.fontSize(15).text(moment().format("MMMM Do YYYY"), 175, 420, {
    align: "center"
  });

  // Finalize the PDF and end the stream
  doc.end();
  console.log("The certificate was created!");

  res.end("This message will be sent back to the client!");
  //res.redirect('/quiz')

});


//quiz page
app.get("/quiz", (req, res) => {
  if (notauth(req, res)) return;
  let user = getUser(req)
  let fname = user.fname;
  let lname = user.lname;
  collection.find({ email: user.email, pass: "TRUE" }).toArray(function (err, users) {
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
        align: "center"
      });

      // Draw the date
      doc.fontSize(15).text(moment().format("MMMM Do YYYY"), 175, 420, {
        align: "center"
      });

      // Finalize the PDF and end the stream
      doc.end();
      console.log("The certificate was created!");
      res.render('quiz', {
        user,
        pass: "TRUE"
      });

    } else {
      res.render('quiz', {
        user,
        pass: "FALSE"
      });
    }

  });
});

//contact us  page
app.get("/aboutus", (req, res) => {
  res.render("aboutus");
});

//When logout
app.get('/logout', (req, res) => {

  clearUser(req)
  res.redirect('/home')

})

//run
app.listen(8080, function () {
  console.log("Listening at Port " + 8080);
});
