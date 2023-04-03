import httpx
from fastapi import APIRouter
from pydantic import BaseModel

todo_router = APIRouter()


class TodoSchema(BaseModel):
    userId: str
    id: str
    title: str
    completed: bool = False


todo_list: list[TodoSchema] = []


@todo_router.get("/")
async def find_all():
    if len(todo_list) == 0:
        async with httpx.AsyncClient() as client:
            resp = await client.get("https://jsonplaceholder.typicode.com/todos")
            resp.raise_for_status()
            data = resp.json()

        print(data)
        todo_list.extend(data)
    return todo_list


@todo_router.get('/{todo_id}')
async def find_by_id(todo_id):
    did_fetch = False
    print(todo_list)
    if not next((item for item in todo_list if item["id"] == int(todo_id)), None):
        async with httpx.AsyncClient() as client:
            did_fetch = True
            resp = await client.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
            resp.raise_for_status()
            data = resp.json()
        print(f"value not found locally and fetch to third party api to get data \n {data}")
        if did_fetch:
            todo_list.append(data)
            return data
    print('we have the value locally')
    return next((item for item in todo_list if item["id"] == int(todo_id)), None)
