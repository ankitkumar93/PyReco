//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var hashSchema = new Schema({
	Id: {type: Number, required: true, unique: true},
	Hash: String
});

//Model
var hashModel = mongoose.model('qhash', hashSchema);

module.exports = hashModel;