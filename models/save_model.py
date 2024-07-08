import joblib
from sentence_transformers import SentenceTransformer

# Load a pre-trained model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')

# Save the model to a file
model_filename = 'models/sentence_transformer_model.pkl'
joblib.dump(model, model_filename)

print("Model saved locally.")
