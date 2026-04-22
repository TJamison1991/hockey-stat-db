# Hockey Stats Database

This project is meant to act as a query tool for writing SELECT queries only. This project contains three challenge questions that help teach the user how to run basic queries. The tables contain hockey players and stats.

## Features
- Contains a menu system
- Custom query runner
- Security blocking non-SELECT queries
- Results displayed as formatted tables

## Project Structure
```
hockey-stats-db/
├── app.py
├── database.py
├── seed.py
├── query_runner.py
├── challenges.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── practice.db
└── sample_data/
    ├── games.csv
    ├── players.csv
    └── player_stats.csv
```
## How To Install And Run
- Clone the repo from GitHub
    git clone <repository-url>
- Navigate to hockey-stats-db
- Install dependencies
    pip install -r requirements.txt
- Set up the database
    python database.py
- Seed the data
    python seed.py
- Run the app
    python app.py

## Technologies Used
- Python 3
- SQLite - database storage
- pandas - data loading and display

## What I Learned
I learned how to set up securities to ensure only SELECT queries are allowed. I'm also learning to write better README documents. I used this project to strengthen my knowledge of while loops. Throughout this project, I also learned how to better set up a repo structure to help myself remain organized. When creating the databases specifically, I learned how to set up FOREIGN KEYS. I also learned how to set up bridges to all tables using game_id and player_id. For this project specifically, I used real hockey stats and players from the 2026 NHL playoffs. In the future, I would like to add JOINS to combine the players with their stats. I could also use this addition to strengthen my understanding of how to write JOINS and how they work.