from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_students(db, skip=skip, limit=limit)

@router.get("/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@router.put("/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student
