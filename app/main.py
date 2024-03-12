import uvicorn
from fastapi import FastAPI
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

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)