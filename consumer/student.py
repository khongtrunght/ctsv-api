from uplink import Consumer, Body, post, headers

from schemas.request_schemas import *
from schemas.response_schemas import RspCriteriaTypeDetails, RspActivityView


class Student(Consumer):
    @post("api-t/Activity/GetActivityById")
    def get_activity_by_id(self, user: Body(type=RqtActivity)) -> RspActivityView:
        """Get detail info for an activity by id"""

    @post("api-t/Activity/GetActivityByCId")
    def get_activity_by_cid(self, user: Body()):
        pass

    @headers({
        "Content-Type": "application/json; charset=UTF-8",
        # "Accept-Language": "vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5"
    })
    @post("api-t/Point/MarkCriteriaUser")
    def mark_criteria_user(self, mark_criteria: Body()):
        pass

    @post("api-t/Criteria/GetCriteriaTypeDetails")
    def get_criteria_type_details(self, user: Body(type=RqtCriteria)) -> RspCriteriaTypeDetails:
        pass

    @post("api-t/Activity/GetActivityByUser")
    def get_activity_by_user(self, user_activity: Body(type=RqtActivityUser)) -> RspActivityView:
        pass
