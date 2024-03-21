import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def init_db(app: FastAPI):
    
    from databases.conn import db_conn
    from models.item import Base as item_base
    from models.user import Base as user_base

    db_conn.initialize(app=app)

    item_base.metadata.create_all(bind=db_conn.engine)
    user_base.metadata.create_all(bind=db_conn.engine)


def create_app():

    app = FastAPI(debug=True)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )   
    
    init_db(app=app)

    return app


app = create_app()


@app.get("/")
async def index():
    return {"hello": "world"}

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)