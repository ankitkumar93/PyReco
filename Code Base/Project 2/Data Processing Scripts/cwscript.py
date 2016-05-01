#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient
from datetime import datetime
from time import strptime

#db
#names
dbname = "project2"
coll_name_repo = "repo"
coll_name_commits = "commits"
coll_name_cw = 'cw'

#place holders
db = MongoClient()[dbname]
coll_repo = db[coll_name_repo]
coll_commits = db[coll_name_commits]
coll_cw = db[coll_name_cw]

#collection tags
repo_id_tag = 'Repo_ID'
timestamp_tag = 'Timestamp'

#timestamp boundaries
twbegin = "2016-02-02"
tw_list =["2016-02-08", "2016-02-15", "2016-02-22", "2016-02-29", "2016-03-07", "2016-03-14", "2016-03-21", "2016-03-28"]

#helper functions
#get list of repo ids
def get_repo_list():
    repo_list = []
    data = coll_repo.find()
    for repo in data:
        repo_id = repo[repo_id_tag]
        repo_list.append(repo_id)
    return repo_list

#get list of commits
def get_commit_list(repo):
    commit_list = []
    data = coll_commits.find({repo_id_tag : repo})
    for commit in data:
        commit_list.append(commit)
    return commit_list

#feature extraction functions
#get commits per week
def commits_per_week(repo):
    commit_list = get_commit_list(repo)

    cpw = []

    ts_beg = datetime.strptime(twbegin, '%Y-%m-%d')
    td_list = []
    for tw in tw_list:
        ts_w = datetime.strptime(tw, '%Y-%m-%d')
        t_diff = (ts_w - ts_beg).total_seconds()
        td_list.append(t_diff)
        cpw.append(0)

    for commit in commit_list:
        timestamp = commit[timestamp_tag]
        date_str = timestamp.split("T")[0]
        ts_commit = datetime.strptime(date_str, '%Y-%m-%d')
        time_diff = (ts_commit - ts_beg).total_seconds()

        if time_diff > 0:
            for index, td in enumerate(td_list):
                if time_diff < td:
                    cpw[index] += 1
                    break

    return cpw

#insert document in the collection gu
def insert_in_cw(repo_id, cpw):
    doc = {}
    doc[repo_id_tag] = repo_id

    for index, cpwval in enumerate(cpw):
        doc[str(index+1)] = cpwval

    coll_cw.insert_one(doc)

#process the featurs
def process_features():
    repo_list = get_repo_list()
    for repo in repo_list:
        cpw = commits_per_week(repo)
        insert_in_cw(repo, cpw)

def main():
    process_features()

if __name__ == "__main__":
    main()
