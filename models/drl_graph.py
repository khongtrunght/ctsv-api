from schemas.schemas import DRL

drl = DRL.parse_file('resources/drl.json')
cid_list = []
for ctype in drl.CriteriaTypeDetailsLst:
    for cgroup in ctype.CriteriaGroupDetailsLst:
        for criteria in cgroup.UserCriteriaDetailsLst:
            cid_list.append(criteria.CId)
