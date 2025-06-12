from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/tags", tags=["Tags"])


app = FastAPI()


@router.get("/")
def get_students():
    return {"data": []}
