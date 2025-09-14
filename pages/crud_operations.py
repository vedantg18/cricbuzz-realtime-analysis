import streamlit as st
import pandas as pd

@st.cache_data
def load_players():
    try:
        return pd.read_csv("notebooks/players_data.csv", encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv("notebooks/players_data.csv", encoding="latin1")

def save_players(df):
    df.to_csv("notebooks/players_data.csv", index=False, encoding="utf-8-sig")
    st.success("✅ Data saved successfully!")

def ensure_columns(df):
    """Ensure required columns exist"""
    required_cols = ["player_name", "playing_role", "batting_style", "bowling_style", "player_id", "field_pos", "player_image"]
    # Map CSV columns to your standard names
    if "bat_style" in df.columns:
        df["batting_style"] = df["bat_style"]
    if "bowl_style" in df.columns:
        df["bowling_style"] = df["bowl_style"]
    if "player_full_name" in df.columns:
        df["player_name"] = df["player_full_name"]
    
    # Ensure all required columns exist
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""
    return df[required_cols]

def show_crud_operations():
    st.header("📝 CRUD Operations for Players Data")

    players_df = load_players()
    players_df = ensure_columns(players_df)

    st.subheader("📋 Current Players Data")
    st.dataframe(players_df)

    # ---------------- CREATE ----------------
    st.subheader("➕ Add New Player")
    with st.form("add_player_form"):
        player_name = st.text_input("Full Name")
        playing_role = st.text_input("Playing Role")
        batting_style = st.text_input("Batting Style")
        bowling_style = st.text_input("Bowling Style")
        submit = st.form_submit_button("Add Player")

        if submit:
            new_row = pd.DataFrame([{
                "player_name": player_name,
                "playing_role": playing_role,
                "batting_style": batting_style,
                "bowling_style": bowling_style,
                "player_id": "",  # you can generate or leave empty
                "field_pos": "",
                "player_image": ""
            }])
            players_df = pd.concat([players_df, new_row], ignore_index=True)
            save_players(players_df)
            st.dataframe(players_df)

    # ---------------- UPDATE ----------------
    st.subheader("✏️ Update Player")
    if not players_df.empty:
        player_to_update = st.selectbox(
            "Select Player to Update", players_df["player_name"].tolist()
        )
        player_data = players_df[players_df["player_name"] == player_to_update].iloc[0]

        with st.form("update_player_form"):
            updated_name = st.text_input("Full Name", value=player_data["player_name"])
            updated_role = st.text_input("Playing Role", value=player_data["playing_role"])
            updated_batting = st.text_input("Batting Style", value=player_data["batting_style"])
            updated_bowling = st.text_input("Bowling Style", value=player_data["bowling_style"])
            update_submit = st.form_submit_button("Update Player")

            if update_submit:
                players_df.loc[
                    players_df["player_name"] == player_to_update,
                    ["player_name", "playing_role", "batting_style", "bowling_style"]
                ] = [updated_name, updated_role, updated_batting, updated_bowling]

                save_players(players_df)
                st.dataframe(players_df)

    # ---------------- DELETE ----------------
    st.subheader("🗑️ Delete Player")
    if not players_df.empty:
        with st.form("delete_player_form"):
            player_to_delete = st.selectbox(
                "Select Player to Delete", players_df["player_name"].tolist()
            )
            delete_submit = st.form_submit_button("Delete Player")

            if delete_submit:
                players_df = players_df[players_df["player_name"] != player_to_delete]
                save_players(players_df)
                st.dataframe(players_df)
