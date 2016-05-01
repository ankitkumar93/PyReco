#Created by Ashutosh Chaturvedi (achatur) for CSC-510 Project 2 Sprint 2016
from pymongo import MongoClient
import sys
import csv

#db
#names
dbname = "seproj2"
coll_name_dev = "developer"
coll_name_repo = "repo"
coll_name_issuedata = "issuedata"
coll_name_commits = "commits"
coll_name_comments = "comments"

#place holders
db = MongoClient()[dbname]
coll_dev = db[coll_name_dev]
coll_repo = db[coll_name_repo]
coll_issuesdata = db[coll_name_issuedata]
coll_commits = db[coll_name_commits]
coll_comments = db[coll_name_comments]

# dict for output data
dict_commits_per_user = {}
dict_comments_per_user = {}
dict_issues_per_user = {}
dict_issues_assigned_per_user = {}

def funcGetCommitsData():
	global dict_commits_per_user
	commit_data = coll_commits.find()
	for data in commit_data:
		if data["Dev_ID"] in dict_commits_per_user:
			dict_commits_per_user[data["Dev_ID"]] += 1
		else:
			dict_commits_per_user[data["Dev_ID"]] = 1

def funcGetCommentsData():
	global dict_comments_per_user
	comment_data = coll_comments.find()
	for data in comment_data:
		if data["Dev_ID"] in dict_comments_per_user:
			dict_comments_per_user[data["Dev_ID"]] += 1
		else:
			dict_comments_per_user[data["Dev_ID"]] = 1

def funcGetIssuesCreatedData():
	global dict_issues_per_user
	issues_data = coll_issuesdata.find()
	for data in issues_data:
		if data["Author"] in dict_issues_per_user:
			dict_issues_per_user[data["Author"]] += 1
		else:
			dict_issues_per_user[data["Author"]] = 1

def funcGetIssuesAssignedData():
	global dict_issues_assigned_per_user
	issues_data = coll_issuesdata.find()
	for data in issues_data:
		if data["Assignee"] in dict_issues_assigned_per_user:
			dict_issues_assigned_per_user[data["Assignee"]] += 1
		else:
			dict_issues_assigned_per_user[data["Assignee"]] = 1


def main():
	global dict_commits_per_user, dict_comments_per_user, dict_issues_per_user, dict_issues_assigned_per_user

	# get commits per user
	funcGetCommitsData()

	# get comments by each user
	funcGetCommentsData()

	# get issues created by each user
	funcGetIssuesCreatedData()
	
	# get issues assigned per user
	funcGetIssuesAssignedData()

	dicts = dict_commits_per_user, dict_comments_per_user, dict_issues_per_user, dict_issues_assigned_per_user
	keys = []
	for d in dicts:
		keys = keys + d.keys()
	keys = set(keys)
	keys = list(keys)
	with open("user_data.csv", "wb") as ofile:
		writer = csv.writer(ofile, delimiter='\t')
		writer.writerow(['ID', 'commits_per_user', 'comments_per_user', 'issues_per_user', 'issues_assigned_per_user'])
		for key in keys:
			if key == "None":
				key = "None"
			writer.writerow([key] + [d.get(key, None) for d in dicts])
if __name__ == "__main__":
  main()

