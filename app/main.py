# Don't edit
__author__ = "Joseph Anderson"
__copyright__ = "Copyright 2022, Modern Time Team"
__license__ = "INTERNAL"
__version__ = "0.1.0"
__maintainer__ = __author__
__email__ = "devanderson0412@gmail.com"
__status__ = "alpha"

from __internal import bootstrap
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import router as api_router
from db.database import Database, Base
from mangum import Mangum

app = FastAPI(
    title="Modern Time Backend",
    description="Gambling site backend API",
    version="-".join([__version__, __status__]),
)

bootstrap(app)

database = Database()
engine = database.get_db_connection()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

handler = Mangum(app=app)