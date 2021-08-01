from fastapi import FastAPI 
from config import settings 
from pages.homepage import router 
def include_router(app):
    app.include_router(router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION)
    include_router(app)

    return app 

app = start_application()




