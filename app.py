import pickle
import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# -- TMDb API setup ----------------------------------------------------------
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/{}"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500/"

# -- Configure a retrying session --------------------------------------------
retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    raise_on_status=False
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

def fetch_movie_data(movie_id):
    """Fetch TMDb overview and poster URL for a movie ID."""
    url = TMDB_MOVIE_URL.format(movie_id)
    params = {"api_key": API_KEY, "language": "en-US"}

    try:
        resp = session.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        overview    = data.get("overview", "No description available.")
        poster_path = data.get("poster_path")
        poster_url  = TMDB_IMAGE_BASE + poster_path if poster_path else None
        return overview, poster_url

    except requests.exceptions.RequestException as e:
        st.warning(f"⚠️ Failed to fetch movie data: {e}")
        return "No description available.", None

def recommend(movie_title):
    """Return lists of top-5 titles, overviews, and poster URLs."""
    idx = movies[movies['title'] == movie_title].index[0]
    sims = sorted(
        enumerate(similarity[idx]),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    titles, overviews, posters = [], [], []
    for i, _ in sims:
        mid   = movies.iloc[i].movie_id
        name  = movies.iloc[i].title
        ovw, p = fetch_movie_data(mid)
        titles.append(name)
        overviews.append(ovw)
        posters.append(p)
    return titles, overviews, posters

# -- Streamlit UI -----------------------------------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header("🎥 Content-Based Movie Recommender")

# Load data
movies     = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

selected = st.selectbox("Type or select a movie:", movies['title'].values)

if st.button("Show Recommendations"):
    names, descs, imgs = recommend(selected)

    for name, desc, img in zip(names, descs, imgs):
        st.markdown("---")
        col1, col2 = st.columns([1, 3])
        with col1:
            if img:
                # Use a fixed width for smaller posters
                st.image(img, width=200)
            else:
                st.write("No poster available.")
        with col2:
            st.subheader(name)
            st.write(desc)
