import streamlit as st
import streamlit_option_menu 
import pickle
import requests

st.set_page_config(layout='wide')

displayed = []

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=5c11f62767c0365b1611057ba4d7db90'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open('movie_similarity.pkl', 'rb'))
movies_list = movies['title'].values

st.session_state.user_menu = streamlit_option_menu.option_menu(
    menu_title = 'Hallo...',
    options = ['Terakhir nonton apa??'],
    icons = ['film'],
    menu_icon = 'list',
    orientation = 'horizontal',
)

st.title('Sistem Rekomendasi Film')

#dropdown pilih film
selected_movie = st.selectbox("Pilih Film", movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:8]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Rekomendasikan Film"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    with col6:
        st.text(movie_name[5])
        st.image(movie_poster[5])
    with col7:
        st.text(movie_name[6])
        st.image(movie_poster[6])