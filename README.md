# support.ai

support.ai is a customer support AI bot that uses Wikipedia data to answer questions. It leverages the power of Sentence Transformers and FAISS for semantic search and MongoDB for storing documents and embeddings.

## Project Structure


## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/support.ai.git
    cd support.ai
    ```

2. Install the required dependencies:
    ```bash
    pip install -r app/requirements.txt
    ```

3. Fetch Wikipedia data and store it in MongoDB:
    ```bash
    python data/wikipedia_data.py
    ```

4. Save the model locally:
    ```bash
    python models/save_model.py
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run app/app.py
    ```

## Usage

- Open the Streamlit app in your browser.
- Enter a question about Artificial Intelligence.
- View the top answers or API responses provided by support.ai.

## License

[MIT License](LICENSE)
