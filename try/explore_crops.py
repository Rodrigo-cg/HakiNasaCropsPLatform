import streamlit as st
import awesome_streamlit as ast
from PIL import Image
import time
import pandas as pd
import random

def generate_random_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def app():
    if 'image' not in st.session_state:
        st.session_state.image = None
        
    st.title('Explore the crops near you')

    search_query = st.text_input("Enter an address to search for crops nearby", "Cholocal, Cajamarca Perú")
    
    image_path_filter = 'crops2.png'
    image_path_no_filter = 'cropSinRelleno.png'

    col1, col2 = st.columns(2)
    
    if col2.button("Search without Filters"):
        st.write(f'<div style="margin-bottom: 100px;">16 crops near you {search_query}</div>', unsafe_allow_html=True)

        image_path = image_path_no_filter  # Cambiar la ruta de la imagen

        image = Image.open(image_path)

        st.image(image, caption='Sunrise by the mountains', use_column_width=False, output_format="PNG")
        st.session_state.image = image

        time.sleep(3)

        subheader_with_formatting = '<div style="margin-top: 20px; font-weight: bold;">Nearest 16 crops dataset</div>'
        st.markdown(subheader_with_formatting, unsafe_allow_html=True)
        pd.options.display.float_format = '{:,.0f}'.format

        df = pd.read_csv('dataCrops.csv', dtype={'ID Cultivation': int})
        
        df.insert(0, 'Contact Number', [generate_random_phone_number() for _ in range(len(df))])

        st.dataframe(df.style.format(thousands="", precision=0), height=500, width=3000, use_container_width=True)
        
        column_names = {
            'Contact Number': 'Contact Number',
            'ID Cultivation': 'ID Cultivation',
            'Type of Crop': 'Type of Crop',
            'Crop Yield': 'Crop Yield',
            'pH': 'pH',
            'Nitrogen N': 'Nitrogen N',
            'Potassium K': 'Potassium K',
            'Phosphorus P': 'Phosphorus P',
            'Organic Matter': 'Organic Matter',
            'Soil Texture': 'Soil Texture',
            'Humidity': 'Humidity',
            'Crop Rotation Number': 'Crop Rotation Number',
            'Fungal Material': 'Fungal Material',
            'Algal Material': 'Algal Material',
            'Earthworm Material': 'Earthworm Material',
            'Altitude': 'Altitude',
            'Latitude': 'Latitude',
            'Longitude': 'Longitude'
        }

        column_elements = {column: st.sidebar.empty() for column in df.columns}
        
        row_index = 0

        while True:
            row_data = "<br>".join([f"**{column_names[column]}:** {df.iloc[row_index][column]}" for column in df.columns])
            
            for column in df.columns:
                column_elements[column].markdown(row_data, unsafe_allow_html=True)

            row_index = (row_index + 1) % len(df)

            time.sleep(5)
    
    if col1.button("Search with filter", key="search_button"):
        st.write(f'<div style="margin-bottom: 100px;">16 crops near you {search_query}</div>', unsafe_allow_html=True)

        image_path = image_path_filter  # Usar la ruta de la imagen con filtro

        image = Image.open(image_path)

        st.image(image, caption='Sunrise by the mountains', use_column_width=False, output_format="PNG")
        st.session_state.image = image

        time.sleep(3)

        subheader_with_formatting = '<div style="margin-top: 20px; font-weight: bold;">Nearest 16 crops dataset</div>'
        st.markdown(subheader_with_formatting, unsafe_allow_html=True)
        pd.options.display.float_format = '{:,.0f}'.format

        df = pd.read_csv('dataCrops.csv', dtype={'ID Cultivation': int})
        
        df.insert(0, 'Contact Number', [generate_random_phone_number() for _ in range(len(df))])

        st.dataframe(df.style.format(thousands="", precision=0), height=500, width=3000, use_container_width=True)
        
        column_names = {
            'Contact Number': 'Contact Number',
            'ID Cultivation': 'ID Cultivation',
            'Type of Crop': 'Type of Crop',
            'Crop Yield': 'Crop Yield',
            'pH': 'pH',
            'Nitrogen N': 'Nitrogen N',
            'Potassium K': 'Potassium K',
            'Phosphorus P': 'Phosphorus P',
            'Organic Matter': 'Organic Matter',
            'Soil Texture': 'Soil Texture',
            'Humidity': 'Humidity',
            'Crop Rotation Number': 'Crop Rotation Number',
            'Fungal Material': 'Fungal Material',
            'Algal Material': 'Algal Material',
            'Earthworm Material': 'Earthworm Material',
            'Altitude': 'Altitude',
            'Latitude': 'Latitude',
            'Longitude': 'Longitude'
        }

        column_elements = {column: st.sidebar.empty() for column in df.columns}
        
        row_index = 0

        while True:
            row_data = "<br>".join([f"**{column_names[column]}:** {df.iloc[row_index][column]}" for column in df.columns])
            
            for column in df.columns:
                column_elements[column].markdown(row_data, unsafe_allow_html=True)

            row_index = (row_index + 1) % len(df)

            time.sleep(5)
        
if __name__ == "__main__":
    app()
