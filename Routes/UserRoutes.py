from fastapi import APIRouter, HTTPException
from Models.CustomsModel import UserModel
from Controllers.UserController import UserController
router = APIRouter(
    prefix="/User",
    tags=["USER-Routes"]
)

@router.post("/AuthUserAD")
def AuthUser(USER_DATA: UserModel):
    AuthResponse = UserController.login(USER_DATA)
    if AuthResponse['Result']['Status'] == 'OK':
        return HTTPException(status_code=200, detail=AuthResponse['ProfileData'])
    elif AuthResponse['Result']['Status'] == 'Unauthorized':
        raise HTTPException(status_code=404, detail="Data not found")
    else: 
        raise HTTPException(status_code=400, detail="Bad request")
    
@router.post("/FetchCustomsUser")
def AuthUser(USER_DATA: UserModel):
    FetchResponse = UserController.FetchCustomsUser(USER_DATA)
    if FetchResponse['status'] == 200:
        return FetchResponse['data']
    elif FetchResponse['status'] == 404:
        raise HTTPException(status_code=404, detail="Data not found")
    elif FetchResponse['status'] == 500:
        raise HTTPException(status_code=500, detail=FetchResponse['message'])
    else: 
        raise HTTPException(status_code=400, detail="Bad request")   