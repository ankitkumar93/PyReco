//Require
var request = require('request');
var mongoose = require("mongoose");
var filter = require('./filter.js');

//Db
var db = 'pyreco';

//Helper Functions
function connecttodb(){
	mongoose.connect('mongodb://localhost/'+db);
}

function closeconnectiontodb(){
	mongoose.connection.close();
}

//Helper Functions
function getQuestions(ids, res){
	request.post(
		'http://127.0.0.1:8080/ques',
		{form: {ids: ids}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				var filteredQuestions = filter.filterQuestions(body);
				res.send(filteredQuestions);
			}else{
				res.send("questions: " + err);
			}
			closeconnectiontodb();
		}
	);
}

function getRecommendation(tags, res){
	request.post(
		'http://127.0.0.1:8080/recom',
		{form: {tags: tags}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				var bodyJSON = JSON.parse(body);
				getQuestions(bodyJSON.ids, res);
			}else{
				res.send("recommendor: " + err);
				closeconnectiontodb();
			}
		}
	);
}

//Class
var requestManager = {
	handleRequest: function(req, res){
		var query = req.body.tag;
		var tags = query.split(';');
		connecttodb();
		getRecommendation(tags, res);
	}
};
module.exports = requestManager;