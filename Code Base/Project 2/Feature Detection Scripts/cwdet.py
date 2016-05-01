#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#names
dbname = "project2"
coll_name_cw = 'cw'
coll_name_bscw = 'bscw'

#place holders
db = MongoClient()[dbname]
coll_cw = db[coll_name_cw]
coll_bscw = db[coll_name_bscw]

#collection tags
repo_id_tag = 'Repo_ID'
cw_tag = 'cw'

#helper functions
#get list of features in gu
def get_cw_list():
    cw_list = []
    data = coll_cw.find()
    for row in data:
        cw_list.append(row)
    return cw_list

def insert_bscw(repo_id, cw_val):
    doc = {}
    doc[repo_id_tag] = repo_id
    doc[cw_tag] = cw_val
    coll_bscw.insert_one(doc)

#process csm feature
def compute_feature_vals(features):
    for row in features:
        mean = 0
        index = 1
        while index < 9:
            mean += row[str(index)]
            index += 1
        mean /= 8

        limit = mean*1.5

        index = 1
        compare_val = 0
        while index < 9:
            if row[str(index)] > limit:
                compare_val = 1
                break
            index += 1
        insert_bscw(row[repo_id_tag], compare_val)

#process features for the bad small
def process_features():
    feature_list = get_cw_list()
    compute_feature_vals(feature_list)

#main
def main():
    process_features()

if __name__ == "__main__":
    main()
