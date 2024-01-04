import requests
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }

def get_top_movies_by_genre(genre):
    min_votes = 5000
    top_movies_by_genre = {}
    url = f'https://www.imdb.com/search/title/?genres={genre}&sort=user_rating,desc&title_type=feature&num_votes={min_votes}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(genre + " genre fetched and being analysed")
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all('li', class_="ipc-metadata-list-summary-item")[:20]  # Limit to top 20 movies
        top_movies_by_genre = []
        movie_link = []
        for movie in movies:
            title = movie.find('h3', class_='ipc-title__text').text
            year = movie.find('span', class_='sc-43986a27-8 jHYIIK dli-title-metadata-item').text
            mo_li = movie.a.get('href')
            # print(mo_li)
            top_movies_by_genre.append({'title': title, 'year': year})
            movie_link.append(mo_li)
    else:
        print(url + " - ERROR - " + response)
    return top_movies_by_genre, movie_link


def get_user_reviews(movie_url):
    reviews = []
    reviews_title = []
    response = requests.get(movie_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        user_reviews = soup.find_all('div', class_='lister-item-content')[:10]  # Limit to latest 10 reviews
        for review in user_reviews:
            title = review.find('a', class_='title').text.strip() 
            text = review.find('div', class_='text show-more__control').text.strip()
            reviews_title.append(title)
            reviews.append(text)
    else:
        print("technical error")
    return reviews, reviews_title

data_to_print = []
genres = ['family','action','adventure','animation','biography','comedy','crime','documentary','drama','fantasy','film-noir','history','horror','music','musical','mystery','romance','sci-fi','short','sport','thriller','war','western']  # Add more genres as needed
for genre in genres:
    data = []
    top_movies, top_movies_link = get_top_movies_by_genre(genre)
    for i,movie in enumerate(top_movies):
        movie_title = movie['title'].split('. ')[1]     # Removes serial number from the start of the extracted names
        movie_year = movie['year']
        review_data = []
        imdb_link = top_movies_link[i]       
        imdb_link = imdb_link.split('?')[0] 
        imdb_link = "https://www.imdb.com" + imdb_link + "reviews?sort=submissionDate&dir=desc&ratingFilter=0"
        user_reviews_full, user_reviews = get_user_reviews(imdb_link)
        for idx, abc in enumerate(user_reviews, start=1):
            review_data_to_append = {
                "heading" : user_reviews[idx-1],
                "content" : user_reviews_full[idx-1]
            }
            review_data.append(review_data_to_append)
        movie_data = {
            "name" : movie_title,
            "year" : movie_year,
            "reviews" : review_data 
        }
        print(str(i+1) + ": " + movie_title + " - " + movie_year) 
        data.append(movie_data)
    data_to_append = {
        "Genre" : genre,
        "Movies_and_reviews" : data
    }
    data_to_print.append(data_to_append)

    
json_file = 'movie_reviews.json'
with open(json_file, 'w') as file:
    json.dump(data_to_print, file, indent=5)

print(f'JSON file "{json_file}" has been created.')