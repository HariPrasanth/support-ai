import os
import streamlit as st
from utils import search_documents, handle_api_call
import joblib

# Path to the model file
model_filename = 'models/sentence_transformer_model.pkl'

# Check if the model file exists
if not os.path.exists(model_filename):
    # If not, run the save_model script
    import subprocess
    subprocess.run(["python", "models/save_model.py"])

# Load the model
model = joblib.load(model_filename)

st.title("support.ai: Customer Support AI")

query = st.text_input("Ask a question about Artificial Intelligence:")
if query:
    api_response = handle_api_call(query)
    if api_response:
        st.write("API Response:")
        st.write(api_response)
    else:
        results = search_documents(query, model)
        st.write("Top answers:")
        for result in results:
            st.write(result)
