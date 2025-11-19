# Retrieval Augmented Generation

The best strategies, tools, and techniques for modern AI-powered search and retrieval.

And "retrieval" is the first component in RAG:
* **R**: **Retrieve** information via a search algorithm
* **A**: **Augment** our instructions with the search results
* **G**: **Generate** better, richer, and more accurate information using LLMs

## Preprocessing

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

## Resources

- [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)