from datagen import generate_event
from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def entry_point():
    return {'Status': 'OK!'}


@router.post('/addevent')
def post_event():
    return generate_event()


@router.get('/event')
def get_event():
    return post_event()
