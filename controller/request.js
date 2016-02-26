//Require
//Model
var recommender = require('../model/recommender.js');
var question = require('../model/question.js');
var answer = require('../model/answer.js');

//View
var display = require("../view/display.js");

//Class
var requestManager = {
	handleRequest: function(req, res){
		var query = req.query.tag;
		var tags = query.split(';');
		//var ids = recommender.getRecommendation(tags);
	}
};
module.exports = requestManager;