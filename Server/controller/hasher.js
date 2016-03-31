//Require
var hashModel = require('../model/hashModel.js');

//Helper Functions
function findHashes(idlist, res){
		hashModel.find({"Id": {$in: idlist}}, function(err, data){
			var object = null;
			if(typeof data != "undefined"){
				object = new Object();
				object['hash'] = data['Hash']
				object['ids'] = data['Id']
			}
			res.send(object);
		});
}

var answer = {
	handleHashes: function(req, res){
		var ids = req.body.ids;
		findHashes(ids, res);
	}
};
module.exports = answer;