import streamlit as st
import random

# Function to start a new game
def start_new_game(range_start, range_end, max_attempts):
    random_number = random.randint(range_start, range_end)
    return random_number, max_attempts, 0  # random number, max attempts, current attempts

# Main function to run the app
def main():
    st.title("Number Guessing Game")

    # Set default values
    if 'random_number' not in st.session_state:
        st.session_state.random_number = None
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'max_attempts' not in st.session_state:
        st.session_state.max_attempts = None

    # User inputs for range and difficulty
    st.sidebar.header("Settings")
    range_start = st.sidebar.number_input("Start of range", value=1, min_value=1)
    range_end = st.sidebar.number_input("End of range", value=100, min_value=range_start)
    difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
    
    # Set max attempts based on difficulty
    if difficulty == "Easy":
        max_attempts = 10
    elif difficulty == "Medium":
        max_attempts = 7
    else:
        max_attempts = 5

    # Start a new game
    if st.sidebar.button("Start New Game"):
        st.session_state.random_number, st.session_state.max_attempts, st.session_state.attempts = start_new_game(range_start, range_end, max_attempts)
        st.session_state.guess = None
        st.success("New game started! Guess the number between {} and {}.".format(range_start, range_end))

    # User input for guessing the number
    if st.session_state.random_number is not None:
        st.subheader("Make a Guess")
        st.session_state.guess = st.number_input("Your guess", min_value=range_start, max_value=range_end, step=1)

        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            if st.session_state.guess < st.session_state.random_number:
                st.warning("Too low!")
            elif st.session_state.guess > st.session_state.random_number:
                st.warning("Too high!")
            else:
                st.success("Congratulations! You've guessed the number {} in {} attempts!".format(st.session_state.random_number, st.session_state.attempts))
                st.session_state.random_number = None  # Reset the game

            # Check if max attempts reached
            if st.session_state.attempts >= st.session_state.max_attempts and st.session_state.random_number is not None:
                st.error("You've reached the maximum attempts! The number was {}.".format(st.session_state.random_number))
                st.session_state.random_number = None  # Reset the game

    # Display number of attempts
    if st.session_state.random_number is not None:
        st.write("Attempts: {}/{}".format(st.session_state.attempts, st.session_state.max_attempts))

if __name__ == "__main__":
    main()