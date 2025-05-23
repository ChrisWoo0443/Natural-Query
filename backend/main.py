from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import upload, query

app = FastAPI(
    title="Natural Language Data Query Tool",
    description="Upload a dataset and query it using natural language.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include your API routes
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
async def root():
    return {"message": "Natural Language Data Query Tool API is running."}
