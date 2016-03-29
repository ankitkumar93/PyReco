var simhash = require('simhash')('md5');

var hashfilter = {
	filter: function(body, context){
		var ids = JSON.parse(body).ids;
		//var context_tags = context.split(" ");

		var hashval = simhash(context);
		console.log(hashval);

		return ids;

	}
};

module.exports = hashfilter;