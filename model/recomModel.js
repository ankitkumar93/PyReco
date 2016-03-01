//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var recomSchema = new Schema({
	id: {type: String, required: true, unique: true},
	tags: {type: String, required: true},
});

//Model
var recomModel = mongoose.model('recomModel', recomSchema);

module.exports = recomModel;