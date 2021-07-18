from pydantic import BaseModel


class User(BaseModel):
    TokenCode : str
    UserName : str


class RqtActivity(User):
    AId : str


class RqtCriteria(User):
    UserCode : str
    Semester : str


class RqtActivityUser(User):
    UserCode : str
    Search : str = ""
    PageNumber : int = 1
    NumberRow : int = 100