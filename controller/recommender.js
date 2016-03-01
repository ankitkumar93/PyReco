//Require
var mongoose = require("mongoose");
var recomModel = require('../model/recomModel.js');
//Db
var db = 'pyreco';

//Helper Functions
function connecttodb(){
	mongoose.connect('mongodb://localhost/'+db);
}

function formQueryString(taglist){
	var queryString = '';
	for(index in taglist){
		if(index < taglist.length - 1)
			queryString +='"' + taglist[index] + '" ';
	}
	return queryString;
}

function findAll(taglist, res){
	connecttodb();
	var queryString = formQueryString(taglist);
	recomModel.find({$text:{$search:queryString}}, function(err, data){
		var ids = new Array();
		for(index in data){
			ids.push(data[index].id);
		}
		var object = new Object();
		object["ids"] = ids;
		res.send(object);
	});
}

var recommender = {
	handleRecomm: function(req, res){
		var taglist = req.body.tags;
		findAll(taglist, res);
	}
};
module.exports = recommender;