var simhash = require('simhash')();

function getHashVal(hasharr){
	var hashval = 0;
	var length = hasharr.length;
	for(index in hasharr){
		if(hasharr[length - index - 1] == 1)
			hashval += Math.pow(2, index);
	}

	return hashval;
}

var hashfilter = {
	filter: function(body, context){
		var ids = JSON.parse(body).ids;
		//var context_tags = context.split(" ");

		var hashdata = simhash(context);
		var hashval = getHashVal(hashdata);
		console.log(hashval);

		return ids;

	}
};

module.exports = hashfilter;