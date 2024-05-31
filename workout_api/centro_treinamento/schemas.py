from workout_api.contrib.schemas import BaseSchemas
from pydantic import Field




class CentroTreinamento (BaseSchemas):
   nome: str = Field(description='Nome do Centro de treinamento ', examples='CT King', max_length=20)
   endereco: str = Field(description='Endero do CT ', examples='Bairro e Rua', max_length=30)
   propietario: str = Field(description='Nome do propietario', examples='Marcos', max_length=30)