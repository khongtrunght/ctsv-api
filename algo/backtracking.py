import json
import logging
from typing import List, Optional

from pydantic import BaseModel, parse_obj_as
from models.drl_graph import drl
from schemas.request_schemas import RqtMarkCriteria, User
from schemas.schemas import ActivityView, CriteriaView

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.INFO)


class ActivityViewAlgo(ActivityView):
    currentCriteria: Optional[CriteriaView]

    def get_length_clist(self):
        return len(self.CriteriaLst)

    def set_criteria(self, index):
        assert index < self.get_length_clist()
        self.currentCriteria = self.CriteriaLst[index]
        self.currentCriteria.set_current_point(self.currentCriteria.get_max_point())

    def reset_criteria(self, index, value):
        assert index < self.get_length_clist()
        self.currentCriteria.set_current_point(value)


class OutputActivitiesLst(BaseModel):
    __root__: List[ActivityViewAlgo]


def get_max_point(a_list: List[ActivityViewAlgo], drl=drl):
    global max_point
    max_point = 0

    def construct_graph(a_list, drl):
        ki_trc = []
        criteria_dict = {}
        for ctype in drl.CriteriaTypeDetailsLst:
            for cgroup in ctype.CriteriaGroupDetailsLst:
                for criteria in cgroup.UserCriteriaDetailsLst:
                    criteria_dict[criteria.CId] = criteria

        for activity in a_list:
            new_list = list()
            for criteria in activity.CriteriaLst:
                # Check hoat dong ki nay
                if criteria.CId in criteria_dict.keys():
                    new_list.append(criteria_dict[criteria.CId])
                else:
                    ki_trc.append(activity)
                    logging.info(f'Found ki trc : {activity}')
            activity.CriteriaLst = new_list

        a_list = [a for a in a_list if a not in ki_trc]
        return a_list, drl

    def back_track(a_list=a_list, index=0, drl=drl):
        global max_point, best_list, s, drl_copy
        if index == len(a_list):
            max_curr = drl.get_current_point()
            if max_curr > max_point:
                max_point = max_curr
                s = OutputActivitiesLst(__root__=a_list)
                drl_copy = drl.copy(deep=True)
        else:
            for number in range(a_list[index].get_length_clist()):
                tmp = a_list[index].CriteriaLst[number]
                crr_cpoint = tmp.get_current_point()
                if tmp.get_current_point() < tmp.get_max_point():
                    a_list[index].set_criteria(number)
                elif (number + 1 == a_list[index].get_length_clist()):
                    a_list[index].set_criteria(number)
                else:
                    continue
                back_track(a_list, index + 1)
                a_list[index].reset_criteria(number, crr_cpoint)

    a_list, drl = construct_graph(a_list, drl)
    a_list.sort(key=lambda a: a.get_length_clist())
    back_track(a_list, drl=drl)

    criteria_activity = {}
    for activity in s.__root__:
        if activity.currentCriteria.CId not in criteria_activity.keys():
            criteria_activity[activity.currentCriteria.CId] = [activity.copy(include={"AId"}), ]
        else:
            criteria_activity[activity.currentCriteria.CId].append(activity.copy(include={"AId"}))

    drl = drl_copy
    for ctype in drl.CriteriaTypeDetailsLst:
        for cgroup in ctype.CriteriaGroupDetailsLst:
            for criteria in cgroup.UserCriteriaDetailsLst:
                if criteria.CId in criteria_activity.keys():
                    criteria.UserCriteriaActivityLst = criteria_activity[criteria.CId]

    return max_point, drl
