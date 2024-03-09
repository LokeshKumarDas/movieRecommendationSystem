# run MovieRecommenderSystemCode.ipynb file and create pickle files
# then create virtual environment
# python -m venv venv 
# activate virtual environment
# venv\Scripts\activate 
# install streamlit 
# pip install streamlit
# to see the website use
# streamlit run app.py



# importing libraries
import streamlit as st 
import pickle
import pandas as pd

# loading pickle file
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# function to recommend movies

def recommend(movie):
    
    # access movie index from title
    movie_index = movies[movies['title'] == movie].index[0]
    
    # access distance of movie from other movies
    distance = similarity[movie_index]
    
    # sort the distance and take first 5, as they are the nearest
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    # creating the list of top 5 recommended movies
    recommended_movies = []
    
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

# set the title of page
st.title('Movies Recommender')

# creating search box to type movie name
selected_movie_name = st.selectbox(
    'Search For Movies .... ',
    movies['title'].values
)

# creating a button, when clicked show top 5 recommended movies
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
