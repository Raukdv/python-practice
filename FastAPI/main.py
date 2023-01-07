from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
async def root():
    return "Hola Raul, desde FastAPI con cariño!"

@app.get("/url")
async def url():
    return { "url":"https://github.com/Raukdv" }