//Require
var mongoose = require("mongoose");

function getAnswer(id){
		return "hi";
}

var answer = {
	getAnswer: function(ids){
		var object = new Object();
		for(id in ids){
			object[id] = getAnswer(id);
		}
		return object;
	}
};
module.exports = answer;