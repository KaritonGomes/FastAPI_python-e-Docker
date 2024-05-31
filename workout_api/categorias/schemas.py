from workout_api.contrib.schemas import BaseSchemas
from pydantic import Field




class Categoria (BaseSchemas):
   nome: str = Field(description='Nome da categoria', example='Scale', max_length=10)