//Comparator for View Count
function compareView(q1,q2){
	var view1 = Number.parseInt(q1.viewCount);
	var view2 = Number.parseInt(q2.viewCount);
	if(view1 > view2)
		return -1;
	else if(view1 < view2)
		return 1;
	else
		return 0;
}

//Comparator for Score
function compareScore(q1,q2){
	var score1 = Number.parseInt(q1.Score);
	var score2 = Number.parseInt(q2.Score);
	if(score1 > score2)
		return -1;
	else if(score1 < score2)
		return 1;
	else
		return 0;
}


//Sort by Votes and Return 100
function sortView(questions){
	var body = JSON.parse(questions).ques;
	body.sort(compareView);
	var output = new Array();
	for(i = 0; i < 100; i++){
		output[i] = body[i];
	}
	return output;
}

//Sort by Score and Return 10
function sortScore(questions){
	questions.sort(compareScore);
	var output = new Array();
	for(i = 0; i < 10; i++){
		output[i] = questions[i];
	}
	return output;
}

var filter = {
	filterQuestions: function(questions){
		var filter_view = sortView(questions);
		var filter_score = sortScore(filter_view);
		var filtered_questions = new Object();
		filtered_questions.ques = filter_score;
		return filtered_questions;
	}
};

module.exports = filter;