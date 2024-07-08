import joblib

# Load the model from the file
model_filename = 'sentence_transformer_model.pkl'
model = joblib.load(model_filename)

print("Model loaded from local storage.")
