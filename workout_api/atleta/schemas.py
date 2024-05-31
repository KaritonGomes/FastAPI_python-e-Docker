from typing import Literal
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchemas

class Atleta(BaseSchemas):
    nome: str = Field(description='Nome do atleta', examples='Joao', max_length=50)
    cpf: str = Field(description='CPF do atleta', examples='1234567900', max_length=11, min_length=11)
    idade: int = Field(description='Idade do atleta', examples=25)
    peso: PositiveFloat = Field(description='Peso do atleta', examples=75.5)
    altura: PositiveFloat = Field(description='Altura do atleta', examples=1.75)
    sexo: Literal['M', 'F'] = Field(description='Genero do atleta', examples='M')
