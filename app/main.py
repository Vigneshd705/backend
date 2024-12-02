from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import chat_router  # Import the chatbot router

app = FastAPI()

# Include the chat router with your API endpoints
app.include_router(chat_router)

# Add CORS middleware to handle frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:19006", "http://localhost:8081"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
