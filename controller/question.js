//Require
var quesModel = require('../model/quesModel.js');

//Helper Functions
function getIdList(ids){
	var idlist = new Array();
	for(index in ids){
		idlist.push(Number.parseInt(ids[index]));
	}
	return idlist;
}

function findQuestions(idlist, res){
	console.log(idlist);
		quesModel.find({"Id": idlist[0]}, function(err, data){
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
		var idlist = getIdList(ids);
		findQuestions(idlist, res);
	}
};
module.exports = question;