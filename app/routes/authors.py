from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/author", tags=["Authors"])


app = FastAPI()


@router.get("/")
def get_students():
    return {"data": []}
