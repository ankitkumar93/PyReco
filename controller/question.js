//Require
var mongoose = require("mongoose");
var quesModel = require('../model/quesModel.js');
//Db
var db = 'pyreco';

//Helper Functions
function connecttodb(){
	mongoose.connect('mongodb://localhost/'+db);
}

function findQuestions(idlist, res){
		connecttodb();
		quesModel.find({"Id": idlist}, function(err, data){
			var object = new Object();
			object['ques'] = data;
			res.send(object);
		});
}

var question = {
	handleQuestions: function(req, res){
		var ids = req.body.ids;
		findQuestions(ids, res);
	}
};
module.exports = question;