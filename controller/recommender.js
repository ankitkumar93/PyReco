//Require
var mongoose = require("mongoose");
var recomModel = require('../model/recomModel.js');
//Db
var db = 'pyreco';

//Helper Functions
function connecttodb(){
	mongoose.connect('mongodb://localhost/'+db);
}

function findAll(taglist){
	recomModel.findAll({tags: taglist}, function(err, ids){
		return ids;
	});
}

var question = {
	getRecommIDs: function(taglist){
		var ids = findAll(taglist);
	}
};
module.exports = recommender;