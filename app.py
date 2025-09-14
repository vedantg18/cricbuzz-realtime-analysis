import streamlit as st
from pages import home, live_matches, top_players, sql_queries, crud_operations

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Live Matches", "Top Player Stats", "SQL Queries", "CRUD Operations"])

if page == "Home":
    home.show_home()
elif page == "Live Matches":
    live_matches.show_live_matches()
elif page == "Top Player Stats":
    top_players.show_top_players()
elif page == "SQL Queries":
    sql_queries.show_sql_queries()
elif page == "CRUD Operations":
    crud_operations.show_crud_operations()
