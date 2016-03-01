//Import
var express = require('express');
var ejs = require('ejs');
var bodyParser = require('body-parser');

//Controllers
var controller = require("./controller/request.js");
var recommender = require('./controller/recommender.js');
var question = require('./controller/question.js');
var answer = require('./controller/answer.js');

//Init
var app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));
//Server Start
app.listen(8080, function(){
	console.log("Server listening now!");
});

//Get Requests
app.get('/', function(req,res){
	controller.handleRequest(req, res);
});

//Post Requests
app.post('/recom', function(req, res){
	recommender.handleRecomm(req, res);
});

app.post('/ques', function(req, res){
	question.handleQuestions(req, res);
});