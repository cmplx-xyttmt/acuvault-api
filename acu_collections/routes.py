from fastapi import APIRouter

collections = []

router = APIRouter()


@router.post("/create")
async def create_collection(collection_name: str):
    collections.append(collection_name)
    return collection_name


@router.get("/list")
async def list_collections():
    return collections


@router.get("/{collection_id}")
async def get_collection(collection_id: int):
    return collections[collection_id]


@router.patch("/update/{collection_id}")
async def update_collection(collection_id: int, new_name: str):
    collections[collection_id] = new_name
    return collections[collection_id]

