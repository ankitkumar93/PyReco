var simhash = require('simhash')();

//Fetch hash data from the db
function getHashVal(hasharr){
	var hashval = 0;
	var length = hasharr.length;
	for(index in hasharr){
		if(hasharr[length - index - 1] == 1)
			hashval += Math.pow(2, index);
	}

	return hashval;
}

//Comparator for sortIds
function compareIds(id1, id2){
	if(id1.dist < id2.dist)
		return -1;
	else if(id1.dist > id2.dist)
		return 1;
	else
		return 0;
}

//Sort Ids based on hash distance
function sortHash(arr){
	var filtered = arr.sort(compareIds);
	var size = 100 < arr.length ? 100: arr.length;
	var returnarr = new Array();
	for(i = 0; i < size; i ++){
		returnarr[i] = filtered[i]["id"];
	}

	return returnarr;
}

//Return an object with ids mapped to hash distance
function getHashDistance(hashval, hasharr){
	var returnarr = new Array();
	for(index in hasharr){
		var currobj = hasharr[index];

		var distance = hashval ^ currobj["hash"];

		var object = new Object();
		object["id"] = currobj["id"];
		object["dist"] = distance;

		returnarr.push(object);
	}

	return returnarr;
}

var hashfilter = {
	filter: function(body, context){
		var hasharr = JSON.parse(body).hashes;

		var hashdata = simhash(context);
		var hashval = getHashVal(hashdata);

		var hashdistarr = getHashDistance(hashval, hasharr);

		var filteredarr = sortHash(hashdistarr);

		return filteredarr;

	}
};

module.exports = hashfilter;