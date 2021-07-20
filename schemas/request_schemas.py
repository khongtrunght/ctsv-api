from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from schemas.schemas import CriteriaGroup, CriteriaType, DRL


class User(BaseModel):
    TokenCode: str
    UserName: str


class RqtActivity(User):
    AId: str


class RqtCriteria(User):
    UserCode: str
    Semester: str


class RqtActivityUser(User):
    UserCode: str
    Search: str = ""
    PageNumber: int = 1
    NumberRow: int = 100

class RqtActivityUserCId(RqtActivityUser):
    CId : Optional[int]



class RqtMarkCriteria(User, DRL):
    UserCode: str
    Semester: str
    # CriteriaTypeDetailsLst: List[CriteriaType]
