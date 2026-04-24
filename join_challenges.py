from query_runner import run_query


join_challenges = [
    {
        "prompt": "run a query that joins the players table and the player_stats table. return only the name of the player and their goals",
        "hint": "think about what column links the two tables",
        "solution": "SELECT players.name, player_stats.goals FROM player_stats JOIN players ON player_stats.player_id=players.player_id"
    },
    {
        "prompt": "run a query that joins all three tables together",
        "hint": "what column(s) ties all three tables together?",
        "solution": "SELECT players.*, games.*, player_stats.* FROM players JOIN player_stats ON player_stats.player_id=players.player_id JOIN games ON player_stats.game_id=games.game_id"
    },
    {
        "prompt": "run a query that joins the players_stats table and games table that returns only games played on 2026-04-18",
        "hint": "utilize the WHERE clause after joining the tables",
        "solution": "SELECT games.*, player_stats.* FROM games JOIN player_stats ON games.game_id=player_stats.game_id WHERE games.date_played = '2026-04-18'"
    }
]

def run_join_challenges():
    for index, challenge in enumerate(join_challenges):
        prompts = challenge.get("prompt")
        hints = challenge.get("hint")
        solutions = challenge.get("solution")
        question_number = index + 1
        print(f"Challenge #{question_number}: {prompts}")
        print(f"{hints}")
        user_input = input("Please enter your query: ")
        run_query(user_input)
        user_input = user_input.strip()
        if user_input.upper().replace('"',"'") == solutions.upper().replace('"',"'"):
            if question_number < len(join_challenges):
                print("Correct! Moving to next challenge")
            else:
                print("Great job! You've completed all the challenges.")
        else:
            print(f"Not quite. The correct solution is: {solutions}")

if __name__ == "__main__":
    run_join_challenges()