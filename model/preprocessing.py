import pandas as pd
import re
import spacy

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def load_dataset(file_path="iphone_16_faqs.csv"):
    """Loads and cleans FAQ dataset from the given file path."""
    try:
        df = pd.read_csv(file_path)  # Read dataset from given path
        df.dropna(inplace=True)  # Remove missing values
        df['Question'] = df['Question'].str.lower().str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
        return df
    except FileNotFoundError:
        print(f"Error: Dataset file '{file_path}' not found.")
        return None

def extract_product_features(description):
    """Extracts key product features using NLP."""
    doc = nlp(description)
    keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'ADJ']]
    return ", ".join(set(keywords))

# Test the dataset loading
if __name__ == "__main__":
    faq_data = load_dataset()  # Uses default filename if no argument is passed
    if faq_data is not None:
        print("Dataset Loaded Successfully!")
        print(faq_data.head())  # Display first few rows for verification
