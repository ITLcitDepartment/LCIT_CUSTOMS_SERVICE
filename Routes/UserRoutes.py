from fastapi import APIRouter, HTTPException
from Models.CustomsModel import UserModel
from Controllers.UserController import UserController
router = APIRouter(
    prefix="/User",
    tags=["USER-Routes"]
)

@router.post("/AuthUser")
def AuthUser(USER_DATA: UserModel):
    AuthResponse = UserController.login(USER_DATA)
    return AuthResponse
    if AuthResponse['status'] == 200:
        return AuthResponse['data']
    elif AuthResponse['status'] == 404:
        raise HTTPException(status_code=404, detail="Data not found")
    elif AuthResponse['status'] == 500:
        raise HTTPException(status_code=500, detail=AuthResponse['message'])
    else: 
        raise HTTPException(status_code=400, detail="Bad request")