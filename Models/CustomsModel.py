from typing import Any
from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class UserModel(BaseModel):
    AD_USERNAME:str = None
    AD_PASSWORD:str = None

    @staticmethod
    def fc_UserModel(obj: Any)-> "UserModel":
        _AD_USERNAME = str(obj.get("AD_USERNAME"))
        _AD_PASSWORD = str(obj.get("AD_PASSWORD"))

        return UserModel()