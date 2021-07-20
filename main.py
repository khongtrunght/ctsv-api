from datetime import datetime

from consumer.student import Student
from algo.backtracking import ActivityViewAlgo, get_max_point
from schemas.request_schemas import User, RqtActivity, RqtActivityUser, RqtMarkCriteria, RqtActivityUserCId
from schemas.schemas import UAStatusClass

TOKEN = ""
MSSV = ""

adi = {"UserCode": MSSV, "Semester": "2020-2"}

me = Student(base_url="https://ctsv.hust.edu.vn/")

u = User(TokenCode=TOKEN, UserName=MSSV)
t_string = f'{{"UserCode":"{MSSV}","Search":"","TokenCode":"{TOKEN}","UserName":"{MSSV}"}}'
test = RqtActivityUser.parse_raw(t_string)
ua = RqtActivityUser(**u.dict(), **test.copy(exclude={"UserName", "TokenCode"}).dict())
rsp = me.get_activity_by_user(user_activity=ua)
rq_CId =RqtActivityUserCId(**ua.dict())
id_all_activity = me.get_all_possible_activites(rq_CId)

activity_with_criteria_list = [me.get_activity_by_id(RqtActivity(AId= index, **u.dict())).Activities[0]
                               for index in id_all_activity]

activities_accept_algo = [ActivityViewAlgo(**activity.dict()) for activity in activity_with_criteria_list]
(max_point, drl) = get_max_point(activities_accept_algo)
mark_criteria = RqtMarkCriteria.parse_obj({**u.dict(), **drl.dict(), **adi})
mark_criteria = mark_criteria.json().encode('utf-8')
me.mark_criteria_user(mark_criteria)

print("DRL", drl.get_current_point())
for ctype in drl.CriteriaTypeDetailsLst:
    print("\tCTYPE", ctype.get_current_point())
    for cgroup in ctype.CriteriaGroupDetailsLst:
        print("\t\tCGROUP", cgroup.get_current_point())
        for criteria in cgroup.UserCriteriaDetailsLst:
            print("\t\t\tC ", criteria.get_current_point())
