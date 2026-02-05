from app.core.retriever import retrieve_relevant_chunks

results = retrieve_relevant_chunks(
    "What is the goal of this project?"
)

for r in results:
    print(r["metadata"])
