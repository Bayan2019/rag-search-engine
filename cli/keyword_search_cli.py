#!/usr/bin/env python3

import argparse
from lib.keyword_search import search_command

# 1. Preprocessing 3. Project Overview
def main() -> None:

    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()


    match args.command:
        case "search":
            # 1. Preprocessing 3. Project Overview
            # print the search query here
            print(f"Searching for: {args.query}")

            # 1. Preprocessing 4. Keyword Search
            # Print the results 
            results = search_command(args.query)
            for i, res in enumerate(results, 1):
                print(f"{i}. {res['title']}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()