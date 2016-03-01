//Require
var mongoose = require("mongoose");

function getQuestion(id){
		return "hi";
}

var question = {
	getQuestions: function(ids){
		var object = new Object();
		for(id in ids){
			object[id] = getQuestion(id);
		}
		return object;
	}
};
module.exports = question;