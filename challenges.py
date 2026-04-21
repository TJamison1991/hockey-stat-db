from query_runner import run_query

# build challenges dictionary
challenges = [
    {
        "prompt": "run a sql query that returns all players.",
        "hint": "in sql, * means ALL.",
        "solution": "SELECT * FROM players"
    },
    {   
        "prompt": "run a query that returns only games played on 2026-04-19",
        "hint": "here we want to introduce the WHERE clause",
        "solution": "SELECT * FROM games WHERE date_played = '2026-04-19'"
    },
    {   
        "prompt": "run a query that returns only players with 2 or more points.",
        "hint": "here we can utilize operands like > or <.",
        "solution": "SELECT * FROM player_stats WHERE points >= 2"
    }
]

def run_challenges():
    for index, challenge in enumerate(challenges):
        prompts = challenge.get("prompt")
        hints = challenge.get("hint")
        solutions = challenge.get("solution")
        question_number = index + 1
        print(f"Challenge #{question_number}: {prompts}")
        print(f"{hints}")
        user_input = input("Please input your query: ")
        run_query(user_input)
        user_input = user_input.strip()
        if user_input.upper().replace('"', "'") == solutions.upper().replace('"', "'"):
            if question_number < len(challenges):
                print("Correct! Moving to the next challenge...")
            else:
                print("Great job! All challenges complete.")
        else:
            print(f"Not quite. The correct query was: {solutions}")

if __name__ == "__main__":
    run_challenges()