from datetime import datetime

from consumer.student import Student
from algo.backtracking import ActivityViewAlgo, get_max_point
from schemas.request_schemas import User, RqtActivity, RqtActivityUser, RqtMarkCriteria
from schemas.schemas import UAStatusClass

TOKEN = ""
MSSV = ""

adi = {"UserCode": MSSV, "Semester": "2020-2"}

me = Student(base_url="https://ctsv.hust.edu.vn/")

u = User(TokenCode=TOKEN, UserName="20194461")
t_string = f'{{"UserCode":"{MSSV}","Search":"","TokenCode":"{TOKEN}","UserName":"{MSSV}"}}'
test = RqtActivityUser.parse_raw(t_string)
ua = RqtActivityUser(**u.dict(), **test.copy(exclude={"UserName", "TokenCode"}).dict())
rsp = me.get_activity_by_user(user_activity=ua)
if rsp.RespCode == 0:
    activities_accept = [me.get_activity_by_id(RqtActivity(**a.copy(include={"AId"}).dict(), **u.dict())).Activities[0]
                         for a in rsp.Activities if a.UAStatus == UAStatusClass.accept]
    in_time = [a for a in activities_accept if a.StartTime > datetime(2020, 12, 31)]
    activities_accept_algo = [ActivityViewAlgo(**activity.dict()) for activity in in_time]
    (max_point, drl) = get_max_point(activities_accept_algo)
    mark_criteria = RqtMarkCriteria.parse_obj({**u.dict(), **drl.dict(), **adi})
    mark_criteria = mark_criteria.json().encode('utf-8')
    me.mark_criteria_user(mark_criteria)

    print("DRL",drl.get_current_point())
    for ctype in drl.CriteriaTypeDetailsLst:
        print("\tCTYPE", ctype.get_current_point())
        for cgroup in ctype.CriteriaGroupDetailsLst:
            print("\t\tCGROUP", cgroup.get_current_point())
            for criteria in cgroup.UserCriteriaDetailsLst:
                print("\t\t\tC ", criteria.get_current_point())


