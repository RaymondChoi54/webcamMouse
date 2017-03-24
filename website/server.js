var express = require('express');
var bodyParser = require('body-parser');
var nodemailer = require('nodemailer');

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
	
	console.log("POST /submit")

	email = req.body.email

	fullText = "Hello " + req.body.firstname + ",\nThank you for your message. We greatly value the opinion of our users. We'll review the feedback and get in touch!\nThanks,\nThe LimbsFree Team"

	transporter = nodemailer.createTransport({
    	service: 'gmail',
    	auth: {
        	user: 'limbsfree@gmail.com',
        	pass: 'helloworld'
    	}
	});

	mailOptions = {
    from: '"LimbsFree Team" <limbsfree@gmail.com>', // sender address
    to: email, // list of receivers
    subject: 'Thank you for your comments', // Subject line
    text: fullText, // plain text body
	};

	transporter.sendMail(mailOptions, function(err, info) {
    	if (error) {
        	return console.log(error);
    	}
    	console.log('Message %s sent: %s', info.messageId, info.response);
	});


	res.sendfile('homepage.html')
});

app.listen(process.env.PORT || 3000);
console.log('Listening on port 3000');