from algo.backtracking import Backtracking, PrintExportor
from consumer.cham_drl import NonBearerInfoGet
from schemas.request_schemas import RqtCriteria
from schemas.schemas import DRL

TOKEN = ""
MSSV = ""

user = RqtCriteria(TokenCode=input("Token :"), UserName= input("UserCode: "), Semester='2020-2')
cham = NonBearerInfoGet(user)

drl = DRL.parse_file('resources/drl.json')
a_list = cham.get_list_of_activities(drl.get_CId_lst())
algorithm = Backtracking(drl, a_list)
algorithm.optimize()
cham.mark_criteria(algorithm.get_drl_optimal())

printExportor = PrintExportor()
printExportor.store(algorithm.get_drl_optimal())
printExportor.print()
