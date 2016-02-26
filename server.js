//Import
var express = require('express');
var ejs = require('ejs');

//Controller
var controller = require("./controller/request.js");

//Init
var app = express();
app.set('view engine', 'ejs');

//Server Start
app.listen(80, function(){
	console.log("Server listening now!");
});

//Get Request
app.get('/', function(req,res){
	controller.handleRequest(req, res);
});