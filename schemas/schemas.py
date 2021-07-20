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
    CurrentPoint: Optional[int] = 0

    @abstractmethod
    def get_max_point(self):
        pass

    def get_current_point(self):
        self.re_caculate_current_point()
        return min(self.get_max_point(), self.CurrentPoint)

    def set_current_point(self, value):
        self.CurrentPoint = value
        self.re_caculate_current_point()

    @abstractmethod
    def re_caculate_current_point(self):
        pass


class Criteria(BaseModel):
    CGroupId: int
    CId: int
    CName: str
    CType: int
    CMaxPoint: int
    CStatus: int

class ActivityId(BaseModel):
    AId : int

class CriteriaView(PointCal):
    def re_caculate_current_point(self):
        pass

    CGroupId: int = None
    CId: int
    CName: str
    CMaxPoint: int
    UCPoint : Optional[int] = 10
    UserCriteriaActivityLst: List[ActivityId] = []

    def get_max_point(self):
        return max(self.CMaxPoint,0)



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
    CGMaxPoint: int  #moi sua
    UserCriteriaDetailsLst: List[CriteriaView]

    def get_max_point(self):
        return max(0,self.CGMaxPoint)

    def re_caculate_current_point(self):
        self.CurrentPoint = min(sum([cv.get_current_point() for cv in self.UserCriteriaDetailsLst]),
                                self.get_max_point())





class CriteriaType(PointCal):
    CTId: int
    CTName: str
    CTPoint: int
    CTMaxPoint: int
    CriteriaGroupDetailsLst: List[CriteriaGroup]

    def get_max_point(self):
        return max(0,self.CTMaxPoint)

    def re_caculate_current_point(self):
        self.CurrentPoint = min(sum([cg.get_current_point() for cg in self.CriteriaGroupDetailsLst]),
                                self.get_max_point())


class DRL(PointCal):
    CriteriaTypeDetailsLst: List[CriteriaType]
    MaxPoint: int = 100

    def re_caculate_current_point(self):
        self.CurrentPoint = min(sum([ct.get_current_point() for ct in self.CriteriaTypeDetailsLst]),
                                self.get_max_point())

    def get_max_point(self):
        return self.MaxPoint


