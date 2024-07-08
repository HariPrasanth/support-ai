from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['wiki_db']
collection = db['documents']


# Function to search documents
def search_documents(query, model, top_k=5):
    # Encode the query
    query_embedding = model.encode([query])

    # Fetch embeddings from MongoDB
    embeddings = np.array([doc['embedding'] for doc in collection.find()])
    documents = [doc['document'] for doc in collection.find()]

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Search the FAISS index
    distances, indices = index.search(query_embedding, top_k)

    # Return the top-k documents
    return [documents[i] for i in indices[0]]


# Function to handle API calls
def handle_api_call(query):
    if "order status" in query.lower():
        # Here, you would make an API call instead
        response = {"status": "success", "order_id": "12345", "details": "Order is being processed"}
        return response
    return None
