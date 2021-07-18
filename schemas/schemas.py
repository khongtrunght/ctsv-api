from abc import abstractmethod
from datetime import datetime
from typing import List, Optional
from enum import Enum

from pydantic import BaseModel




class UAStatusClass(int, Enum):
    reject = 0
    pending = 1
    accept = 2


class PointCal(BaseModel):
    CurrentPoint: Optional[float] = 0.0

    @abstractmethod
    def get_max_point(self):
        pass

    def get_current_point(self):
        return min(self.get_max_point(), self.CurrentPoint)

    def set_current_point(self, value):
        self.CurrentPoint = value


class Criteria(BaseModel):
    CGroupId: int
    CId: int
    CName: str
    CType: int
    CMaxPoint: float
    CStatus: int


class CriteriaView(PointCal):
    CGroupId: int = None
    CId: int
    CName: str
    CMaxPoint: float

    def get_max_point(self):
        return self.CMaxPoint




class Activity(BaseModel):
    AID: int
    ACode: str
    AName: str
    AType: str
    ADesc: str
    StartTime: datetime
    FinishTime: datetime
    APlace: str
    GId: int
    GName: str
    AGId: int
    Data: str
    CreateDate: datetime
    CreateUser: str
    AStatus: int
    UAStatus: UAStatusClass
    ARefId: str
    ACriteriaLst: str
    AGDesc: str
    UserRole: int
    Publish: int
    Avatar: str
    Deadline: datetime
    CriteriaLst: List[Criteria]
    Signature: str


class ActivityView(BaseModel):
    AId: int
    AName: str
    StartTime: datetime
    FinishTime: datetime
    CriteriaLst: List[CriteriaView] = None
    UAStatus: UAStatusClass



class CriteriaGroup(PointCal):
    CGId: int
    CGName: str
    CGMaxPoint: float
    UserCriteriaDetailsLst: List[CriteriaView]

    def get_max_point(self):
        return self.CGMaxPoint


class CriteriaType(PointCal):
    CTId: int
    CTName: str
    CTPoint: float
    CTMaxPoint: float
    CriteriaGroupDetailsLst: List[CriteriaGroup]

    def get_max_point(self):
        return self.CTMaxPoint


class DRL(PointCal):
    MaxPoint: float = 100
