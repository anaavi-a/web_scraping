### Setup and execution instructions
# 1. Get the Repository URL
Visit the GitHub repository you want to clone.
Click on the "Code" button (usually a green button).
Copy the URL provided (it should look like https://github.com/username/repository.git).
# 2. Open a Terminal or Command Prompt and navigate to the Directory Where You Want to Clone the Repository
# 3. Clone the Repository
Use the git clone command followed by the repository URL you copied earlier

### What does the script do?
# This Python code defines two functions and a script to gather information about top-rated movies in various genres from IMDb, along with user reviews for each movie. 

1. Top Movies Retrieval:
Utilizes the get_top_movies_by_genre function to fetch details of the top 20 movies in various genres from IMDb. Information includes movie titles, release years, and IMDb links.

2.User Reviews Retrieval:
Employs the get_user_reviews function to gather the latest 10 user reviews for each of the top movies, extracting review titles and content.

3. Data Organization:
Structures the collected data into a nested format, categorizing it by genre, and associating each movie with its details and user reviews.

4.Printing and JSON File Creation:
Prints the titles and release years of the top movies for each genre.
Writes the organized data into a JSON file named "movie_reviews.json" with a clear representation of genres, movies, and their respective user reviews.

### Assumptions 
1. IMDb Structure Stability:
Assumes that the HTML structure of the IMDb pages, particularly the search results and movie pages, remains relatively stable. Any changes to the IMDb website structure could potentially break the code.

2. Consistent Data Availability:
Assumes that the desired information (movie titles, release years, user reviews) is consistently available on the IMDb pages being scraped. Changes to IMDb's data presentation could impact the code's ability to extract relevant information.

3. Genre Availability:
Assumes that the specified genres are valid and available on IMDb. If IMDb updates its genre categories, some genres may become obsolete or new ones may be introduced.

4. Review Titles and Content:
Assumes that user reviews on IMDb pages consistently have titles and content in the expected HTML elements. Changes in the IMDb website layout may impact the extraction of review titles and content.
