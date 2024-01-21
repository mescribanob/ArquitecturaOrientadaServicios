from pydantic import BaseModel

class Equivalencias(BaseModel):
    nombre: str
    fabricante: str
    modelo: str

class Link(BaseModel):
    href: str
    rel: str

class Links(BaseModel):
    parent: Link
    self: Link

class Recambio(BaseModel):
    numero_serie: str
    nombre: str
    descripcion: str
    proveedor: str
    equivalencias: Equivalencias
    garantia: str
    precio: str
    iva: str
    importe: str
    cantidad: str
    links: Links