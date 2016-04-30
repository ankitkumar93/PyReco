#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#db
#names
dbname = "project2"
coll_name_dev = "developer"
coll_name_repo = "repo"
coll_name_collaborators = "collaborators"
coll_name_issues = "raw_issues"

#place holders
db = MongoClient()[dbname]
coll_dev = db[coll_name_dev]
coll_repo = db[coll_name_repo]
coll_issues = db[coll_name_issues]
coll_collaborators = db[coll_name_collaborators]

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

#fetch list of devs for a repo
def fetch_devs(repo_url):
    dev_list = []
    data = coll_issues.find()
    for row in data:
        url = row[url_tag]
        if repo_url in url:
            login_name = row[actor_tag][login_tag]
            if login_name not in dev_list:
                if login_name not in dev_ignore_list:
                    dev_list.append(login_name)
    return dev_list

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
        dev_list = fetch_devs(gitapi_url)
        row = data[0]
        repo_id = row[repo_id_tag]
        for dev_name in dev_list:
            doc = {}
            doc[dev_id_tag] = id
            doc[dev_name_tag] = dev_name
            coll_dev.insert_one(doc)
            set_collaborator(id, repo_id)
            id += 1
    print("Anonymize Devs Done")

#set collaborators
def set_collaborator(dev_id, repo_id):
    doc = {}
    doc[repo_id_tag] = repo_id
    doc[dev_id_tag] = dev_id
    coll_collaborators.insert_one(doc)

def main():
    anonymize_repos()
    anonymize_devs()

if __name__ == "__main__":
  main()
