from fastapi import FastAPI
from backend.app.api import auth, notes, checklists, common
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://43.204.38.250"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(notes.router)
app.include_router(checklists.router)
app.include_router(common.router)
