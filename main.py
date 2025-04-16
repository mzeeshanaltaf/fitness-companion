import streamlit as st
from util import *

# Page title of the application
page_title = "NutriFit"
page_icon = "🏋️"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

if "user_profile" not in st.session_state:
    st.session_state.user_profile = None

# Application Title and description
st.title(f'{page_title}{page_icon}')
st.write('***:blue[Fuel Your Goals, Transform Your Body! 🏋️♂️🍏]***')
st.write("""
NutriFit is your all-in-one fitness companion! 💪 Simply input your profile (weight, height, gender) and your 
goal—whether it's weight loss ⚖️, muscle gain 🏋️, or fat loss 🔥—and get a personalized nutrition & workout plan 
tailored just for you!

🔹 Get your daily calorie needs

🔹 Balanced macros: Carbs 🍞, Proteins 🍗, Fats 🥑

🔹 Personalized exercise routines based on your fitness level 🏋️‍♀️

🔹 Progress tracking and motivational nudges to keep you going 🚀

Whether you're just starting out or leveling up your fitness journey, NutriFit has your back. Start your transformation today! 🌟

""")
# Display footer in the sidebar
display_footer()

st.subheader('Configuration:')
col1, col2, col3 = st.columns([0.3, 0.3, 0.4], border=True)
with col1:
    st.subheader('User Profile:🧑‍💻', divider='gray')
    user_profile_button = st.button("Set Your Profile", icon=":material/account_circle:")
    if user_profile_button:
        set_user_profile()
with col2:
    st.subheader('Fitness Goal:🎯', divider='gray')
    fitness_goal = st.selectbox('Fitness Goal ', ['💪Muscle Gain', '🏃‍♂️Weight Loss', '🥵Fat Loss', '🏋️Endurance'],
                                       placeholder='Select the Gender', help='Select the Gender',
                                       label_visibility="collapsed")
with col3:
    st.subheader('Notes:📝', divider='gray')
    notes = st.text_input('Notes', value=None, placeholder='Any medical condition or notes', max_chars=200,
                          label_visibility="collapsed")


button = st.button("Generate Plan", type='primary', icon=":material/fitness_center:")

if button:
    with st.spinner('Processing ...', show_time=True):
        st.subheader('Calories & Macronutrients🌾🥩🥑:', divider='gray')
        calories = 2500
        carbs = 300
        protein = 150
        fat = 70
        col1, col2, col3, col4 = st.columns(4, border=True)
        with col1:
            st.metric('Calories', f'{calories:,}')
        with col2:
            st.metric('Carbs🌾', f'{carbs}g')
        with col3:
            st.metric('Protein🥩', f'{protein}g')
        with col4:
            st.metric('Fat🥑', f'{fat}g')




