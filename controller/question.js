//Require
var quesModel = require('../model/quesModel.js');

//Helper Functions
function findQuestions(idlist, res){
	console.log(idlist);
		quesModel.find({"Id": {$in: idlist}}, function(err, data){
			console.log("err: " + err);
			console.log("data: " + data);
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