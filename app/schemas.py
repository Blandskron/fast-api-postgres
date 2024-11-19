from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    course: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
