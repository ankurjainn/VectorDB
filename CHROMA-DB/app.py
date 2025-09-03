import chromadb
chroma_client = chromadb.Client()

collection_name = "test_collection"

collection = chroma_client.get_or_create_collection(collection_name)


# Define text docs
documents = [
    {"id": "doc1", "text":"Hello, World!"},
    {"id": "doc2", "text":"How are you today?"},
    {"id": "doc3", "text":"Goodbye, See you later!"}
]

for doc in documents:
    collection.upsert(ids = doc["id"], documents= [doc["text"]])

# define a query text
query_text = "Hello, World!"


results = collection.query(query_texts=[query_text], 
                           n_results=3)

# print(results)
for idx, documents in enumerate(results['documents'][0]):
    doc_id = results['ids'][0][idx]
    distance = results['distances'][0][idx]
    print(
        f"For the query: {query_text}, \n Found similar documents: {documents} (ID: {doc_id}, Distnace: {distance})"
    )




