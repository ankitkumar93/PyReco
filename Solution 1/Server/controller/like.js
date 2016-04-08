//Require
var likeModel = require("../model/likeModel.js");
var mongoose = require("mongoose");

//Db
var db = 'pyreco';

//Helper Functions
function connecttodb(){
	mongoose.connect('mongodb://localhost/'+db);
}

function closeconnectiontodb(){
	mongoose.connection.close();
}

function addLikeToDb(data, res){
	var dataJSON = {id: String(data.id), index: String(data.index), sol: "sol1"};
	var likeData = new likeModel(dataJSON);
	console.log(dataJSON);
	connecttodb();
	likeData.save(function(err, data){
		if(err){
			console.log("error with like insertion: " + err);
			res.send(err);
		}else{
			console.log("like inserted!");
			res.send(data);
		}
		closeconnectiontodb();
	});
}


//Module
var likeManager = {
	addLike: function(req, res){
		var data = req.body;
		addLikeToDb(data, res);
	}
};

module.exports = likeManager;