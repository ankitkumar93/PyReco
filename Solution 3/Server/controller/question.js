//Require
var quesModel = require('../model/quesModel.js');

//Helper Functions
function findQuestions(idlist, res){
		quesModel.find({"Id": {$in: idlist}}, function(err, data){
			var object = null;
			if(typeof data != "undefined"){
				object = new Object();
				object['ques'] = data;
			}
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