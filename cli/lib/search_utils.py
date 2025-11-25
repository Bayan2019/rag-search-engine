import json
import os


# 1. Preprocessing 4. Keyword Search
# Truncate the list to a maximum of 5 results, 
# order by IDs ascending.
DEFAULT_SEARCH_LIMIT = 5

# 1. Preprocessing 4. Keyword Search
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# 1. Preprocessing 4. Keyword Search
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
# 1. Preprocessing 8. Stop Words
STOP_WORDS_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")

# 2. TF-IDF 1. Inverted Index
CACHE_DIR = os.path.join(PROJECT_ROOT, "cache")

# 1. Preprocessing 4. Keyword Search
# Load the data/movies.json file into a Python dictionary
def load_movies() -> list[dict]:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]

# 1. Preprocessing 8. Stop Words
# Read the stop words from the file 
# and store them in a list.
def load_stopwords() -> list[str]:
    with open(STOP_WORDS_PATH, "r") as f:
        stopWords = f.read().splitlines()
    return stopWords