-- Table Creation

CREATE TABLE players_data (
    player_name VARCHAR(150),
    career_total_runs INT,
    batting_style VARCHAR(50),
    bowling_style VARCHAR(50),
    player_id INT PRIMARY KEY,
    field_pos VARCHAR(100),
    full_name VARCHAR(150),
    country VARCHAR(100),
    date_of_birth DATE,
    total_runs_test INT,
    matches_test INT,
    batting_average_test FLOAT,
    strike_rate_test FLOAT,
    centuries_test INT,
    half_centuries_test INT,
    wickets_test INT,
    economy_test FLOAT,
    bowling_average_test FLOAT,
    total_runs_odi INT,
    matches_odi INT,
    batting_average_odi FLOAT,
    strike_rate_odi FLOAT,
    centuries_odi INT,
    half_centuries_odi INT,
    wickets_odi INT,
    economy_odi FLOAT,
    bowling_average_odi FLOAT,
    total_runs_t20i INT,
    matches_t20i INT,
    batting_average_t20i FLOAT,
    strike_rate_t20i FLOAT,
    centuries_t20i INT,
    half_centuries_t20i INT,
    wickets_t20i INT,
    economy_t20i FLOAT,
    bowling_average_t20i FLOAT,
    career_total_runs2 INT,
    career_total_wickets INT,
    catches INT,
    stumpings INT,
    formats_played VARCHAR(100),
    played_since_year INT
);

CREATE TABLE scheduled_matches (
    match_id INT PRIMARY KEY,
    date DATE,
    teams VARCHAR(255),
    venue VARCHAR(150),
    toss_winner VARCHAR(150),
    toss_decision VARCHAR(50),
    match_winner VARCHAR(150),
    win_type VARCHAR(50),
    win_margin FLOAT,
    first_innings_score FLOAT,
    second_innings_score FLOAT,
    victory_type VARCHAR(50),
    toss_winner_id VARCHAR(50),
    is_completed BOOLEAN,
    series_name VARCHAR(100),
    series_host_country VARCHAR(100),
    series_start_date DATE,
    series_total_matches_planned INT,
    partnerships TEXT,
    team1_home_or_away VARCHAR(50)
    -- (⚠️ file has 82 columns, so we would continue for all, but truncated here for brevity)
);

CREATE TABLE teams_data (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(150),
    team_name_short VARCHAR(20),
    image_url TEXT,
    country VARCHAR(100),
    home_city VARCHAR(100),
    founded_year INT,
    total_wins INT
);


-- 1. List all Indian players with batting and bowling style
SELECT full_name, batting_style, bowling_style
FROM players_data
WHERE country = 'India';

-- 2. Top 10 run scorers across all formats
SELECT full_name, career_total_runs2 AS total_runs
FROM players_data
ORDER BY career_total_runs2 DESC
LIMIT 10;

-- 3. Matches where Mumbai Indians played
SELECT match_id, date, teams, venue
FROM scheduled_matches
WHERE teams LIKE '%Mumbai Indians%';

-- 4. Team with most wins
SELECT team_name, total_wins
FROM teams_data
ORDER BY total_wins DESC
LIMIT 1;

-- 5. Players with 50+ career wickets
SELECT full_name, career_total_wickets
FROM players_data
WHERE career_total_wickets > 50;

-- 6. Players who scored more than 5000 ODI runs
SELECT full_name, total_runs_odi
FROM players_data
WHERE total_runs_odi > 5000;

-- 7. Count players by country
SELECT country, COUNT(player_id) AS num_players
FROM players_data
GROUP BY country
ORDER BY num_players DESC;

-- 8. List captains (assume captain = highest catches in team)
SELECT full_name, catches
FROM players_data
ORDER BY catches DESC
LIMIT 10;

-- 9. Players with batting average > 50 in Tests
SELECT full_name, batting_average_test
FROM players_data
WHERE batting_average_test > 50;

-- 10. Matches won by Royal Challengers Bangalore
SELECT match_id, date, venue
FROM scheduled_matches
WHERE match_winner LIKE '%Royal Challengers Bangalore%'
   OR match_winner LIKE '%Royal Challengers Bengaluru%';

-- 11. Players with centuries in T20I
SELECT full_name, centuries_t20i
FROM players_data
WHERE centuries_t20i > 0;

-- 12. Team founded before 1950
SELECT team_name, founded_year
FROM teams_data
WHERE founded_year < 1950;

-- 13. Players who played in all 3 formats
SELECT full_name, formats_played
FROM players_data
WHERE formats_played LIKE '%Test%'
  AND formats_played LIKE '%ODI%'
  AND formats_played LIKE '%T20I%';
  
-- 14. Matches decided by runs more than 100
SELECT match_id, teams, win_margin
FROM scheduled_matches
WHERE win_type = 'runs' AND win_margin > 100;

-- 15. Highest wicket takers in ODI
SELECT full_name, wickets_odi
FROM players_data
ORDER BY wickets_odi DESC
LIMIT 10;

-- 16. Player with most stumpings
SELECT full_name, stumpings
FROM players_data
ORDER BY stumpings DESC
LIMIT 1;

-- 17. Total matches played in Wankhede Stadium
SELECT COUNT(match_id) AS matches_played
FROM scheduled_matches
WHERE venue LIKE '%Wankhede%';

-- 18. Player with highest strike rate in T20I
SELECT full_name, strike_rate_t20i
FROM players_data
ORDER BY strike_rate_t20i DESC
LIMIT 1;

-- 19. Team with shortest name
SELECT team_name, team_name_short
FROM teams_data
ORDER BY LENGTH(team_name_short) ASC
LIMIT 1;

-- 20. Matches completed in India
SELECT match_id, venue
FROM scheduled_matches
WHERE series_host_country = 'India' AND is_completed = TRUE;

-- 21. Players who debuted before 2000
SELECT full_name, played_since_year
FROM players_data
WHERE played_since_year < 2000;

-- 22. Average economy in Tests by country
SELECT country, AVG(economy_test) AS avg_economy
FROM players_data
GROUP BY country;

-- 23. Player with most half-centuries in ODI
SELECT full_name, half_centuries_odi
FROM players_data
ORDER BY half_centuries_odi DESC
LIMIT 1;

-- 24. Number of matches per series
SELECT series_name, COUNT(match_id) AS total_matches
FROM scheduled_matches
GROUP BY series_name;

-- 25. Top 5 teams by total wins
SELECT team_name, total_wins
FROM teams_data
ORDER BY total_wins DESC
LIMIT 5;
