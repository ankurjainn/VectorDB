import chromadb
import os
from PyPDF2 import PdfReader

# Path to your PDF file
doc_path = r"f:\ArtificialIntelligence\eBook-How-to-Build-a-Career-in-AI.pdf"

# Read PDF and extract text (one document per page)
def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    documents = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            documents.append({"id": f"page_{i+1}", "text": text.strip()})
    return documents

# Initialize ChromaDB client
chroma_client = chromadb.Client()
collection_name = "pdf_collection"
collection = chroma_client.get_or_create_collection(collection_name)

# Extract documents from PDF
documents = extract_pdf_text(doc_path)

# Upsert documents into ChromaDB
for doc in documents:
    collection.upsert(ids=doc["id"], documents=[doc["text"]])

# Example query
query_text = documents[0]["text"][:100]  # Use first 100 chars of first page as query
results = collection.query(query_texts=[query_text], n_results=3)

for idx, doc_text in enumerate(results['documents'][0]):
    doc_id = results['ids'][0][idx]
    distance = results['distances'][0][idx]
    print(f"For the query: {query_text[:50]}...\n Found similar document: {doc_id} (Distance: {distance})\n")
