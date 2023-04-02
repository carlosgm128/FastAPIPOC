from fastapi import FastAPI, HTTPException

appv1 = FastAPI()


@appv1.get('/location')
def get_location():
    return {'location': 'Republica dominicana'}
