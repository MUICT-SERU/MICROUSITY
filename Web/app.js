//import to use
const express = require('express')
const app = express()
const dotenv = require('dotenv');



//setting
app.use(express.static('public'))

app.use(express.json())
app.use(express.urlencoded({
    extended: true,
}))
//Setting for ejs
app.set('view engine', 'ejs')
app.set('views', './views')
dotenv.config();


//main home page
app.get('/', (req, res) => {
    res.render('home')
})


//run
app.listen(8088, function(){
    console.log("Listening at Port " + 8088);
});