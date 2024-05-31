from pydantic import BaseModel




class BaseSchemas (BaseModel):
    class Condif:
        extra = 'forbid'
        from_atributes = True