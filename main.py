import streamlit as st

# Importing the Nanum Gothic font from Google Fonts
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
    <style>
    .css-18e3th9, .css-1d391kg {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    .full-width-banner {
        background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)), 
                    url('https://ifh.cc/g/lD0gY1.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 500px;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        display: flex;
        align-items: flex-end;
        justify-content: center;
        color: white;
        position: relative;
        z-index: 1;
        font-family: 'Nanum Gothic', sans-serif;
    }

    .full-width-banner h1 {
        font-size: 3em;
        margin: 0;
        padding: 20px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    header, footer, .css-1lsmgbg {
        visibility: hidden;
        height: 0px;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the full-width banner
st.markdown(
    """
    <div class="full-width-banner">
        <h1>Welcome to My Streamlit App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sample content
st.write("This is the content of the app below the banner.")
st.write("You can add more Streamlit components here.")