import streamlit as st
import pandas as pd
import requests
import json

# Custom formatting function
def format_text(text):
    if not isinstance(text, str):
        return text

    # Preserve known abbreviations (add more as needed)
    abbreviations = {'HIIT': 'HIIT', '60S': '60s'}

    # Replace underscores with spaces and title case
    formatted = text.replace('_', ' ').title()

    # Handle special cases
    for original, replacement in abbreviations.items():
        formatted = formatted.replace(original.title(), replacement)

    return formatted

@st.dialog("User Profile")
def set_user_profile():
    gender = st.selectbox('Gender:', ['Male', 'Female',],
                                       placeholder='Select the Gender', help='Select the Gender',
                                       label_visibility="visible")
    weight = st.number_input("Enter Your Weight (in kg):", value=80, min_value=30, max_value=200,
                             placeholder='Enter Your Weight (in Kg)', help= 'Enter Your Weight')
    height = st.number_input("Enter Your Height (in cm):", value=180, min_value=100, max_value=215,
                             placeholder='Enter Your Height', help= 'Enter Your Height')
    age = st.slider('Select Your Age:', 15, 90, 30, help= 'Select Your Age')

    if st.button('Submit'):
        st.session_state.user_profile = {"gender": gender, "weight": weight, "height": height, "age": age}
        st.rerun()

def langflow_fitness_plan_generator(user_profile, fitness_goal, notes):
    # The complete API endpoint URL for this flow
    url = f"https://api.langflow.astra.datastax.com/lf/{st.secrets['LANGFLOW_API_EP']}"

    # Request payload configuration
    payload = {
        "output_type": "chat",  # Specifies the expected output format
        "input_type": "text",  # Specifies the input format,
        "tweaks": {
        "TextInput-6Zbvg": {
            "input_value": f"{fitness_goal}"
        },
        "TextInput-HKYL9": {
            "input_value": f"Weight: {user_profile['weight']}kg, height: {user_profile['height']}cm, gender: {user_profile['gender']}, age:{user_profile['age']}"
        },
        "TextInput-xKCGx": {
            "input_value": f"{notes}"
        }
    }  # Custom tweaks to modify flow behavior
    }

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['LANGFLOW_APPLICATION_TOKEN']}"  # Authentication key from environment variable
    }

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        message = json.loads(response.text)
        result = json.loads(message['outputs'][0]['outputs'][0]['results']['message']['data']['text'])['results'][0]

        calorie_macronutrient_requirements = result['calorie_macronutrient_requirements']
        daily_workout_routine = result['daily_workout_routine']
        additional_notes = result['additional_notes']
        motivational_quote = result['motivational_quote']

        return calorie_macronutrient_requirements, daily_workout_routine, additional_notes, motivational_quote

    except requests.exceptions.RequestException as e:
        st.exception(f"Error making API request: {e}")
    except ValueError as e:
        st.exception(f"Error parsing response: {e}")

def display_workout_routine(workout_routine):
    # Create columns for each day
    cols = st.columns(len(workout_routine), border=False)

    for i, (day, routine) in enumerate(workout_routine.items()):
        with cols[i]:
            st.subheader(f"DAY {i + 1}")

            # Convert to DataFrame and format both index and values
            df = pd.DataFrame.from_dict(routine, orient='index', columns=['Details'])

            # Format columns
            df.index = df.index.map(format_text)
            df['Details'] = df['Details'].apply(format_text)

            # Display the table
            st.dataframe(
                df,
                use_container_width=True,
                column_config={
                    "Details": st.column_config.TextColumn()
                }
            )

def display_tips(tips):

    # Convert dictionary values to bullet points
    bullet_points = "\n".join([f"* {value.title()}" for value in tips.values()])
    st.markdown(bullet_points)

def display_motivational_quote(quote):
    st.success("***" + quote + "***")

def display_footer():
    footer = """
    <style>
    /* Ensures the footer stays at the bottom of the sidebar */
    [data-testid="stSidebar"] > div: nth-child(3) {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }

    .footer {
        color: grey;
        font-size: 15px;
        text-align: center;
        background-color: transparent;
    }
    </style>
    <div class="footer">
    Made with ❤️ by <a href="mailto:zeeshan.altaf@gmail.com">Zeeshan</a>.
    </div>
    """
    st.sidebar.markdown(footer, unsafe_allow_html=True)