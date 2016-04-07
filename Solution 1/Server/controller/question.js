//Require
var quesModel = require('../model/quesModel.js');

//Helper Functions
function getTop100(data){
	var size = 10 < data.length ? 10 : data.length;
	var index = 0;
	var output = new Array();
	for(; index < size; index++){
		output[index] = data[index];
	}

	return output;
}


function findQuestions(idlist, res){
		quesModel.find({"Id": {$in: idlist}}, function(err, data){
			var object = new Object();
			object['ques'] = getTop100(data);
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