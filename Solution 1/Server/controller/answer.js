//Require
var ansModel = require('../model/ansModel.js');

//Helper Functions
function orderData(idlist, data){
	var output = new Array();
	for(index in idlist){
		var currid = idlist[index];
		for(index2 in data){
			var currdata = data[index2];
			if(currdata['Id'] == currid){
				output[index] = currdata;
				break;
			}
		}
	}
	
	return output;
}

function findAnswers(idlist, res){
		ansModel.find({"Id": {$in: idlist}}, function(err, data){
			var object = null;
			if(typeof data != "undefined"){
				object = new Object();
				object['ans'] = orderData(idlist, data);
			}
			res.send(object);
		});
}

function getAnsIds(ques){
	var ids = new Array();
	for(index in ques){
		ids.push(ques[index]['AcceptedAnswerId']);
	}
	return ids;
}

var question = {
	handleAnswers: function(req, res){
		var ques = req.body.ques;
		var ansIds = getAnsIds(ques);
		findAnswers(ansIds, res);
	}
};
module.exports = question;