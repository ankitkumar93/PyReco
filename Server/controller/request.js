//Require
var request = require('request');
var mongoose = require("mongoose");
var filter = require('./filter.js');
var hashfilter = require('./hashfilter.js');

//Db
var db = 'pyreco';

//Helper Functions
function connecttodb(){
	mongoose.connect('mongodb://localhost/'+db);
}

function closeconnectiontodb(){
	mongoose.connection.close();
}

//Helper Functions
function getQuestions(ids, res){
	request.post(
		'http://127.0.0.1:8080/ques',
		{form: {ids: ids}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				var ques = JSON.parse(body).ques;
				if(ques.length == 0){
					closeconnectiontodb();
					res.send(ques);
				}
				else{
					var filteredQuestions = filter.filterQuestions(ques);
					res.send(filteredQuestions);
				}
			}else{
				res.send("questions: " + err);
			}
			closeconnectiontodb();
		}
	);
}

function getHash(ids, tags, res){
	request.post(
		'http://127.0.0.1:8080/gethash',
		{form: {ids: ids}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				var hashes = JSON.parse(body).hashes;
				if(hashes.length == 0){
					closeconnectiontodb();
					res.send(hashes);
				}
				else{
					var filteredIds = hashfilter.filter(body, tags);
					getQuestions(filteredIds, res);
				}
			}else{
				res.send("hash: " + err);
				closeconnectiontodb();
			}
		}
	);
}

function getRecommendation(tags, res){
	request.post(
		'http://127.0.0.1:8080/recom',
		{form: {tags: tags}},
		function (err, response, body){
			if(!err && response.statusCode == 200){
				var ids = JSON.parse(body).ids;
				if(ids.length == 0){
					closeconnectiontodb();
					res.send(ids);
				}
				else
					getHash(ids, tags, res);
			}else{
				res.send("recommendor: " + err);
				closeconnectiontodb();
			}
		}
	);
}

//Class
var requestManager = {
	handleRequest: function(req, res){
		var query = req.body.tag;
		var tags = query.split(';');
		var taglist = new Array();
		for(index in tags){
			var currtag = tags[index];
			if(currtag != '')
				taglist.push(currtag);
		}
		connecttodb();
		getRecommendation(taglist, res);
	}
};
module.exports = requestManager;