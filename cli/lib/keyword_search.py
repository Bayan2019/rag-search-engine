from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    # 1. Preprocessing 4. Keyword Search
    # Iterate over all the movies in the list stored under the movies key, 
    # and check their "title" field
    # If the title contains the search query, 
    # append the movie to a results list.
    # for movie in movies:
    #     if query.lower() in movie['title'].lower().split():
    #         results.append(movie)
    for movie in movies:
        # 1. Preprocessing 5. Text Preprocessing
        # Update your matching logic to .lower() case 
        # both the search query and the movie titles 
        # before comparing them.
        preprocessed_query = preprocess_text(query)
        preprocessed_title = preprocess_text(movie["title"])        
        if preprocessed_query in preprocessed_title:
            results.append(movie)
            # 1. Preprocessing 4. Keyword Search
            # Truncate the list to a maximum of 5 results, order by IDs ascending.
    # results = sorted(results, key=lambda x: x['id'])
    # results = results[0:5]
            if len(results) >= limit:
                break
    return results

def preprocess_text(text: str) -> str:
    # 1. Preprocessing 5. Text Preprocessing
    # Update your matching logic to .lower() case 
    text = text.lower()
    return text