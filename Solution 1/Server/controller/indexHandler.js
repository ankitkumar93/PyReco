//Require
var indexModel = require("../model/indexModel.js");
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

function addIndexToDb(data, res){
	var dataJSON = {id: String(data.id), index: String(data.index), sol: "sol1"};
	var indexData = new indexModel(dataJSON);
	console.log(dataJSON);
	connecttodb();
	indexData.save(function(err, data){
		if(err){
			console.log("error with index insertion: " + err);
			res.send(err);
		}else{
			console.log("index inserted!");
			res.send(data);
		}
		closeconnectiontodb();
	});
}


//Module
var indexManager = {
	addIndex: function(req, res){
		var data = req.body;
		addIndexToDb(data, res);
	}
};

module.exports = indexManager;