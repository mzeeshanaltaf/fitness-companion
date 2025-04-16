import streamlit as st

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