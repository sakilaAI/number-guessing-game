import streamlit as st
import random

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 10)
    st.session_state.attempts = 0

st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 10. Can you guess it?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning("Too low!")
    elif guess > st.session_state.number:
        st.warning("Too high!")
    else:
        st.success(f"You guessed it right in {st.session_state.attempts} attempts! 🎉")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 10)
            st.session_state.attempts = 0
