var express = require('express');

//var nodemailer = require('nodemailer');

var app = express();
//app.use(express.static(__dirname + '/assets'));
app.use(express.static(__dirname + '/'));
var list=[];

// Get the index page:
app.get(['/', '/:file'],function(req, res, next) {
  if(req.params.file == 'list' || req.params.file == 'link' )
    next();
  else {
    res.sendfile('landing.html');
  }
});
app.get('/link',function (req,res){
  var link=req.query.link;
  var name=req.query.name;
  var tmp={};
  tmp["name"]=name;
  tmp["link"]=link;
  list.push(tmp);
  console.log(list);
  res.sendStatus(200);
});

app.get('/list',function (req,res){
  res.status(200).send(list);
});



app.listen(process.env.PORT || 3000);
console.log('Listening on port 3000');
