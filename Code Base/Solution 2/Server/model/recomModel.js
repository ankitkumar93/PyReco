//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var recomSchema = new Schema({
	id: {type: String, required: true, unique: true},
	tag: String
});

//Model
var recomModel = mongoose.model('sol2', recomSchema);

module.exports = recomModel;