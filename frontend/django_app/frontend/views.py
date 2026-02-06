import requests
from django.shortcuts import render

FASTAPI_BASE_URL = "https://YOUR-BACKEND.up.railway.app/api"


def upload_document(request):
    """
    Upload document to FastAPI backend
    """
    if request.method == "POST" and request.FILES.get("document"):
        file = request.FILES["document"]

        try:
            response = requests.post(
                f"{FASTAPI_BASE_URL}/upload",
                files={"file": file},
                timeout=60
            )

            if response.headers.get("Content-Type", "").startswith("application/json"):
                upload_response = response.json()
            else:
                upload_response = {
                    "error": "Backend did not return JSON",
                    "status_code": response.status_code
                }

        except Exception as e:
            upload_response = {"error": str(e)}

        return render(
            request,
            "chat.html",
            {"upload_response": upload_response}
        )

    return render(request, "chat.html")


def ask_question(request):
    """
    Send question to FastAPI QA endpoint
    """
    if request.method == "POST":
        question = request.POST.get("question")

        try:
            response = requests.post(
                f"{FASTAPI_BASE_URL}/qa",
                json={"question": question},
                timeout=60
            )

            if response.headers.get("Content-Type", "").startswith("application/json"):
                answer = response.json()
            else:
                answer = {"answer": "Backend error", "references": []}

        except Exception as e:
            answer = {"answer": f"Error: {str(e)}", "references": []}

        return render(
            request,
            "chat.html",
            {"answer": answer}
        )

    return render(request, "chat.html")


def generate_summary(request):
    """
    Generate summary and force-render it in UI
    """
    summary = "Summary could not be generated."

    try:
        response = requests.post(
            f"{FASTAPI_BASE_URL}/summary",
            timeout=180
        )

        print("FASTAPI SUMMARY RESPONSE:", response.text)  # 🔍 DEBUG

        if response.status_code == 200:
            data = response.json()
            summary = data.get("summary", summary)

    except Exception as e:
        summary = f"Error: {str(e)}"

    # 🔥 FORCE render summary
    return render(
        request,
        "chat.html",
        {
            "summary": summary
        }
    )
