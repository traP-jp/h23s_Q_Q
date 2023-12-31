import pprint
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from q_q.routers import deps
from q_q import schemas
from q_q.services import stamp


router = APIRouter()


@router.get("/", response_model=List[schemas.TraQStamp])
async def read_stamps(
    db: Session = Depends(deps.get_db),
):
    try:
        data = stamp.get_stamps()
        return [
            schemas.TraQStamp(
                id=stamp["id"],
                name=stamp["name"],
                fileId=stamp["file_id"],
                isUnicode=stamp["is_unicode"],
            )
            for stamp in data
        ]
    except Exception as e:
        pprint(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/{stamp_id}", response_model=schemas.TraQStamp)
async def read_stamp(
    stamp_id: str,
    db: Session = Depends(deps.get_db),
):
    try:
        data = stamp.get_stamp(stamp_id)
        print(data)
        return schemas.TraQStamp(
            id=data["id"],
            name=data["name"],
            fileId=data["file_id"],
            isUnicode=data["is_unicode"],
        )
    except Exception as e:
        pprint(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
