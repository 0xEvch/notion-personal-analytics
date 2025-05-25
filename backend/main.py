from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.api.activities import router as activities

app = FastAPI(
    title="Analytics API",
    description="API for analyzing activity data",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URl
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(activities)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)