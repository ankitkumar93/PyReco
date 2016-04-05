//Require
var hashModel = require('../model/hashModel.js');

//Helper Functions
function findHashes(idlist, res){
		hashModel.find({"Id": {$in: idlist}}, function(err, data){
			var arr = new Array();
			if(typeof data != "undefined"){
				for(index in data){
					var object = new Object();
					object['hash'] = data[index]['Hash'];
					object['id'] = data[index]['Id'];

					arr.push(object);
				}
			}
			var hasobject = new Object();
			hasobject['hashes'] = arr;
			res.send(hasobject);
		});
}

var answer = {
	handleHashes: function(req, res){
		var ids = req.body.ids;
		findHashes(ids, res);
	}
};
module.exports = answer;