from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=True)
    peso: Mapped[float] = mapped_column(Float, nullable=True)
    altura: Mapped[float] = mapped_column(Float, nullable=True)
    sexo: Mapped[str] = mapped_column(String(1), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.date, nullable=False)
    categoria: Mapped ['CategoriaModel'] = relationship(back_populates = 'atletas')
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped ['CentroTreinamentoModel'] = relationship(back_populates = 'atletas')
    centro_treinamento_id = Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))