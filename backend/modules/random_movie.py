import requests
import json
import os
from dotenv import load_dotenv
import random
from filter import filter, common_search_words
from omdb_api import get_API_response
import streamlit as st
load_dotenv()

os.environ["OMDB_API"] = st.secrets['OMDB_API']


def get_movie(title):
    
    # api_key = os.environ.get('OMDB_API')
    
    # if api_key is None:
    #     print("Error: OMDB_API environment variable is not set.")
    #     return
    
    # url = f'http://www.omdbapi.com/?s={title}&apikey={api_key}'

    # response = requests.get(url)

    # if response.status_code == 200:
    #     data = response.json()
    #     if 'Search' in data:
    #         for movie in data['Search']:
    #             if title.lower() in movie['Title'].lower():
    #                 movie_details_url = f"http://www.omdbapi.com/?i={movie['imdbID']}&apikey={api_key}"
    #                 movie_response = requests.get(movie_details_url)
    #                 if movie_response.status_code == 200:
    #                     data = movie_response.json()
    #                     result = json.dumps(data['Title'], indent=4)
    #                     print(result)
    #                     return result
    #     print("No movies found with the specified word in the title.")
    # else:
    #     print(f"Error with the request: {response.status_code}")
    #     print(response.text)
    response = get_API_response(title)

    if response is not None:
        data = response.json()
        if data['Response']:
            for movie in data['Search']:
                if title.lower() in movie['Title'].lower():
                    movie_details_url = f"http://www.omdbapi.com/?i={movie['imdbID']}&apikey={api_key}"
                    movie_response = requests.get(movie_details_url)
                    if movie_response.status_code == 200:
                        data = movie_response.json()
                        result = json.dumps(data['Title'], indent=4)
                        print(result)
                        return result
        print("No movies found with the specified word in the title.")
    else:
        print(f"Error with the request: {response.status_code}")
        print(response.text)

def get_random_word():
    random_word = random.choice(common_search_words)
    return random_word

if __name__ == '__main__':
    get_movie()