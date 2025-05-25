
# -- Esquema Marshmallow para validar células --
from marshmallow import Schema, fields, validate

class CelulaSchema(Schema):
    id = fields.Str(required=True)
    tipo = fields.Str(required=True, validate=validate.OneOf(["G","A","S","D"]))
    energia_actual = fields.Float(required=True)
    energia_maxima = fields.Float(required=True)
    organulos = fields.List(fields.Str(), required=True)
    estado = fields.Str()
    ubicacion = fields.Dict()
    nivel_evolucion = fields.Int()
    enlaces = fields.List(fields.Str())
    generada_por = fields.Str(allow_none=True)
    puede_multiplicar = fields.Bool()
    posibles_evoluciones = fields.List(fields.Str())
