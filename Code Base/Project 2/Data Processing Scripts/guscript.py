#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#db
#names
dbname = "project2"
coll_name_collaborators = "collaborators"
coll_name_issues = "issues"
coll_name_milestones = "milestones"
coll_name_commits = "commits"
coll_name_repo = 'repo'
coll_name_gu = 'gu'

#place holders
db = MongoClient()[dbname]
coll_collaborators = db[coll_name_collaborators]
coll_issues = db[coll_name_issues]
coll_milestones = db[coll_name_milestones]
coll_commits = db[coll_name_commits]
coll_repo = db[coll_name_repo]
coll_gu = db[coll_name_gu]

#collection tags
repo_id_tag = 'Repo_ID'
dev_id_tag = 'Dev_ID'
milestone_id_tag = 'Milestone_ID'
issue_id_tag = 'Issue_ID'
issue_comments_tag = 'Issue_Comments'
assignee_tag = 'Assignee'
labels_tag = 'Labels'
message_tag = 'Message'
author_tag = 'Author'
issues_tag = 'Issues'

#new tags
mwi_tag = 'mwi'
iwm_tag= 'iwm'
iwc_tag = 'iwc'
iwl_tag = 'iwl'
iwa_tag = 'iwa'
csm_tag = 'csm'

#helper functions
#get list of repo ids
def get_repo_list():
    repo_list = []
    data = coll_repo.find()
    for repo in data:
        repo_id = repo[repo_id_tag]
        repo_list.append(repo_id)
    return repo_list

#get list of milestones
def get_milestone_list(repo):
    milestone_list = []
    data = coll_milestones.find({repo_id_tag : repo})
    for miletone in data:
        milestone_list.append(miletone)
    return milestone_list

def get_dev_list(repo):
    dev_list = []
    data = coll_collaborators.find({repo_id_tag : repo})
    for dev in data:
        dev_id = dev[dev_id_tag]
        dev_list.append(dev_id)
    return dev_list

#get list of issues
def get_issue_list(repo):
    issue_list = []
    dev_list = get_dev_list(repo)
    for dev in dev_list:
        data = coll_issues.find({author_tag : dev})
        for issue in data:
            issue_list.append(issue)
    return issue_list

#get list of commits
def get_commit_list(repo):
    commit_list = []
    data = coll_commits.find({repo_id_tag : repo})
    for commit in data:
        commit_list.append(commit)
    return commit_list

#feature extraction functions
#get milestones without issues
def milestones_without_issues(repo):
    val = 0
    milestone_list = get_milestone_list(repo)

    for milestone in milestone_list:
        issue_list = milestone[issues_tag]
        if len(issue_list) == 0:
            val += 1

    return val

#get issues without milestones
def issues_without_milestones(repo):
    val = 0
    issue_list = get_issue_list(repo)

    for issue in issue_list:
        milestone_id = issue[milestone_id_tag]
        if milestone_id is None:
            val += 1

    return val

#get issues without comments
def issues_without_comments(repo):
    val = 0
    issue_list = get_issue_list(repo)

    for issue in issue_list:
        comments = issue[issue_comments_tag]
        if comments == 0:
            val += 1

    return val

#get issues without labels
def issues_without_labels(repo):
    val = 0
    issue_list = get_issue_list(repo)

    for issue in issue_list:
        label_list = issue[labels_tag]
        if len(label_list) == 0:
            val += 1

    return val

#get issues without assignees
def issues_without_assignees(repo):
    val = 0
    issue_list = get_issue_list(repo)

    for issue in issue_list:
        assignee = issue[assignee_tag]
        if assignee is None:
            val += 1

    return val

#get commits with same message
def commits_same_message(repo):
    val = 0
    commit_list = get_commit_list(repo)

    message_list = []
    for commit in commit_list:
        message = commit[message_tag]
        if message in message_list:
            val +=1
        else:
            message_list.append(message)

    return val

#insert document in the collection gu
def insert_in_gu(repo_id, mwi, iwm, iwc, iwl, iwa, csm):
    doc = {}
    doc[repo_id_tag] = repo_id
    doc[mwi_tag] = mwi
    doc[iwm_tag] = iwm
    doc[iwc_tag] = iwc
    doc[iwl_tag] = iwl
    doc[iwa_tag] = iwa
    doc[csm_tag] = csm
    coll_gu.insert_one(doc)

#process the featurs
def process_features():
    repo_list = get_repo_list()
    for repo in repo_list:
        mwi = milestones_without_issues(repo)
        iwm = issues_without_milestones(repo)
        iwc = issues_without_comments(repo)
        iwl = issues_without_labels(repo)
        iwa = issues_without_assignees(repo)
        csm = commits_same_message(repo)
        insert_in_gu(repo, mwi, iwm, iwc, iwl, iwa, csm)

def main():
    process_features()

if __name__ == "__main__":
    main()
