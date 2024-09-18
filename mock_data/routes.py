from datagen import event_data_test
from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def entry_point():
    return {'Status': 'OK!'}


@router.post('/addevent')
def post_event():
    return event_data_test


@router.get('/event')
def get_event():
    return post_event()
