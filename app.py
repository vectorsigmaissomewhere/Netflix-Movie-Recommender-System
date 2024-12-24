import streamlit as st 
import pickle 
import requests

movies = pickle.load(open("movies_list.pk1", "rb"))
similarity = picke.load(open("similarity.pk1", "rb"))
movies_list = movies['title'].values

st.header("Movie Recommender System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    url = ""
    requests.get(url)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https"+poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.illoc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title))
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommend"):
    movie_name = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.images(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.images(movie_poster[0])
    with col3:
        st.text(movie_name[2])
        st.images(movie_poster[0])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
    
        
