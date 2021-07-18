from uplink import Consumer, Body, post

from schemas import *


class Student(Consumer):
    @post("api-t/Activity/GetActivityById")
    def get_activity_by_id(self, user: Body(type=RqtActivity)) -> RspActivityView :
        """Get detail info for an activity by id"""

    @post("api-t/Activity/GetActivityByCId")
    def get_activity_by_cid(self, user: Body()):
        pass

    @post("api-t/Point/MarkCriteriaUser")
    def choqua(self):
        pass

    @post("api-t/Criteria/GetCriteriaTypeDetails")
    def get_criteria_type_details(self, user : Body(type=RqtCriteria)) -> RspCriteriaTypeDetails :
        pass

    @post("api-t/Activity/GetActivityByUser")
    def get_activity_by_user(self, user_activity : Body(type=RqtActivityUser)) -> RspActivityView:
        pass