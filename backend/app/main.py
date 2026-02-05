from fastapi import FastAPI
from app.config import settings

# ----------------------
# App initialization
# ----------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# ----------------------
# Health & root routes
# ----------------------
@app.get("/")
def root():
    return {
        "message": "Smart Assistant for Research Summarization is running 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }

# ----------------------
# API Routers
# ----------------------
from app.api.upload import router as upload_router
from app.api.qa import router as qa_router
from app.api.logic import router as logic_router

# ✅ NEW: summary router
from app.api.summary import router as summary_router

# ----------------------
# Register routers
# ----------------------
app.include_router(upload_router, prefix="/api")
app.include_router(qa_router, prefix="/api")
app.include_router(logic_router, prefix="/api")
app.include_router(summary_router, prefix="/api")  # ✅ added
