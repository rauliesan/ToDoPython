from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Table, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

# Tabla de usuarios
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="user") # Relación entre el usuario y la tarea por ejemplo para acceder a todas las tareas de un usuario usuario.tasks_user

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False) # Nombre de la tarea
    id_user = Column(Integer, ForeignKey(User.id), nullable=False)
    text = Column(String, nullable=False) # Texto informativo sobre de que trata la tarea
    state = Column(Boolean, nullable=False) # El estado de la tarea (false) por defecto porque cuando se crea no está realizada
    # Añadir como actualización la fecha de creación

    user = relationship("User", back_populates="tasks")