from datetime import datetime

from consumer.student import Student
from algo.backtracking import ActivityViewAlgo, get_max_point
from schemas.request_schemas import User, RqtActivity, RqtActivityUser
from schemas.schemas import UAStatusClass

me = Student(base_url="https://ctsv.hust.edu.vn/")
# d = {"AId":"1837","TokenCode":"B81FDBCA017219DF2BF071BECCD61996","UserName":"20194461"}
# request = RqtActivity(AId=d["AId"], TokenCode=d["TokenCode"], UserName=d["UserName"])
# request2 = RqtActivity.parse_obj(d)
# request3 = RqtActivity.parse_raw(json.dumps(d))
# ex = me.get_activity_by_id(request3)
# print(me.get_criteria_type_details(RqtCriteria.parse_raw('{"UserCode":"20194461","Semester":"2020-2","TokenCode":"B81FDBCA017219DF2BF071BECCD61996","UserName":"20194461"}')))

u = User(TokenCode="B81FDBCA017219DF2BF071BECCD61996",UserName="20194461")
test = RqtActivityUser.parse_raw('{"UserCode":"20194461","Search":"","TokenCode":"B81FDBCA017219DF2BF071BECCD61996","UserName":"20194461"}')
ua = RqtActivityUser(**u.dict(), **test.copy(exclude={"UserName", "TokenCode"}).dict())
rsp = me.get_activity_by_user(user_activity=ua)
if rsp.RespCode == 0:
    print(len(rsp.Activities))
    # me.get_activity_by_id(rsp.Activities[0].AId)
    activities_accept = [me.get_activity_by_id(RqtActivity(**a.copy(include={"AId"}).dict(),**u.dict())).Activities[0] for a in rsp.Activities if a.UAStatus == UAStatusClass.accept]
    in_time = [a for a in activities_accept if a.StartTime > datetime(2020,12,1)]
    print(activities_accept[1].StartTime, type(activities_accept[1].StartTime))
    activities_accept_algo = [ActivityViewAlgo(**activity.dict()) for activity in in_time]
    print(len(activities_accept_algo))
    print(get_max_point(activities_accept_algo))

