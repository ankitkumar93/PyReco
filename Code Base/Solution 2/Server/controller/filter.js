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
	var size = 100 < body.length ? 100:body.size;
	var output = new Array();
	for(i = 0; i < size; i++){
		output[i] = body[i];
	}
	return output;
}

//Filter Second:
function sortScore(questions){
	questions.sort(compareScore);
	var output = new Array();
	var size = 10 < questions.length ? 10:questions.size;
	for(i = 0; i < size; i++){
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