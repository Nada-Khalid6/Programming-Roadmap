# This is Arabic comment
# This is another Arabic comment

import streamlit as st

# Your existing code...

if "session_state" in st.session_state:
    del st.session_state["session_state"]  # Safety check before deletion

# Link button adjustment
st.link_button("Your Button Text")