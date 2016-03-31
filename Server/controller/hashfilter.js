var simhash = require('simhash')();

//Fetch hash data from the db
function getHashVal(hasharr){
	var hashval = 0;
	var length = hasharr.length;
	console.log(hasharr);
	for(index in hasharr){
		if(hasharr[length - index - 1] == 1)
			hashval += Math.pow(2, index);
	}

	return hashval;
}

//Comparator for sortIds
function compareIds(id1, id2){
	if(id1.hash < id2.hash)
		return 1;
	else if(id1.hash > id2.hash)
		return -1;
	else
		return 0;
}

//Sort Ids based on hash distance
function sortIds(object){
	var filtered = object.sort(compareIds);
	var size = 100 < object.length ? 100: object.length;
	var returnObject = new Array();
	for(i = 0; i < size; i ++){
		returnObject[i] = filtered[i];
	}

	return returnObject;
}

var hashfilter = {
	filter: function(body, context){
		var ids = JSON.parse(body).ids;
		//var context_tags = context.split(' ');
		var hashdata = simhash(context);
		var hashval = getHashVal(hashdata);

		return ids;

	}
};

module.exports = hashfilter;