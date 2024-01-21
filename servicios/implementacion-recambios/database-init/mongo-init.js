db.recambios.drop();
db.recambios.createIndex({ "numero_serie": 1 }, { unique: true }),
db.recambios.insertOne(
    { 
        "numero_serie": "Z0000001-A", 
        "nombre": "Kit Frenos Brembo" , 
        "descripcion": "Los kits Brembo GT | M están compuestos por discos compuestos y perforados; \
        pinzas de aluminio de 6 pistones;  un set completo de pastillas de altas prestaciones; tubos con trenzado metálico y tornillería de gran calidad." , 
        "proveedor": "Brembo", 
        "equivalencias": {"nombre": "Kit Frenos EBC", "fabricante": "EBC Brakes", "modelo": "Golf GTI MK7" } , 
        "garantia": "3 meses", 
        "precio": "448.32", 
        "iva": "21%",
        "importe": "587.50", 
        "cantidad": "10",
        "links": {
            "parent": { "href": "http://127.0.0.1:4000/api/v1/recambios", "rel": "recambio_post recambio_cget"},
            "self": { "href": "http://127.0.0.1:4000/api/v1/recambios/Z0000001-A", "rel": "recambio_get recambio_delete recambio_put" }
        }
    }
)
db.recambios.insertOne(
    { 
        "numero_serie": "Z0000003-B", 
        "nombre": "Neumático pilot sport 4 205/55ZR16" , 
        "descripcion": "El neumático de verano MICHELIN Pilot Sport 4 se adapta a la carretera gracias a su excelente reactividad y precisión de conducción y a su excelente duración" , 
        "proveedor": "Michelin", 
        "equivalencias": {"nombre": "Neumático Potenza S001 205/55", "fabricante": "Bridgestone", "modelo": "Vehículos con dimensiones en las ruedas de 205/55" } , 
        "garantia": "No ofrece", 
        "precio": "197.5", 
        "iva": "21%", 
        "importe": "250.00", 
        "cantidad": "20",
        "links": {
            "parent": { "href": "http://127.0.0.1:4000/api/v1/recambios", "rel": "recambio_post recambio_cget"},
            "self": { "href": "http://127.0.0.1:4000/api/v1/recambios/Z0000003-B", "rel": "recambio_get recambio_delete recambio_put" }
        }
    }
)