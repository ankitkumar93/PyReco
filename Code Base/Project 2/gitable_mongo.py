#  gitabel
#  the world's smallest project management tool
#  reports relabelling times in github (time in seconds since epoch)
#  thanks to dr parnin
#  todo:
#    - ensure events sorted by time
#    - add issue id
#    - add person handle

"""
You will need to add your authorization token in the code.
Here is how you do it.
1) In terminal run the following command
curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "SE Project"}' https://api.github.com/authorizations
2) Enter ur password on prompt. You will get a JSON response.
In that response there will be a key called "token" .
Copy the value for that key and paste it on line marked "token" in the attached source code.
3) Run the python file.
     python gitable.py
"""

from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
from pymongo import MongoClient

#db
dbname = "project2"
coll_issues_name = "raw_issues"
coll_commits_name = "raw_commits"
coll_milestones_name = "raw_milestones"
db = MongoClient()[dbname]
coll_issues = db[coll_issues_name]
coll_commits = db[coll_commits_name]
coll_milestones = db[coll_milestones_name]

#repos
repo_names = ['ankitkumar93/csc510-se-project', 'jordy-jose/CSC_510_group_d', 'moharnab123saikia/CSC510-group-f', 'cleebp/csc-510-group-g']

#token
token = "1a0895991496c60384e1b420d43a397e161951c9"

def dump_data(url, collection):
  try:
    request = urllib2.Request(url, headers={"Authorization" : "token "+token})
    v = urllib2.urlopen(request).read()
    w = json.loads(v)
    if not w: return False
    for data in w:
      collection.insert_one(data)
    return True
  except Exception as e:
    print(e)
    print("Contact TA")
    return False

def fetchIssues(repo_name):
  print("Issues Init")
  page = 1
  while(True):
    doNext = dump_data('https://api.github.com/repos/' + repo_name + '/issues/events?page=' + str(page), coll_issues)
    print("page "+ str(page))
    page += 1
    if not doNext : break
  print("Issues Done")

def fetchCommits(repo_name):
  print("Commits Init")
  page = 1
  while(True):
    doNext = dump_data('https://api.github.com/repos/' + repo_name + '/commits?page=' + str(page), coll_commits)
    print("page "+ str(page))
    page += 1
    if not doNext : break
  print("Commits Done")

def fetchMilestones(repo_name):
  print("Milestones Init")
  page = 1
  while(True):
    doNext = dump_data('https://api.github.com/repos/' + repo_name + '/milestones?state=all&page=' + str(page), coll_milestones)
    print("page "+ str(page))
    page += 1
    if not doNext : break
  print("Milstones Done")

def main():
    for repo_name in repo_names:
        print("Repo Being Considered: " + repo_name)
        fetchIssues(repo_name)
        fetchCommits(repo_name)
        fetchMilestones(repo_name)

if __name__ == "__main__":
  main()
