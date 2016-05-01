#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#db
#names
dbname = "project2"
coll_name_comments_raw = "raw_comments"
coll_name_comments = "comments"
coll_name_dev = "developer"

#place holders
db = MongoClient()[dbname]
coll_comments_raw = db[coll_name_comments_raw]
coll_comments = db[coll_name_comments]
coll_dev = db[coll_name_dev]

#tags
#dev
dev_name_tag = 'Dev_NAME'
dev_id_tag = 'Dev_ID'

#comment
comment_message_tag = 'Message'

#general
message_tag = "body"
user_tag = "user"
login_tag = "login"


#fetch list of raw commits
def fetch_raw_comments():
    data = coll_comments_raw.find()
    return data

#fetch the dev id
def fetch_dev_id(name):
    data = coll_dev.find({dev_name_tag : name})
    dev_data = data[0]
    return dev_data[dev_id_tag]

#insert refined commit into collection
def insert_comment(dev_id, message):
    doc = {}
    doc[dev_id_tag] = dev_id
    doc[comment_message_tag] = message
    coll_comments.insert_one(doc)


#refine commits
def refine_comments():
    comment_list = fetch_raw_comments()
    for comment in comment_list:
        user = comment[user_tag]
        if user is not None:
            message = comment[message_tag]
            dev_name = user[login_tag]
            dev_id = fetch_dev_id(dev_name)
            insert_comment(dev_id, message)



def main():
    refine_comments()

if __name__ == "__main__":
  main()
