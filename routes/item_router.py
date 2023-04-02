from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
item_router = APIRouter()

items_list = ['gorra', 'perro', 'gato']


@item_router.get('/')
def find_all():
    return items_list


@item_router.get('/{item_id}')
def find_by_id(item_id: str):
    if item_id not in items_list:
        raise HTTPException(status_code=404, detail=f'item with id: {item_id} is not found')
    return {'item': items_list[items_list.index(item_id)]}


@item_router.post('/')
def save_item(new_item: str):
    if new_item in items_list:
        raise HTTPException(status_code=400, detail=f'item {new_item} is already registered')
    items_list.append(new_item)
    return Response(content=new_item, status_code=201, media_type='application/text')


@item_router.patch('/{item_old_name}')
def update_item(item_new_name: str, item_old_name):
    if item_old_name not in items_list:
        raise HTTPException(status_code=400, detail=f'item {item_old_name} is not registered')
    if item_new_name == item_old_name:
        raise HTTPException(status_code=304, detail=f'item {item_old_name} has not suffer any change')
    items_list[items_list.index(item_old_name)] = item_new_name
    return Response(content=item_new_name, media_type='application/text', status_code=200)

