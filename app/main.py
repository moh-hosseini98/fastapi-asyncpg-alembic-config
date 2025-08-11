from fastapi import FastAPI

app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version='v1',
)


@app.get("/")
async def root():
    return "hello updated!!"