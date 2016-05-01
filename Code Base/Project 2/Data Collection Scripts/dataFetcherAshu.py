#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from pymongo import MongoClient
import sys

#db
#names
dbname = "seproj2"
# coll_name_dev = "developer"
coll_name_repo = "repo"
# coll_name_collaborators = "collaborators"
coll_name_issues = "issues"
coll_name_issuedata = "issuedata"

#place holders
db = MongoClient()[dbname]
# coll_dev = db[coll_name_dev]
coll_repo = db[coll_name_repo]
coll_issues = db[coll_name_issues]
# coll_collaborators = db[coll_name_collaborators]
coll_issuesdata = db[coll_name_issuedata]

#tags
#repo
repo_url_tag = 'Repo_URL'
repo_id_tag = 'Repo_ID'

#repos urls
repo_names = ["ankitkumar93/csc510-se-project", "jordy-jose/CSC_510_group_d", "moharnab123saikia/CSC510-group-f", "cleebp/csc-510-group-g"]

#url prefix
gitapi_url_prefix = "https://api.github.com/repos/"
github_url_prefix = "https://github.com/"

#ignores
dev_ignore_list = ["timm", "history"]

#fetch list of devs for a repo
def fetch_issues():
    issue_list = []
    data = coll_issues.find()
    for row in data:
        labels = []
        #print row['issue']
        issue_id = row['issue']['id']
        issue_title = row['issue']['title']
        issue_created_at = row['issue']['created_at']
        issue_closed_at = row['issue']['closed_at']
        issue_author = row['issue']['user']['login']
        issue_labels = row['issue']['labels']
        if issue_labels:
            for a in issue_labels:
                labels.append(a['name'])
        assignee = row['issue']['assignee']
        if assignee:
            assignee = row['issue']['assignee']['login']
        issue_comments = row['issue']['comments']
        issue_state = row['issue']['state']
        issue_milestone = row['issue']['milestone']
        if issue_milestone:
            issue_milestone = issue_milestone['id']
        issue_list.append([issue_id, issue_title, issue_created_at, issue_closed_at, issue_author, assignee, labels, issue_comments, issue_state, issue_milestone])
        funcInsertInTable(issue_id, issue_title, issue_created_at, issue_closed_at, issue_author, assignee, labels, issue_comments, issue_state, issue_milestone)
    return issue_list

#anonymize repos statically
def anonymize_repos():
    print("Anonymize Repos Init")
    id = 0
    for name in repo_names:
        url = github_url_prefix + name
        doc = {}
        doc[repo_url_tag] = url
        doc[repo_id_tag] = id
        coll_repo.insert_one(doc)
        id += 1
    print("Anonymize Repos Done")

#anonymize devs
def anonymize_devs():
    print("Anonymize Devs Init")
    id = 0
    for name in repo_names:
        github_url = github_url_prefix + name
        gitapi_url = gitapi_url_prefix + name
        data = coll_repo.find({repo_url_tag : github_url})
        issue_list = fetch_issues()
        # for issue in issue_list:
        #     funcInsertInTable(issue)
            # doc = {}
            # doc['Id'] = id
            # doc['Issue Body'] = issue
            # coll_issuesdata.insert_one(doc)
            # id+= 1
    print("Anonymize Issues Done")

def funcInsertInTable(issue_id, issue_title, issue_created_at, issue_closed_at, issue_author, assignee, labels, issue_comments, issue_state, issue_milestone):
    coll_issuesdata.insert_one({
        "Issue_ID" : issue_id, 
        "Issue_Title" : issue_title, 
        "Issue_Created_At" : issue_created_at, 
        "Issue_Closed_At" : issue_closed_at, 
        "Author" : issue_author, 
        "Assignee" : assignee, 
        "Labels" : labels, 
        "Issue_Comments" : issue_comments, 
        "Issue_State" : issue_state, 
        "Milestone" : issue_milestone
        })

#set collaborators
# def set_collaborator(dev_id, repo_id):
#     doc = {}
#     doc[repo_id_tag] = repo_id
#     doc[dev_id_tag] = dev_id
#     coll_issuesdata.insert_one(doc)

def main():
    anonymize_repos()
    anonymize_devs()

if __name__ == "__main__":
  main()