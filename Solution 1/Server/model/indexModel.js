//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var indexSchema = new Schema({
	id: String,
	index: String,
	sol: String
}, {
	collection: 'clicks'
});

//Model
var indexModel = mongoose.model('clicks', indexSchema);

module.exports = indexModel;