var express = require('express');
var bodyParser = require('body-parser');
//var nodemailer = require('nodemailer');

var app = express();
//app.use(express.static(__dirname + '/assets'));
app.use(express.static(__dirname + '/'));


// The request body is received on GET or POST.
// A middleware that just simplifies things a bit.
app.use(bodyParser.json()); // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({ // to support URL-encoded bodies
    extended: true
}));

// Get the index page:
app.get('/', function(req, res) {
    res.sendfile('homepage.html');
    console.log("GET /");
});

//Get the download in motion
app.get('/download', function(req, res) {

});

//submit feedback
app.post('/submit', function(req, res) {

});

app.listen(process.env.PORT || 3000);
console.log('Listening on port 3000');