import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="IPL 2025 Final - RCB vs PBKS",
    page_icon="🏏",
    layout="wide"
)

def show_live_matches():
    # Refresh button in top-right corner
    st.markdown(
        """
        <style>
        .refresh-button {
            position: fixed;
            top: 1rem;
            right: 1rem;
            z-index: 1000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("🔄 Refresh", key="refresh_button", help="Click to refresh the page"):
        st.success("Refresh for Live Updates")

    st.title("🏆 IPL, Royal Challengers Bangalore vs Punjab Kings")
    st.markdown("---")

    # Match Summary
    st.info("""
    **📅 Date:** June 3, 2025  
    **🏟️ Venue:** Narendra Modi Stadium, Ahmedabad  
    **🎲 Toss Winner:** PBKS (elected to field first)  
    **👑 Player of the Match:** Krunal Pandya (RCB) – 4 (5) & 2/17 (4 overs)  
    **⭐ Player of the Series:** Suryakumar Yadav (MI)
    """)
    st.success("🏆 RCB WON BY 6 RUNS 🏆")
    st.balloons()

    st.markdown("---")
    st.header("📋 Overall Scorecard Summary")

    # Overall team scores
    st.markdown("**Royal Challengers Bangalore**: 190/9 in 20 overs")
    st.markdown("**Punjab Kings**: 184/7 in 20 overs")

    st.markdown("---")
    st.header("📝 Detailed Scorecard")

    # Batting DataFrames
    rcb_batting = {
        'Batsman': ['Phil Salt', 'Virat Kohli', 'Mayank Agarwal', 'Rajat Patidar', 'Liam Livingstone',
                    'Jitesh Sharma', 'Romario Shepherd', 'Krunal Pandya', 'Bhuvneshwar Kumar', 'Yash Dayal'],
        'Runs': [16, 43, 24, 26, 25, 24, 17, 4, 1, 1],
        'Balls': [9, 35, 18, 16, 15, 10, 9, 5, 2, 1],
        '4s': [2, 3, 2, 1, 0, 2, 1, 0, 0, 0],
        '6s': [1, 0, 1, 2, 2, 2, 1, 0, 0, 0],
        'SR': [177.78, 122.86, 133.33, 162.50, 166.67, 240.00, 188.89, 80.00, 50.00, 100.00]
    }

    pbks_batting = {
        'Batsman': ['Priyansh Arya', 'Prabhsimran Singh', 'Josh Inglis', 'Shreyas Iyer', 'Nehal Wadhera',
                    'Shashank Singh', 'Marcus Stoinis', 'Azmatullah Omarzai', 'Kyle Jamieson'],
        'Runs': [24, 26, 39, 1, 15, 61, 6, 1, 0],
        'Balls': [19, 22, 23, 2, 18, 30, 2, 2, 2],
        '4s': [4, 0, 1, 0, 0, 3, 0, 0, 0],
        '6s': [0, 2, 4, 0, 1, 6, 1, 0, 0],
        'SR': [126.32, 118.18, 169.57, 50.00, 83.33, 203.33, 300.00, 50.00, 0.00]
    }

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Royal Challengers Bangalore Batting")
        st.dataframe(pd.DataFrame(rcb_batting), use_container_width=True)
    with col2:
        st.subheader("Punjab Kings Batting")
        st.dataframe(pd.DataFrame(pbks_batting), use_container_width=True)

    # Bowling DataFrames
    rcb_bowling = {
        'Bowler': ['Bhuvneshwar Kumar', 'Yash Dayal', 'Josh Hazlewood', 'Krunal Pandya', 'Suyash Sharma', 'Romario Shepherd'],
        'Overs': [4, 3, 4, 4, 2, 3],
        'Runs': [38, 18, 54, 17, 19, 30],
        'Wickets': [2, 1, 1, 2, 0, 1],
        'Econ': [9.50, 6.00, 13.50, 4.30, 9.50, 10.00]
    }

    pbks_bowling = {
        'Bowler': ['Arshdeep Singh', 'Kyle Jamieson', 'Azmatullah Omarzai', 'Vyshak Vijaykumar', 'Yuzvendra Chahal'],
        'Overs': [4, 4, 4, 4, 4],
        'Runs': [40, 48, 35, 30, 37],
        'Wickets': [3, 3, 1, 1, 1],
        'Econ': [10.00, 12.00, 8.80, 7.50, 9.30]
    }

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("RCB Bowling Performance")
        st.dataframe(pd.DataFrame(rcb_bowling), use_container_width=True)
    with col2:
        st.subheader("PBKS Bowling Performance")
        st.dataframe(pd.DataFrame(pbks_bowling), use_container_width=True)

    st.markdown("---")
    st.header("📊 Runs Per Over Comparison")

    rcb_runs = [15, 12, 18, 14, 17, 9, 21, 10, 12, 16]
    pbks_runs = [13, 18, 22, 8, 25, 30, 10, 5, 3, 4]
    overs = list(range(1, 11))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(overs, rcb_runs, label="RCB", marker='o', color='red', linewidth=2.5)
    ax.plot(overs, pbks_runs, label="PBKS", marker='s', color='blue', linewidth=2.5)
    ax.set_xlabel('Over')
    ax.set_ylabel('Runs')
    ax.set_title('Runs per Over - IPL 2025 Final')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

    st.markdown("---")
    st.markdown("## 🎉 CELEBRATIONS TIME! 🎉")
    st.image("https://www.pngitem.com/pimgs/m/27-272594_trophy-png-transparent-images-trophy-cup-png-png.png", width=150)
    st.success("""
    ### Royal Challengers Bangalore lift the IPL Trophy!  
    """)

if __name__ == "__main__":
    show_live_matches()


