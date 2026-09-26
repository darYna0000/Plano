from fastapi import FastAPI


app = FastAPI(title="Plano Salon AI")

@app.get("/")
def read_root():
    return {"message": "Вітаємо у Plano! Сервер працює, Слава Богу)."}

