//Require
var request = require('request');

//View
var display = require("../views/display.ejs");

//Helper Functions
function getQuestions(ids){
	request.post(
		'http://127.0.0.1:8080/ques',
		{form: {ids: ids}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				res.send(body);
			}else{
				res.send("questions: " + err);
			}
		}
	);
}

function getRecommendation(tags){
	request.post(
		'http://127.0.0.1:8080/recom',
		{form: {tags: tags}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				getQuestions(body.ids);
			}else{
				res.send("recommendor: " + err);
			}
		}
	);
}

//Class
var requestManager = {
	handleRequest: function(req, res){
		var query = req.query.tag;
		var tags = query.split(';');
		getRecommendation(tags);
	}
};
module.exports = requestManager;