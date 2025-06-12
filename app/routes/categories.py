from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/categories", tags=["Categories"])


app = FastAPI()


@router.get("/")
def get_students():
    return {"data": []}
