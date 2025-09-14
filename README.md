🏏 Cricbuzz Player Stats Analysis Project
✅ Project Purpose

This project converts detailed cricket player performance data from a nested JSON format into a flat CSV format.
It is designed to enable easier analysis and visualization using tools like Pandas and Streamlit.

⚡ Features

Converts nested JSON to structured CSV.

Handles missing or malformed data gracefully.

Uses Pandas for data manipulation.

Prepares the dataset for future interactive analysis or visualization in Streamlit.

📁 Folder Structure
cricbuzz_analysis_project/
│
├── data/
│   ├── input_data.json      # Raw JSON file with player stats
│   ├── output_data.csv      # Flattened CSV file generated from JSON
│
├── app.py                   # Streamlit dashboard (optional)
├── json_to_csv.py           # Script to convert JSON → CSV
├── requirements.txt         # Required Python libraries
├── README.md                # This file
└── .gitignore                # Optional (to ignore data files in git)

✅ Prerequisites

Python 3.10 or newer

Pip package manager

🚀 Installation & Setup

Clone the repository (if applicable):

git clone https://github.com/your-repo/cricbuzz_analysis_project.git
cd cricbuzz_analysis_project


Install required Python packages:

pip install -r requirements.txt

⚙️ Running the Conversion Script

Place your input JSON file inside the data/ folder (e.g., input_data.json).

Run the conversion script:

python json_to_csv.py


Output:

A file data/output_data.csv will be generated containing flattened player stats.

🌟 Running the Streamlit Dashboard (Optional)

Once the data is converted, you can launch the Streamlit app for visualization.

streamlit run app.py

✅ Example Input (JSON)
{
    "DA Warner": {
        "op_team": {
            "Royal Challengers Bengaluru": {
                "Bt_Runs": 307,
                "Bt_Balls": 202,
                "Bw_Runs": 0,
                "Bw_Balls": 0,
                "Matches": 10,
                "Bw_economy": 0,
                "Bt_Strike rate": 151.98,
                "Bt_Avg": 30.7,
                "Bt_Runs_list": [14, 100, 8],
                "Bt_Balls_list": [9, 55, 6]
            }
        }
    }
}

✅ Example Output (CSV)
player_name	opponent_team	Bt_Runs	Bt_Balls	Bw_Runs	Bw_Balls	Matches	Bw_economy	Bt_Strike_rate	Bt_Avg	Bt_Runs_list	Bt_Balls_list
DA Warner	Royal Challengers Bengaluru	307	202	0	0	10	0	151.98	30.7	[14,100,8]	[9,55,6]
✅ Notes

Ensure your JSON structure follows the expected hierarchy:
{ player_name → op_team → opponent_team → stats }

The script uses default encoding (ISO-8859-1) to avoid Unicode errors.

🛠️ Future Enhancements

Add CLI arguments to specify input and output files.

Integrate automated unit tests.

Build advanced visualizations in Streamlit (e.g., charts, filters).