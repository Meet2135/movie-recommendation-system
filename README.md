# 🎬 Movie Recommendation System

A comprehensive movie recommendation system that combines **Content-Based** and **Collaborative Filtering** approaches to provide personalized movie recommendations. Built with Python, Streamlit, and powered by TMDb API.

## 🌟 Features

- **Hybrid Recommendation Engine**: Combines content-based and collaborative filtering for better recommendations
- **Interactive Web Interface**: Beautiful Streamlit-based UI with movie posters and descriptions
- **Real-time Movie Data**: Fetches movie information and posters from TMDb API
- **Content-Based Filtering**: Uses movie features like genres, cast, crew, and keywords
- **Collaborative Filtering**: Leverages user ratings using Non-negative Matrix Factorization (NMF)
- **Smart Similarity Scoring**: Cosine similarity for content-based recommendations

## 📁 Project Structure

```
movie recommendation system/
├── app.py                          # Main Streamlit application
├── hybrid.ipynb                    # Jupyter notebook with model development
├── model/                          # Trained models and data
│   ├── collab.pkl                 # Collaborative filtering model (NMF)
│   ├── content.pkl                # Content-based model (CountVectorizer + similarity)
│   ├── similarity.pkl             # Pre-computed similarity matrix
│   ├── movie_list.pkl             # Processed movie dataset
│   └── count_vectorizer.pkl       # Fitted CountVectorizer
├── tmdb_5000_movies.csv           # TMDb movies dataset
├── tmdb_5000_credits.csv          # TMDb credits dataset
├── links.csv                      # MovieLens to TMDb ID mapping
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install streamlit pandas numpy scikit-learn requests
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 🎯 How to Use

1. **Select a Movie**: Choose any movie from the dropdown menu
2. **Get Recommendations**: Click "Show Recommendations" button
3. **Explore Results**: View recommended movies with posters and descriptions

## 🔧 Technical Details

### Data Sources

- **TMDb 5000 Movies Dataset**: Contains movie metadata (title, overview, genres, keywords)
- **TMDb 5000 Credits Dataset**: Contains cast and crew information
- **MovieLens Links**: Maps MovieLens IDs to TMDb IDs for rating data

### Model Architecture

#### Content-Based Filtering
- **Feature Extraction**: Combines movie overview, genres, keywords, cast, and crew
- **Vectorization**: Uses CountVectorizer with 5000 features
- **Similarity**: Cosine similarity between movie vectors

#### Collaborative Filtering
- **Matrix Factorization**: Non-negative Matrix Factorization (NMF) with 50 components
- **Rating Prediction**: Predicts user ratings for unseen movies
- **Scalability**: Handles sparse rating matrices efficiently

#### Hybrid Approach
- **Combination**: Weighted average of content-based and collaborative scores
- **Parameter**: α (alpha) controls the balance between approaches
- **Default**: α = 0.5 (equal weighting)

### API Integration

- **TMDb API**: Fetches movie posters and descriptions in real-time
- **Error Handling**: Robust retry mechanism for API failures
- **Caching**: Efficient session management for API requests

## 📊 Model Performance

The system provides recommendations based on:

- **Content Similarity**: Movies with similar genres, cast, and themes
- **User Preferences**: Patterns from similar users' rating behavior
- **Hybrid Scoring**: Balanced approach combining both methods

## 🛠️ Development

### Model Training

The models are trained using the `hybrid.ipynb` notebook, which includes:

1. **Data Preprocessing**: Cleaning and merging datasets
2. **Feature Engineering**: Creating movie tags from multiple sources
3. **Model Training**: Training both content-based and collaborative models
4. **Model Persistence**: Saving trained models for deployment

### Key Functions

- `recommend(movie_title)`: Returns top 5 movie recommendations
- `fetch_movie_data(movie_id)`: Retrieves movie data from TMDb API
- `hybrid_recommend(user_id, movie_title, α=0.5)`: Hybrid recommendation function

## 🔒 API Configuration

The application uses a TMDb API key for fetching movie data. The current key is included in the code, but for production use, consider:

- Using environment variables for API keys
- Implementing rate limiting
- Adding API key rotation

## 📈 Future Enhancements

- **User Authentication**: Personal recommendation history
- **Advanced Filtering**: Filter by genre, year, rating
- **A/B Testing**: Compare different recommendation algorithms
- **Real-time Learning**: Update models with new user interactions
- **Mobile App**: Native mobile application

## 🤝 Contributing

Feel free to contribute to this project by:

1. Forking the repository
2. Creating a feature branch
3. Making your changes
4. Submitting a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **TMDb**: For providing comprehensive movie data and API
- **MovieLens**: For user rating datasets
- **Streamlit**: For the beautiful web interface framework
- **Scikit-learn**: For machine learning algorithms

---

**Happy Movie Watching! 🍿**
