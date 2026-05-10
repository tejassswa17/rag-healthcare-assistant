from src.workflow.graph import app

print("Healthcare Assistant Chatbot")
print("Type 'exit' to quit.\n")

# Conversation thread
config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

while True:

    query = input("You: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    feedback = ""

    retry_count = 0

    while True:

        # Invoke graph
        result = app.invoke(
            {
                "query": query,
                "feedback": feedback,
                "chat_history": "",
                "retry_count": retry_count
            },
            config=config
        )

        print("\nBot:\n")
        print(result["answer"])

        # Ask review
        review = input("\nWas this answer helpful? (yes/no): ")

        # End if satisfied
        if review.lower() == "yes":
            break

        # Retry limit
        if retry_count >= 2:

            print(
                "\nBot:\n"
                "I don't have additional relevant medical "
                "information to improve the answer further."
            )

            break

        # Prepare refinement
        feedback = (
            "The answer was not clear enough. "
            "Please improve and refine it."
        )

        retry_count += 1

    print("\n-----------------------------------\n")