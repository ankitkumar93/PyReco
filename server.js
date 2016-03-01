//Import
var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');

//Controllers
var controller = require("./controller/request.js");
var recommender = require('./controller/recommender.js');
var question = require('./controller/question.js');
var answer = require('./controller/answer.js');

//Init
var app = express();
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));
//Server Start
app.listen(8080, function(){
	console.log("Server listening now!");
});

//Get Requests
app.get('/req', function(req,res){
	controller.handleRequest(req, res);
});

//Post Requests
app.post('/recom', function(req, res){
	recommender.handleRecomm(req, res);
});

app.post('/ques', function(req, res){
	question.handleQuestions(req, res);
});