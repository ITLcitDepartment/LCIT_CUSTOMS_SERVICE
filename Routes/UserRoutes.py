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
    if AuthResponse['Result']['Status'] == 'OK':
        return HTTPException(status_code=200, detail=AuthResponse['ProfileData'])
    elif AuthResponse['Result']['Status'] == 'Unauthorized':
        raise HTTPException(status_code=404, detail="Data not found")
    else: 
        raise HTTPException(status_code=400, detail="Bad request")