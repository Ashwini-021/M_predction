# Movie_Prediction: Movie Recommendation System

## Overview

`Movie_Prediction` is a content-based movie recommendation system that suggests movies to users based on a similarity score calculated from various movie features. The model analyzes the genres, keywords, tagline, cast, and director of movies to find and recommend films similar to the user's favorite movie.

## Features

- **Content-Based Filtering**: Recommends movies by analyzing and comparing movie features like genre, cast, and director.
- **Cosine Similarity**: Uses cosine similarity to calculate how closely related different movies are based on their feature vectors.
- **User Input**: Accepts a favorite movie from the user and returns the top 10 similar movies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Movie_Prediction.git
   cd Movie_Prediction
2.Install the required Python libraries:
  pip install pandas numpy scikit-learn
3.# Sample Input:
Enter your favourite movie name: The Matrix

# Sample Output:
Top 10 Movies Suggested for you:
1. The Matrix Reloaded
2. The Matrix Revolutions
3. Inception
4. Blade Runner
5. The Terminator
6. Minority Report
7. The Fifth Element
8. Tron: Legacy
9. Equilibrium
10. Dark City
