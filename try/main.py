import streamlit as st
from streamlit_option_menu import option_menu
import about, explore_datasets, my_crop, explore_crops

st.set_page_config(
    page_title="Pondering",
    layout="wide"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Haki Nasa Crops',
                options=['about', 'explore datasets', 'explore crops', 'my crops', ],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "10px", "background-color": 'black'},
                    "menu-title": {"color": "#02ab21", "font-size": "23px"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "about":
            about.app()
        if app == "explore datasets":
            explore_datasets.app()
        if app == "explore crops":
            explore_crops.app()
        if app == 'my crops':
            my_crop.app()

MultiApp().run()