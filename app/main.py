from fastapi import FastAPI

app = FastAPI(title="Agenda de serviços")

@app.get("/")
def saude():
    return {"status": "ok"}
