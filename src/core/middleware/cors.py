from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    # CORS settings
    origins = [
        "http://localhost",
        # "http://localhost:3000",
        # "http://localhost:8000",
        # Add more allowed origins as needed
    ]

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
