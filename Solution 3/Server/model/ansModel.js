//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var ansSchema = new Schema({
	Id: {type: String, required: true, unique: true},
	Title: String,
	Body: String,
	ViewCount: String,
	LastEditDate: String,
	AnswerCount: String,
	Score: String,
	OwnerDisplayName: String,
	PostTypeId: String,
	Body: String,
	Tags: String,
	LastEditorUserId: String,
	LastActivityDate: String,
	CommentCount: String,
	AcceptedAnswerId: String,
	CreationDate: String
});

//Model
var ansModel = mongoose.model('answers', ansSchema);

module.exports = ansModel;