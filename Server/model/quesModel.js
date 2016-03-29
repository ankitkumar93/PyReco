//Require
var mongoose = require("mongoose");

//Schema
var Schema = mongoose.Schema;
var quesSchema = new Schema({
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
var quesModel = mongoose.model('questions', quesSchema);

module.exports = quesModel;