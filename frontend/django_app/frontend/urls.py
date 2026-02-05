from django.urls import path
from .views import upload_document, ask_question, generate_summary

urlpatterns = [
    path("", upload_document, name="upload"),
    path("ask/", ask_question, name="ask"),

    # ✅ NEW: Generate document summary
    path("summary/", generate_summary, name="generate_summary"),
]
