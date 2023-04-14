import requests
import streamlit as st
import pickle
import pandas as pd
import time


def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data= response.json()

    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

    recommended_movies=[]
    recommended_movies_poster=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movie_dicts.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender')
st.snow()
selected_movie_name = st.selectbox(
    'Enter the name of the movie',
    movies['title'].values)

if st.button('Recommend'):
    with st.spinner('Wait for it...'):
        time.sleep(2)
    st.success('Done!')


    names,posters= recommend(selected_movie_name)

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.markdown(names[0])
        st.image(posters[0])

    with col2:
        st.markdown(names[1])
        st.image(posters[1])

    with col3:
        st.markdown(names[2])
        st.image(posters[2])

    with col4:
        st.markdown(names[3])
        st.image(posters[3])

    with col5:
        st.markdown(names[4])
        st.image(posters[4])


    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.markdown(names[5])
        st.image(posters[5])

    with col7:
        st.markdown(names[6])
        st.image(posters[6])

    with col8:
        st.markdown(names[7])
        st.image(posters[7])

    with col9:
        st.markdown(names[8])
        st.image(posters[8])

    with col10:
        st.markdown(names[9])
        st.image(posters[9])






    # for i in recommendations:
    #     st.write(i)