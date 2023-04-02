from fastapi import APIRouter, HTTPException

import models
from models import User

user_router = APIRouter()

user_data: User = []


@user_router.get('/')
def find_all():
    return user_data


@user_router.get("/{user_id}/")
def find_by_id(user_id: str):
    for user in user_data:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"user by id {user_id} was not found")
