//Require
var request = require('request');

//View
var display = require("../views/display.ejs");

//Class
var requestManager = {
	handleRequest: function(req, res){
		var query = req.query.tag;
		var tags = query.split(';');
		request.post(
			'http://127.0.0.1:8080/recom',
			{form: {tags: tags}},
			function (err, response, body){
				if(!err && response.statusCode == 200){
					res.send(body);
				}
			}
		);
	},
};
module.exports = requestManager;