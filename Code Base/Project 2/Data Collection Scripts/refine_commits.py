#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#db
#names
dbname = "project2"
coll_name_commits_raw = "raw_commits"
coll_name_commits = "commits"
coll_name_collaborators = "collaborators"
coll_name_dev = "developer"

#place holders
db = MongoClient()[dbname]
coll_commits_raw = db[coll_name_commits_raw]
coll_commits = db[coll_name_commits]
coll_collaborators = db[coll_name_collaborators]
coll_dev = db[coll_name_dev]

#tags
#repo
repo_id_tag = 'Repo_ID'

#dev
dev_name_tag = 'Dev_NAME'
dev_id_tag = 'Dev_ID'

#commit
commit_timestamp_tag = 'Timestamp'
commit_message_tag = 'Message'

#general
message_tag = "message"
author_tag = "author"
login_tag = "login"
commit_tag = 'commit'
timestamp_tag = 'date'


#fetch list of raw commits
def fetch_raw_commits():
    data = coll_commits_raw.find()
    return data

#fetch the dev id
def fetch_dev_id(name):
    data = coll_dev.find({dev_name_tag : name})
    dev_data = data[0]
    return dev_data[dev_id_tag]

#fetch the repo id
def fetch_repo_id(dev_id):
    data = coll_collaborators.find({dev_id_tag : dev_id})
    collaborators_data = data[0]
    return collaborators_data[repo_id_tag]

#insert refined commit into collection
def insert_commit(dev_id, timestamp, repo_id, message):
    doc = {}
    doc[dev_id_tag] = dev_id
    doc[repo_id_tag] = repo_id
    doc[commit_timestamp_tag] = timestamp
    doc[commit_message_tag] = message
    coll_commits.insert_one(doc)


#refine commits
def refine_commits():
    commit_list = fetch_raw_commits()
    for commit in commit_list:
        author = commit[author_tag]
        if author is not None:
            message = commit[commit_tag][message_tag]
            timestamp = commit[commit_tag][author_tag][timestamp_tag]
            dev_name = author[login_tag]
            dev_id = fetch_dev_id(dev_name)
            repo_id = fetch_repo_id(dev_id)
            insert_commit(dev_id, timestamp, repo_id, message)



def main():
    refine_commits()

if __name__ == "__main__":
  main()
