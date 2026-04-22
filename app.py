from query_runner import run_query
from challenges import run_challenges

running = True
menu_list = ["1. Run a query", "2. Take a challenge", "3. Exit"]

while running:
    print("\n---MENU---")
    print(*menu_list, sep="\n")
    user_input = input("Please make a selection: ")
    if user_input == "1":
        query = input("Please input your query using SELECT only: ")
        run_query(query)
    elif user_input == "2":
        run_challenges()
    elif user_input == "3":
        print("Goodbye")
        break
    else:
        print("Please make a valid selection.")