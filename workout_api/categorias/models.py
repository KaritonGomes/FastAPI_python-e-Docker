from workout_api.atleta.models import AtletaModel
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime


class CategoriaModel(BaseModel):
    __tablename__ = 'Categoria'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column (String(50), unique=True, nullable=False)
    atleta: Mapped ['AtletaModel'] = relationship(back_populates = 'Categoria')
 
    