//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var likeSchema = new Schema({
	id: String,
	index: String
}, {
	collection: 'likes'
});

//Model
var likeModel = mongoose.model('likes', likeSchema);

module.exports = likeModel;