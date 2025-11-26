# Retrieval Augmented Generation

The best strategies, tools, and techniques for modern AI-powered search and retrieval.

And "retrieval" is the first component in RAG:
* **R**: **Retrieve** information via a search algorithm
* **A**: **Augment** our instructions with the search results
* **G**: **Generate** better, richer, and more accurate information using LLMs

## 1. Preprocessing

### 2. What Is Search?

1. Use `uv` to create a new project. 
    ```sh
    uv init rag-search-engine
    cd rag-search-engine
    ```
2. Create a virtual environment at the top level of your project directory:
    ```sh
    uv venv
    ```
3. Activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```
4. Create a `data` directory in your project root.
    ```sh
    mkdir data
    ```
5. Download the movie dataset and save it as `data/movies.json`.
    ```sh
    curl -o data/movies.json https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/course-rag-movies.json 
    ```
6. Add `/data/` to your `.gitignore` file to keep large data files out of version control.
    ```sh
    echo "/data/" >> .gitignore
    ```

### 3. Project Overview

We'll be implementing **Hoopla** as a collection of command line scripts that perform various search operations on a local dataset of movies.

1. In your project's root, create a new `cli` directory. 
This is where we'll place all our entrypoint scripts to run our various search implementations.
    ```sh
    mkdir cli
    ```
2. Delete the current `main.py` file – we won't need it.
    ```sh
    rm main.py
    ```
3. In the cli directory, create a new file called `keyword_search_cli.py`.
    ```sh
    touch cli/keyword_search_cli.py
    ```


### 4. Keyword Search

### 5. Text Processing 

* **Case insensitivity**: Convert all text to lowercase
    * `"The Matrix"` becomes `"the matrix"`
    * `"HE IS HERE"` becomes `"he is here"`
* **Remove punctuation**: We don't care about periods, commas, etc
    * `"Hello, world!"` becomes `"hello world"`
    * `"sci-fi"` becomes `"scifi"`
* **Tokenization**: Break text into individual words
    `"the matrix"` becomes `["the", "matrix"]`
    `"hello world"` becomes `["hello", "world"]`
* **Stop words**: Remove common stop words that don't add much meaning
    * `["the", "matrix"]` becomes `["matrix"]`
    * `["a", "puppy"]` becomes `["puppy"]`
* **Stemming**: Keep only the stem of words
    * `["running", "jumping"]` becomes `["run", "jump"]`
    * `["watching", "windmills"]` becomes `["watch", "windmill"]`

### 6. Punctuation

### 7. Tokenization

Tokenization means splitting text into smaller pieces, called tokens.

### 8. Stop Words

Now that we have a list of tokens, we need to decide which ones are actually useful for search. 
Not all tokens are created equal...

### 9. Stemming

Install the nltk library:
```sh
uv add nltk==3.9.1
```

## 2. TF-IDF

### 1. Inverted Index

An **inverted index** is what makes search fast – it's like a SQL database index, but for text search. 
Instead of scanning every document each time a user searches, we build an index for fast lookups.

A "forward index" maps location -> value. 
An "inverted index" maps value -> location.

### 2. Use the Index

### 3. Boolean Search

### 4. Term Frequency (TF)

### 5. Inverse Document Frequency

### 6. TF-IDF

## 3. Keyword Search

## 4. Semantic Search

## 5. Chunking

## 6. Hybrid Search

## 7. LLMs

## 8. Reranking

## 9. Evaluation

## 10. Augmented Generation

## 11. Agentic 

## 12. Multimodal

## Resources

- [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)