from fastapi import FastAPI
#Crear instancia de FastAPI
app = FastAPI()
#Este decorador convierte la función en un endpoint
@app.get("/")
def saludo():
    return "hola"

#Este endpoint requiere un parametro llamado "nombre" para retornarlo en la respuesta 
@app.get("/lucario/{nombre}")
def saludo(nombre):
    print("Este es mi pokemon")
    return f"Mi pokemon es lucario y mi nombre es {nombre}"

#Para ejecutar una aplicación toca hacer "fastapi dev main.py"