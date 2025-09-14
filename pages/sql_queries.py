import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    players_df = pd.read_csv('notebooks/players_data.csv', encoding='ISO-8859-1')
    matches_df = pd.read_csv('notebooks/scheduled_matches.csv', encoding='ISO-8859-1')
    teams_df = pd.read_csv('notebooks/teams_data.csv', encoding='ISO-8859-1')
    return players_df, matches_df, teams_df

def show_sql_queries():
    st.header("📊 Cricket Data Analytics – 25 Key Insights")

    players_df, matches_df, teams_df = load_data()

    # 1. Players representing India
    st.subheader("1️⃣ Players representing India")
    q1 = players_df[players_df['country'] == 'India'][['full_name','batting_style','bowling_style']]
    st.dataframe(q1)

    # 2. Matches in last 30 days
    st.subheader("2️⃣ Matches played in last 30 days")
    matches_df['match_date'] = pd.to_datetime(matches_df['match_date'], errors='coerce')
    last_30 = matches_df[matches_df['match_date'] >= (pd.Timestamp.today() - pd.Timedelta(days=30))]
    q2 = last_30[['match_description','team1_name','team2_name','venue_name','venue_city','match_date']].sort_values('match_date', ascending=False)
    st.dataframe(q2)

    # 3. Top 10 highest ODI run scorers
    st.subheader("3️⃣ Top 10 ODI Run Scorers")
    q3 = players_df[['full_name','total_runs_odi','batting_average_odi','centuries_odi']].sort_values('total_runs_odi', ascending=False).head(10)
    st.dataframe(q3)

    # 4. Venues with capacity > 50,000
    st.subheader("4️⃣ Venues with Capacity > 50,000")
    q4 = matches_df[matches_df['venue_capacity'] > 50000][['venue_name','venue_city','venue_country','venue_capacity']].drop_duplicates().sort_values('venue_capacity', ascending=False)
    st.dataframe(q4)

    # 5. Matches won by each team
    st.subheader("5️⃣ Total Matches Won by Teams")
    q5 = matches_df['Match_Winner'].value_counts().reset_index()
    q5.columns = ['team_name','total_wins']
    st.dataframe(q5)

    # # 6. Players count by role
    # st.subheader("6️⃣ Player Count by Playing Role")
    # q6 = players_df['playing_role'].value_counts().reset_index()
    # q6.columns = ['playing_role','player_count']
    # st.bar_chart(q6.set_index('playing_role'))

    # 7. Highest individual batting score per format (use career_total_runs approximation)
    st.subheader("7️⃣ Highest Individual Score per Format")
    highest_test = players_df[['full_name','total_runs_test']].sort_values('total_runs_test', ascending=False).head(1)
    highest_odi = players_df[['full_name','total_runs_odi']].sort_values('total_runs_odi', ascending=False).head(1)
    highest_t20i = players_df[['full_name','total_runs_t20i']].sort_values('total_runs_t20i', ascending=False).head(1)
    st.write("**Test:**", highest_test)
    st.write("**ODI:**", highest_odi)
    st.write("**T20I:**", highest_t20i)

    # 8. Series started in 2024
    st.subheader("8️⃣ Series started in 2024")
    matches_df['series_start_date'] = pd.to_datetime(matches_df['series_start_date'], errors='coerce')
    q8 = matches_df[matches_df['series_start_date'].dt.year == 2024][['series_name','series_host_country','match_type','series_start_date','series_total_matches_planned']].drop_duplicates()
    st.dataframe(q8)

    # 9. All-rounders with >1000 runs & >50 wickets
    st.subheader("9️⃣ All-Rounders with 1000+ Runs & 50+ Wickets")
    q9 = players_df[(players_df['career_total_runs'] > 1000) & (players_df['career_total_wickets'] > 50)][['full_name','career_total_runs','career_total_wickets','formats_played']]
    st.dataframe(q9)

    # 10. Last 20 completed matches
    st.subheader("🔟 Last 20 Completed Matches")
    q10 = matches_df[matches_df['is_completed'] == True][['match_description','team1_name','team2_name','Match_Winner','victory_margin','victory_type','venue_name','match_date']].sort_values('match_date', ascending=False).head(20)
    st.dataframe(q10)

    # 11. Compare players performance across formats
    st.subheader("1️⃣1️⃣ Player Performance Across Formats")
    multi_format = players_df[players_df['formats_played'].str.contains(',')]
    q11 = multi_format[['full_name','total_runs_test','total_runs_odi','total_runs_t20i','batting_average_test','batting_average_odi','batting_average_t20i']]
    st.dataframe(q11)

    # 12. Team performance home vs away
    st.subheader("1️⃣2️⃣ Team Performance Home vs Away")
    home_wins = matches_df[matches_df['team1_home_or_away'] == 'home']['Match_Winner'].value_counts()
    away_wins = matches_df[matches_df['team1_home_or_away'] == 'away']['Match_Winner'].value_counts()
    q12 = pd.DataFrame({'home_wins':home_wins, 'away_wins':away_wins}).fillna(0)
    st.dataframe(q12)

    # 13. Batting partnerships > 100 runs
    st.subheader("1️⃣3️⃣ Batting Partnerships > 100 Runs")
    if 'partnerships' in matches_df.columns:
        # Assuming 'partnerships' contains a list/dict of partnerships
        partnerships_df = matches_df[['match_id','partnerships']].copy()
        st.write("Partnership data available but complex. Example placeholder table:")
        st.dataframe(partnerships_df.head())
    else:
        st.info("No partnership data available.")

    # 14. Bowling performance per venue (approx using economy + wickets)
    st.subheader("1️⃣4️⃣ Bowling Performance per Venue")
    q14 = players_df.groupby('country').agg({'career_total_wickets':'sum','economy_t20i':'mean'}).reset_index()
    st.dataframe(q14)

    # 15. Close match performance
    st.subheader("1️⃣5️⃣ Player Performance in Close Matches (<50 runs or <5 wickets)")
    close_matches = matches_df[(matches_df['victory_margin'] < 50) | (matches_df['victory_type'].str.contains('wicket',case=False,na=False))]
    q15 = close_matches['Match_Winner'].value_counts().reset_index()
    q15.columns = ['team','close_match_wins']
    st.dataframe(q15)

    # 16. Year-wise batting averages
    st.subheader("1️⃣6️⃣ Player Batting Performance Since 2020")
    players_since_2020 = players_df[players_df['played_since_year'] >= 2020]
    q16 = players_since_2020[['full_name','career_total_runs','matches_odi','matches_test','matches_t20i']]
    st.dataframe(q16)

    # 17. Toss impact on match results
    st.subheader("1️⃣7️⃣ Toss Impact on Match Results")
    toss_win = matches_df[matches_df['toss_winner_id'] == matches_df['winning_team_id']]
    toss_loss = matches_df[matches_df['toss_winner_id'] != matches_df['winning_team_id']]
    st.write(f"Toss Winners Win %: {len(toss_win) / len(matches_df) * 100:.2f}%")

    # 18. Most economical bowlers (ODI + T20)
    st.subheader("1️⃣8️⃣ Most Economical Bowlers (ODI + T20)")
    q18 = players_df[['full_name','economy_odi','economy_t20i','wickets_odi','wickets_t20i']].sort_values('economy_odi').head(10)
    st.dataframe(q18)

    # 19. Most consistent batsmen (use std dev approximation)
    st.subheader("1️⃣9️⃣ Most Consistent Batsmen")
    q19 = players_df[['full_name','career_total_runs','matches_odi']].copy()
    q19['avg_runs'] = q19['career_total_runs'] / q19['matches_odi'].replace(0,1)
    q19['consistency_score'] = q19['avg_runs'] / q19['avg_runs'].std()
    st.dataframe(q19.sort_values('consistency_score',ascending=False).head(10))

    # 20. Matches per format + batting averages
    st.subheader("2️⃣0️⃣ Matches per Format + Batting Averages")
    q20 = players_df[['full_name','matches_test','matches_odi','matches_t20i','batting_average_test','batting_average_odi','batting_average_t20i']]
    q20 = q20[(q20[['matches_test','matches_odi','matches_t20i']].sum(axis=1) >= 20)]
    st.dataframe(q20)

    # 21. Player ranking system
    st.subheader("2️⃣1️⃣ Player Performance Ranking")
    df = players_df.copy()
    df['batting_points'] = (df['career_total_runs']*0.01)+(df['batting_average_odi']*0.5)+(df['strike_rate_odi']*0.3)
    df['bowling_points'] = (df['career_total_wickets']*2)+((50 - df['bowling_average_odi'])*0.5)+((6 - df['economy_odi'])*2)
    df['fielding_points'] = (df['catches']*3)+(df['stumpings']*5)
    df['total_score'] = df['batting_points']+df['bowling_points']+df['fielding_points']
    q21 = df[['full_name','total_score']].sort_values('total_score',ascending=False)
    st.dataframe(q21.head(10))

    # 22. Head-to-head summary (simplified)
    st.subheader("2️⃣2️⃣ Head-to-Head Summary (Simplified)")
    q22 = matches_df.groupby(['team1_name','team2_name'])['Match_Winner'].count().reset_index()
    q22.columns = ['team1','team2','matches_played']
    st.dataframe(q22)

    # 23. Recent player form (approx using last few rows)
    st.subheader("2️⃣3️⃣ Recent Player Form")
    recent_players = players_df.sort_values('played_since_year',ascending=False).head(10)
    st.dataframe(recent_players[['full_name','career_total_runs','strike_rate_odi']])

    # 24. Best batting partnerships (placeholder)
    st.subheader("2️⃣4️⃣ Best Batting Partnerships")
    st.info("Detailed partnerships data not available, displaying placeholder with match_id + teams.")
    st.dataframe(matches_df[['match_id','Teams','match_description']].head(10))

    # 25. Time series performance evolution
    st.subheader("2️⃣5️⃣ Player Performance Over Time")
    st.info("Quarterly performance data not available – showing overall trend using played_since_year.")
    q25 = players_df.groupby('played_since_year')['career_total_runs'].mean().reset_index()
    st.line_chart(q25.set_index('played_since_year'))
