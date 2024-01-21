from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from models.recambio import Recambio

api_recambios = FastAPI()
mongo_client = MongoClient("mongodb://root:root@recambios-db:27017/")
taller = mongo_client["taller"]

# CORSMiddleware para método OPTIONS

origins = [
    "127.0.0.1:4000"
]

api_recambios.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS", "PUT", "DELETE"],
    allow_headers=["*"],
    max_age=3600,
)

@api_recambios.get("/api/v1/recambios")
async def lista_recambios(page: int = 0):
    recambios_cur = taller["recambios"].find({}, {"_id": 0}).skip(page).limit(10)
    recambios = {
        "recambios": [recambio for recambio in recambios_cur],
        "links": {
            "nextPage": { "href": "http://127.0.0.1:4000/api/v1/recambios?page=1", "rel": "nextPage" }
        } if page == 0 else \
        {
            "prevPage": { "href": f"http://127.0.0.1:4000/api/v1/recambios?page={page-1}", "rel": "prevPage" },
            "nextPage": { "href": f"http://127.0.0.1:4000/api/v1/recambios?page={page+1}", "rel": "nextPage" }
        }
    }
    return recambios

@api_recambios.get('/api/v1/recambios/{numero_serie}')
async def obtener_recambio(numero_serie: str):
    recambio = taller["recambios"].find_one({"numero_serie": numero_serie}, {"_id": 0})
    if not recambio:
        raise HTTPException(status_code=404, detail="No se encuentra el recambio")
    recambioOut = {"recambios": recambio}
    return recambioOut

@api_recambios.delete('/api/v1/recambios/{numero_serie}')
async def borrar_recambio(numero_serie: str):
    deleted = taller["recambios"].delete_one({"numero_serie": numero_serie}).deleted_count
    if deleted:
        return {"message": "Recambio eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Recambio no encontrado")

@api_recambios.post('/api/v1/recambios')
async def crear_recambio(recambio: Recambio):
    try:
        taller["recambios"].insert_one(recambio.dict())
        return {"message": "Recambio añadido correctamente"}
    except:
        raise HTTPException(status_code=400, detail="No se pudo añadir el recambio")

@api_recambios.put('/api/v1/recambios/{numero_serie}')
async def actualizar_recambio(numero_serie: str, recambio: Recambio):
    if numero_serie != recambio.numero_serie:
        raise HTTPException(status_code=400, detail="El número de serie no coincide")
    
    found_recambio = taller["recambios"].find_one({"numero_serie": numero_serie}, {"_id": 0})
    if not found_recambio:
        raise HTTPException(status_code=404, detail="No se encuentra el recambio")

    try:
        taller["recambios"].update_one({"numero_serie": numero_serie}, {"$set": recambio.dict()})
        return {"message": "Recambio actualizado correctamente"}    
    except:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el recambio")