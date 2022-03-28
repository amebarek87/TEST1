# -------------------------------------------------------
# Streamlit demo program to handle multiple pages with widget state
# preservation.
# Page selection: Buttons on the page top.
#
# Ray J.
# -------------------------------------------------------

import streamlit as st

# --- I don't understand the necessity of this line. But it is needed
#    to preserve session_state in the cloud. Not locally.
# st.session_state.update(st.session_state)

# --- Init session_state
if 'active_page' not in st.session_state:
    st.session_state.active_page = 'Home'
    st.session_state.slider1 = 0
    st.session_state.slider2 = 0
    # st.session_state.MyForm = 0
    st.session_state.check1 = False
    st.session_state.check2 = False

st.session_state.active_page = st.session_state.active_page
st.session_state.slider1 = st.session_state.slider1
st.session_state.check1 = st.session_state.check1
st.session_state.slider2 = st.session_state.slider2
st.session_state.check2 = st.session_state.check2


# --- Callback functions
def CB_HomeButton():
    st.session_state.active_page = 'Home'


def CB_SliderButton():
    st.session_state.active_page = 'Slider'


def CB_ContactButton():
    st.session_state.active_page = 'Contact'


# --- Payload code of each page
def home():
    st.write('Welcome to home page')
    link = '[GitHub](http://github.com)'
    st.markdown(link, unsafe_allow_html=True)
    st.checkbox('Check me', key='check1')
    if st.button('Click Home'):
        st.write('Welcome to home page')


def slider():
    st.write('Welcome to the slider page')
    slide1 = st.slider('this is a slider', min_value=0, max_value=15, key='slider1')
    st.write('Slider position:', slide1)


def contact():
    st.title('Welcome to contact page')
    st.write(f'Multipage app. Streamlit {st.__version__}')
    if st.button('Click Contact'):
        st.write('Welcome to contact page')
    with st.form(key='MyForm', clear_on_submit=False):
        st.write("Inside the form")
        slider_val = st.slider("Form slider", key='slider2')
        checkbox_val = st.checkbox("Form checkbox", key='check2')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")


# --- Page selection buttons
col1, col2, col3 = st.columns(3)
col1.button('Home', on_click=CB_HomeButton)
col2.button('Slider', on_click=CB_SliderButton)
col3.button('Contact', on_click=CB_ContactButton)

# --- Run the active page
if st.session_state.active_page == 'Home':
    home()
elif st.session_state.active_page == 'Slider':
    slider()
elif st.session_state.active_page == 'Contact':
    contact()
