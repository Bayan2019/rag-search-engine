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



## Resources

- [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)