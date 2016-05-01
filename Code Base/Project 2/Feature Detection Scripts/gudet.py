#Created by Ankit Kumar(ankitkumar93) for CSC-510 Project 2 Sprint 2016
from __future__ import print_function
from pymongo import MongoClient

#names
dbname = "project2"
coll_name_gu = 'gu'
coll_name_bsgu = 'bsgu'

#place holders
db = MongoClient()[dbname]
coll_gu = db[coll_name_gu]
coll_bsgu = db[coll_name_bsgu]

#collection tags
repo_id_tag = 'Repo_ID'
mwi_tag = 'mwi'
iwm_tag= 'iwm'
iwc_tag = 'iwc'
iwl_tag = 'iwl'
iwa_tag = 'iwa'
csm_tag = 'csm'

#helper functions
#get list of features in gu
def get_gu_list():
    gu_list = []
    data = coll_gu.find()
    for row in data:
        gu_list.append(row)
    return gu_list

def insert_bsgu(repo_id, mwi, iwm, iwc, iwl, iwa, csm):
    doc = {}
    doc[repo_id_tag] = repo_id
    doc[mwi_tag] = mwi
    doc[iwm_tag] = iwm
    doc[iwc_tag] = iwc
    doc[iwl_tag] = iwl
    doc[iwa_tag] = iwa
    doc[csm_tag] = csm
    coll_bsgu.insert_one(doc)

def compare(val, limit):
    if val > limit:
        return 1
    else:
        return 0

#process csm feature
def compute_feature_vals(features):
    mean_mwi = 0
    mean_iwm = 0
    mean_iwc = 0
    mean_iwl = 0
    mean_iwa = 0
    mean_csm = 0

    for row in features:
        mean_mwi += row[mwi_tag]
        mean_iwm += row[iwm_tag]
        mean_iwc += row[iwc_tag]
        mean_iwl += row[iwl_tag]
        mean_iwa += row[iwa_tag]
        mean_csm += row[csm_tag]

    size = len(features)

    mean_mwi /= size
    mean_iwm /= size
    mean_iwc /= size
    mean_iwl /= size
    mean_iwa /= size
    mean_csm /= size

    limit_mwi = mean_mwi*1.5
    limit_iwm = mean_iwm*1.5
    limit_iwc = mean_iwc*1.5
    limit_iwl = mean_iwl*1.5
    limit_iwa = mean_iwa*1.5
    limit_csm = mean_csm*1.5

    for row in features:
        repo_id = row[repo_id_tag]
        mwi = compare(row[mwi_tag], limit_mwi)
        iwm = compare(row[iwm_tag], limit_iwm)
        iwc = compare(row[iwc_tag], limit_iwc)
        iwl = compare(row[iwl_tag], limit_iwl)
        iwa = compare(row[iwa_tag], limit_iwa)
        csm = compare(row[csm_tag], limit_csm)
        insert_bsgu(repo_id, mwi, iwm, iwc, iwl, iwa, csm)

#process features for the bad small
def process_features():
    feature_list = get_gu_list()
    compute_feature_vals(feature_list)

#main
def main():
    process_features()

if __name__ == "__main__":
    main()
