//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var hashSchema = new Schema({
	Id: {type: String, required: true, unique: true},
	Hash: {type: String, required: true}
});

//Model
var hashModel = mongoose.model('qhash', hashSchema);

module.exports = hashModel;