[10:25 pm, 11/8/2024] Gauri Kale YCCE: meet hogayi shuru
[10:25 pm, 11/8/2024] +91 7499 741 951: .
[10:34 pm, 11/8/2024] +91 7499 741 951: def display_movie_details(movie):
    """Display the details of the selected movie."""
    print(f"Title: {movie['title']}")
    print(f"Trailer: {movie['trailer']}")
    print(f"Cast: {movie['cast']}")
    print(f"Director: {movie['director']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Budget: {movie['budget']}")
    print(f"Collection: {movie['collection']}")
    print(f"Verdict: {movie['verdict']}")
    print(f"IMDb Rating: {movie['rating']}")
    print(f"Public Review: {movie['review']}")
    print(f"Available on: {movie['platform']}")
    print()

def main():
    # Sample movie data
    movies = {
        'Bollywood': {
            'Action': [
                {
                    'title': 'PK',
                    'trailer': 'https://www.youtube.com/watch?v=1z2C2u2Yo38',
                    'cast': 'Aamir Khan, Anushka Sharma',
                    'director': 'Rajkumar Hirani',
                    'release_date': '2014-12-19',
                    'budget': '$17 million',
                    'collection': '$100 million',
                    'verdict': 'A thought-provoking and entertaining film.',
                    'rating': '8.1',
                    'review': 'A mix of humor and social commentary.',
                    'platform': 'Netflix'
                },
                {
                    'title': 'Bajrangi Bhaijaan',
                    'trailer': 'https://www.youtube.com/watch?v=8O2uRpS2hIY',
                    'cast': 'Salman Khan, Kareena Kapoor',
                    'director': 'Kabir Khan',
                    'release_date': '2015-07-17',
                    'budget': '$14 million',
                    'collection': '$150 million',
                    'verdict': 'A heartwarming action-drama.',
                    'rating': '8.0',
                    'review': 'Emotionally engaging with a strong performance by Salman Khan.',
                    'platform': 'Disney+ Hotstar'
                },
                # Add more Bollywood Action movies
            ],
            'Comedy': [
                {
                    'title': '3 Idiots',
                    'trailer': 'https://www.youtube.com/watch?v=K0eDlF6bG8c',
                    'cast': 'Aamir Khan, R. Madhavan',
                    'director': 'Rajkumar Hirani',
                    'release_date': '2009-12-25',
                    'budget': '$8 million',
                    'collection': '$85 million',
                    'verdict': 'A mix of comedy and drama with a strong message.',
                    'rating': '8.4',
                    'review': 'Heartwarming and thought-provoking.',
                    'platform': 'Amazon Prime Video'
                },
                # Add more Bollywood Comedy movies
            ],
            # Add more categories for Bollywood
        },
        'Hollywood': {
            'Adventure': [
                {
                    'title': 'Mad Max: Fury Road',
                    'trailer': 'https://www.youtube.com/watch?v=hEJnMQG9ev8',
                    'cast': 'Tom Hardy, Charlize Theron',
                    'director': 'George Miller',
                    'release_date': '2015-05-15',
                    'budget': '$150 million',
                    'collection': '$375 million',
                    'verdict': 'High-octane action with stunning visuals.',
                    'rating': '8.1',
                    'review': 'A relentless, visually arresting action spectacle.',
                    'platform': 'Hulu'
                },
                # Add more Hollywood Adventure movies
            ],
            # Add more categories for Hollywood
        },
        'Sandalwood': {
            'Drama': [
                {
                    'title': 'KGF Chapter 1',
                    'trailer': 'https://www.youtube.com/watch?v=5A2-G7CkHT8',
                    'cast': 'Yash, Srinidhi Shetty',
                    'director': 'Prashanth Neel',
                    'release_date': '2018-12-21',
                    'budget': '$14 million',
                    'collection': '$70 million',
                    'verdict': 'A gripping tale with high-octane action sequences.',
                    'rating': '8.2',
                    'review': 'A blockbuster hit with great performances and high production values.',
                    'platform': 'Amazon Prime Video'
                },
                # Add more Sandalwood Drama movies
            ],
            # Add more categories for Sandalwood
        },
        # Add more industries like Tollywood, Mollywood, Kollywood, Chinese film industry
    }

    categories = ['Romantic', 'Action', 'Comedy', 'Drama', 'Horror', 'Fantasy', 'Adventure', 'Science Fiction', 'Thriller', 'Crime', 'Mystery', 'War', 'Biopic']
    industries = ['Hollywood', 'Bollywood', 'Sandalwood', 'Tollywood', 'Mollywood', 'Kollywood', 'Chinese film industry']
    
    # Get user inputs for industry
    print("Select an industry:", ', '.join(industries))
    industry = input().capitalize()
    
    if industry not in industries:
        print("Invalid industry.")
        return
    
    # Get user inputs for category
    print("Select a movie type:", ', '.join(categories))
    category = input().capitalize()
    
    if category not in categories:
        print("Invalid category.")
        return
    
    # Display movies based on user inputs
    if industry in movies and category in movies[industry]:
        print(f"Movies in {industry} - {category} category:")
        for i, movie in enumerate(movies[industry][category], start=1):
            print(f"{i}. {movie['title']}")
        
        # Select a movie
        try:
            choice = int(input("Enter the number of the movie you want to view details for: "))
            selected_movie = movies[industry][category][choice - 1]
            display_movie_details(selected_movie)
        except (IndexError, ValueError):
            print("Invalid selection.")
    else:
        print("No movies found for the selected criteria.")

if _name_ == "_main_":
    main()
