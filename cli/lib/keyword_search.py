import string
from nltk.stem import PorterStemmer
import pickle
import os
from collections import defaultdict

from .search_utils import (
    CACHE_DIR,
    DEFAULT_SEARCH_LIMIT,
    load_movies,
    load_stopwords,
)

# 1. Preprocessing 4. Keyword Search
movies = load_movies()
# 1. Preprocessing 8. Stop Words
stopWords = load_stopwords()
# 1. Preprocessing 9.Stemming
stemmer = PorterStemmer()

# 2. TF-IDF 1. Inverted Index
# Create a new InvertedIndex class
class InvertedIndex:
    # 2. TF-IDF 1. Inverted Index
    def __init__(self) -> None:
        # An index attribute – a dictionary mapping 
        # tokens (strings) to sets of document IDs (integers).
        self.index = defaultdict(set)
        # A docmap attribute – a dictionary mapping 
        # document IDs to their full document objects.
        self.docmap: dict[int, dict] = {}
        self.index_path = os.path.join(CACHE_DIR, "index.pkl")
        self.docmap_path = os.path.join(CACHE_DIR, "docmap.pkl")

    # 2. TF-IDF 1. Inverted Index
    def __add_document(self, doc_id:int, text:str) -> None:
        # Tokenize the input text
        tokens = tokenize_text(text=text)
        for token in set(tokens):
            self.index[token].add(doc_id)
    
    # 2. TF-IDF 1. Inverted Index
    def get_documents(self, term:str)->list[int]:
        # It should get the set of document IDs for a given token
        # and return them as a list, sorted in ascending order
        ids = sorted(list(self.index.get(term, set())))
        return ids
    
    # 2. TF-IDF 1. Inverted Index
    def build(self)->None:
        for movie in movies:
            doc_id = movie['id']
            doc_description = f"{movie['title']} {movie['description']}"
            self.__add_document(doc_id, doc_description)
            self.docmap[doc_id] = movie

    # 2. TF-IDF 1. Inverted Index
    def save(self)->None:
        os.makedirs(CACHE_DIR, exist_ok=True)
        # if os.path.isdir("cache"):
        with open(self.index_path, 'wb') as file:
            pickle.dump(self.index, file)
        with open(self.docmap_path, 'wb') as file:
            pickle.dump(self.docmap, file)

# 2. TF-IDF 1. Inverted Index
def build_command() -> None:
    idx = InvertedIndex()
    idx.build()
    idx.save()
    docs = idx.get_documents("merida")
    print(f"First document for token 'merida' = {docs[0]}")

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    results = []
    # 1. Preprocessing 7. Tokenization
    query_tokens = tokenize_text(query)
    # 1. Preprocessing 4. Keyword Search
    # Iterate over all the movies in the list stored under the movies key
    for movie in movies:
        # 1. Preprocessing 7. Tokenization
        # Split the query and the title into tokens
        # query_tokens = tokenize_text(query)
        title_tokens = tokenize_text(movie["title"])  
        # 1. Preprocessing 7. Tokenization
        # Update your matching logic 
        if has_matching_token(query_tokens, title_tokens):
            results.append(movie)
            if len(results) >= limit:
                break

    return results

# 1. Preprocessing 5. Text Preprocessing
def preprocess_text(text: str) -> str:
    # 1. Preprocessing 5. Text Preprocessing
    # Update your matching logic to .lower() case 
    text = text.lower()
    # 1. Preprocessing 6. Punctuation
    # Remove all punctuation 
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    return text

# 1. Preprocessing 7. Tokenization
def tokenize_text(text: str) -> list[str]:
    # We already handled case insensitivity 
    # and punctuation removal in the previous steps.
    text = preprocess_text(text)
    # 1. Preprocessing 7. Tokenization
    # Split the query and the title into tokens
    # .split() on whitespace
    tokens = text.split()
    # 1. Preprocessing 7. Tokenization
    # Remove any empty tokens
                    # 1. Preprocessing 9.Stemming
                    # reduce each token to its root
    clean_tokens = [stemmer.stem(token) for token in tokens if token
                    # 1. Preprocessing 8. Stop Words
                    # Remove any stop words 
                    # from the user query tokens and the title tokens 
                    and token not in stopWords]
    return clean_tokens

# 1. Preprocessing 7. Tokenization
def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    # 1. Preprocessing 7. Tokenization
    # Update your matching logic 
    for query_token in query_tokens:
        # 1. Preprocessing 7. Tokenization
        # to allow matches where at least one token from the query
        for title_token in title_tokens:
            # 1. Preprocessing 7. Tokenization
            # matches any part of a token from the title.
            if query_token in title_token:
                return True
    return False