from schemas import *
from student import Student
from pprint import  pprint as pp
import json

me = Student(base_url="https://ctsv.hust.edu.vn/")
# d = {"AId":"1837","TokenCode":"B81FDBCA017219DF2BF071BECCD61996","UserName":"20194461"}
# request = RqtActivity(AId=d["AId"], TokenCode=d["TokenCode"], UserName=d["UserName"])
# request2 = RqtActivity.parse_obj(d)
# request3 = RqtActivity.parse_raw(json.dumps(d))
# ex = me.get_activity_by_id(request3)
# print(me.get_criteria_type_details(RqtCriteria.parse_raw('{"UserCode":"20194461","Semester":"2020-2","TokenCode":"B81FDBCA017219DF2BF071BECCD61996","UserName":"20194461"}')))

u = User(TokenCode="B81FDBCA017219DF2BF071BECCD61996",UserName="20194461")
test = RqtActivityUser.parse_raw('{"UserCode":"20194461","Search":"","NumberRow":12,"PageNumber":1,"TokenCode":"B81FDBCA017219DF2BF071BECCD61996","UserName":"20194461"}')
pp(me.get_activity_by_user(user_activity=RqtActivityUser(**u.dict(), **test.copy(exclude={"UserName", "TokenCode"}).dict())))