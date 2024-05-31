from workout_api.atleta.models import AtletaModel
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamentos'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60),unique=True, nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped ['AtletaModel'] = relationship(back_populates = 'Categoria')
 
    