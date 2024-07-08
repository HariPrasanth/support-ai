import wikipediaapi
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')

# Function to fetch content from Wikipedia
def fetch_wikipedia_content(topic, depth=1):
    page = wiki_wiki.page(topic)
    content = [page.summary]
    if depth > 0:
        for section in page.sections:
            content.extend(fetch_wikipedia_content(section.title, depth - 1))
    return content

# Fetch content for a topic
topic = "Artificial Intelligence"
documents = fetch_wikipedia_content(topic)

# Load a pre-trained model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings for the documents
embeddings = model.encode(documents)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['wiki_db']
collection = db['documents']

# Store documents and embeddings in MongoDB
for doc, emb in zip(documents, embeddings):
    collection.insert_one({
        'document': doc,
        'embedding': emb.tolist()
    })

print("Documents and embeddings stored successfully.")
