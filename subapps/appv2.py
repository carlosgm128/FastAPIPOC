from fastapi import FastAPI

appv2 = FastAPI()


@appv2.get('/location')
def get_location():
    return {'location': 'united states'}
