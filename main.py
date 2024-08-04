from fastapi import FastAPI
from pydantic import BaseModel

#إنشاء تطبيق FastApi
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],#قم بقييد هذا في الإنتاج يسمح بالوصول من أي مصدر
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

#تعريف نموذج البيانات بإستخدام Pydantic
class Student(BaseModel):
    id: int
    name: str
    grade:int

#قائمة لتخزين البيانات في الذاكرة
students = [
    Student(id=1,name="baha khaled",grade=10),
    Student(id=2 ,name="bouali youcef" ,grade=7),
    Student(id=3 ,name="mebtouche leyace" ,grade=7),
    Student(id=4 ,name="hamza omar" ,grade=8),
    Student(id=5,name="hicham silami",grade=10),
]

#قراءة العناصر
@app.get("/students/")
def read_students():
    return students

#إنشاء عنصر جديد
@app.post("/students/")
def create_student(New_Student:Student):
    students.append(New_Student)
    return New_Student

#تحديث عنصر معين بناء على معرفة (ID) بإستخدام PUT method
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

#حذف خنصر معين بناء على معرفة (ID) بإستخدام DELETE method
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "student deleted"}
    return {"error": "Student not found"}

