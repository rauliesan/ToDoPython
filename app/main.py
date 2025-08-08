from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from app.models import User, Task, Base
from app.database import SessionLocal, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

## Habilita CORS en FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "API is running"}

@app.post("/create_user/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="Error, an user has this username")
        #return "Error, an user has this username"
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/log_in/")
def log_in(username: str, password: str, db: Session= Depends(get_db)):
    user = db.query(User).filter(User.username==username, User.password==password).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="Error, this password or username is incorrect")

@app.post("/create_task/")
def create_task(name: str, text: str, state: bool, user: int, db: Session= Depends(get_db)):
    task = db.query(Task).filter(Task.name==name, user==user).first()
    if task:
        raise HTTPException(status_code=400, detail="Error, there is a task with the same name")
    task = Task(name=name, text=text, state=state, id_user=user)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.post("/edit_task/")
def edit_task(id: int, name: str, text: str, state: bool, user: int, db: Session= Depends(get_db)):
    task = db.query(Task).filter(Task.id==id).first()
    if not task:
        raise HTTPException(status_code=400, detail="Error, I can't find this task")
    task.name= name
    task.text= text
    task.state= state
    db.commit()
    db.refresh(task)
    return task

@app.post("/edit_state/")
def edit_state(id: int, db: Session= Depends(get_db)):
    task = db.query(Task).filter(Task.id==id).first()
    if not task:
        raise HTTPException(status_code=400, detail="Error, I can't find this task")
    if task.state==True:
        task.state=False
    else:
        task.state=True
    db.commit()
    db.refresh(task)
    return task

@app.post("/delete_task/")
def delete_task(id: int, db: Session= Depends(get_db)):
    task = db.query(Task).filter(Task.id==id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    else:
        raise HTTPException(status_code=400, detail="Error, The task couldn't been deleted")
    
# Metodos para mostrar las tareas del usuario, una para las que está realizadas y otra para las que no (que lo único que pida es el id)

@app.get("/get_toDo_tasks/")
def get_toDo_tasks(user: int, db: Session= Depends(get_db)):
    tasks = db.query(Task).filter(Task.id_user==user, Task.state==False).all()
    return tasks

@app.get("/get_done_tasks/")
def get_done_tasks(user: int, db: Session= Depends(get_db)):
    tasks = db.query(Task).filter(Task.id_user==user, Task.state==True).all()
    return tasks