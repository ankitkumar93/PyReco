#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#db
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
#names
dbname = "se_project2"
coll_name_milestone_raw = "milestone_raw"
coll_name_milestones = "milestones"
coll_name_issues = "issues"

#place holders
db = MongoClient(MONGO_CONNECTION_STRING)[dbname]
coll_name_milestone_raw = db[coll_name_milestone_raw]
coll_name_milestones = db[coll_name_milestones]
coll_name_issues = db[coll_name_issues]


#tags
#repo
repo_url_tag = 'Repo_URL'
repo_id_tag = 'Repo_ID'

#dev
dev_name_tag = 'Dev_NAME'
dev_id_tag = 'Dev_ID'

#general
url_tag = 'url'
actor_tag = 'actor'
login_tag = 'login'

#repos urls
repo_names = ["ankitkumar93/csc510-se-project", "jordy-jose/CSC_510_group_d", "moharnab123saikia/CSC510-group-f", "cleebp/csc-510-group-g"]

#url prefix
gitapi_url_prefix = "https://api.github.com/repos/"
github_url_prefix = "https://github.com/"

#ignores
dev_ignore_list = ["timm", "history"]

milestones_cursor = coll_name_milestone_raw.find()

#fetch list of devs for a repo
def fetch_issues(milestone_id):
    issues_list = []
    data = coll_issues.find()
    for row in data:
        url = row[url_tag]
        if repo_url in url:
            login_name = row[actor_tag][login_tag]
            if login_name not in dev_list:
                if login_name not in dev_ignore_list:
                    dev_list.append(login_name)
    return dev_list


#filter milestone
def filter_milestones():
    print("Filterng milestones Init")
    id = 0
    for milestone in milestones_cursor:
        Description = milestone['description']
        Created_Timestamp = milestone['created_at']
        Due_Timestamp = milestone['due_on']
        Closed_Timestamp = milestone['closed_at']
        milestone_id = milestone['id']
        fetch_issues(milestone_id)
        insert_milestone(Created_Timestamp,Due_Timestamp,Closed_Timestamp,milestone_id)
        

    print("Anonymize Devs Done")

# # insert milestone
def insert_milestone(Created_Timestamp, Due_Timestamp, Closed_Timestamp,milestone_id):
  print('inside insert ')
  coll_name_milestones.insert_one({
    "Milestone_ID" : milestone_id,
    "Created_Timestamp" : Created_Timestamp,
    "Due_Timestamp" : Due_Timestamp,
    "Closed_Timestamp" : Closed_Timestamp
    })

def main():
    filter_milestones()

if __name__ == "__main__":
  main()
