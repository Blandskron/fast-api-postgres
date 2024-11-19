from sqlalchemy.orm import Session
from app import models, schemas

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = get_student_by_id(db, student_id)
    if not db_student:
        return None
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student_by_id(db, student_id)
    if not db_student:
        return None
    db.delete(db_student)
    db.commit()
    return db_student
