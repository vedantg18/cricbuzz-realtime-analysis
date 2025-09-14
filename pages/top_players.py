import streamlit as st
import pandas as pd

@st.cache_data
def load_players():
    # Use 'ISO-8859-1' encoding to handle special characters
    return pd.read_csv('notebooks/players_data.csv', encoding='ISO-8859-1')

def show_top_players():
    st.header("🌟 Player Stats Data")

    players_df = load_players()

    # Example: Top run-scorers (if column 'total_runs' exists)
    if 'career_total_runs' in players_df.columns:
        st.subheader("🏏 Top 10 Run Scorers")
        top_players = players_df.sort_values(by='career_total_runs', ascending=False).head(10)
        st.dataframe(top_players)
    else:
        st.warning("⚠️ Column 'total_runs' not found in players_data.csv.")
