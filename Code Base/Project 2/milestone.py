#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient
import sys

#db
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
#names
dbname = "project2"
coll_name_milestone_raw = "raw_milestones"
coll_name_milestones = "milestones"
coll_name_issues = "issues"

#place holders
db = MongoClient(MONGO_CONNECTION_STRING)[dbname]
coll_name_milestone_raw = db[coll_name_milestone_raw]
coll_name_milestones = db[coll_name_milestones]
coll_name_issues = db[coll_name_issues]


milestones_cursor = coll_name_milestone_raw.find()


#fetch list of issues for a repo
def fetch_issues(milestone_id):
    issues_list = []
    issues_cursor = coll_name_issues.find({'Milestone': milestone_id})
    for issue in issues_cursor:
        Issue_ID = issue['Issue_ID']
        issues_list.append(Issue_ID)
    issues_list=issues_list
    return issues_list
    # print('milestone')
    # print(milestone_id)
    # print('issues')
    # print(issues_list)
    # print('count')
    # print(len(issues_list))
    # sys.exit(0)

# filter milestone
def filter_milestones():
    print("Filterng milestones Init")
    for milestone in milestones_cursor:
        Description = milestone['description']
        Created_Timestamp = milestone['created_at']
        Due_Timestamp = milestone['due_on']
        Closed_Timestamp = milestone['closed_at']
        milestone_id = milestone['id']
        milestone_title = milestone['title']
        issues = fetch_issues(milestone_id)
        insert_milestone(Created_Timestamp,Due_Timestamp,Closed_Timestamp,milestone_id,milestone_title,issues)
        

    print("Filterng milestones Done")

# insert milestone
def insert_milestone(Created_Timestamp, Due_Timestamp, Closed_Timestamp,milestone_id,milestone_title,issues):
  #print('inside insert ')
  coll_name_milestones.insert_one({
    "Milestone_ID" : milestone_id,
    "Milestone_Title" : milestone_title,
    "Created_Timestamp" : Created_Timestamp,
    "Due_Timestamp" : Due_Timestamp,
    "Closed_Timestamp" : Closed_Timestamp,
    "Issues" : issues
    })

def main():
    filter_milestones()

if __name__ == "__main__":
  main()
