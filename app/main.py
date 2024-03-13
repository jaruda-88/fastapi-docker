import uvicorn
from fastapi import FastAPI
from databases.conn import db_conn
from models.item import Base
# from models.user import Base as base_user
# from models.item import Base as base_item
from starlette.middleware.cors import CORSMiddleware


def create_app():

    app = FastAPI(debug=True)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )   
    # base_user.metadata.create_all(bind=db_conn.engine)
    # base_item.metadata.create_all(bind=db_conn.engine)

    db_conn.initialize(app=app)
    Base.metadata.create_all(bind=db_conn.engine)


    return app


app = create_app()


@app.get("/")
async def index():
    return {"hello": "world"}

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)