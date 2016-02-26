//Require
//Model
var recommender = require('../model/recommender.js');
var question = require('../model/question.js');
var answer = require('../model/answer.js');

//View
var display = require("../views/display.ejs");

//Class
var requestManager = {
	handleRequest: function(req, res){
		var query = req.query.tag;
		var tags = query.split(';');
		res.render('display');
		//var ids = recommender.getRecommendation(tags);
	}
};
module.exports = requestManager;