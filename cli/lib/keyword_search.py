from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies, load_stopwords
import string
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    stopWords = load_stopwords()
    results = []
    # 1. Preprocessing 7. Tokenization
    query_tokens = tokenize_text(query, stopWords)
    # 1. Preprocessing 4. Keyword Search
    # Iterate over all the movies in the list stored under the movies key
    for movie in movies:
        # 1. Preprocessing 7. Tokenization
        # Split the query and the title into tokens
        # query_tokens = tokenize_text(query)
        title_tokens = tokenize_text(movie["title"], stopWords)  
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
def tokenize_text(text: str, stopWords: list[str]) -> list[str]:
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