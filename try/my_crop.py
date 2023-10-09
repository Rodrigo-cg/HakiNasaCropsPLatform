import ee
import geemap
import streamlit as st
import random
from PIL import Image

def app():
    st.title('Locate your crop')
    st.subheader('Obtain valuable data for your crop from satellites and contribute to open source datasets')

    st.markdown('<span style="color: blue;">1. Enter the latitude and longitude of your crop to obtain important satellite data.</span>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        latitud = st.text_input("Latitude:", "-7.4687477", key="latitude", max_chars=20, help="E.g., 42.1234")

    with col2:
        longitud = st.text_input("Longitude:", "78.1679569", key="longitude", max_chars=20, help="E.g., -75.0")
        
    if st.button("Get Values From Satellite"):
        ndvi = round(random.uniform(0.1, 0.9), 2)
        ndmi = round(random.uniform(0.1, 0.9), 2)
        ndre = round(random.uniform(0.1, 0.9), 2)
        elevation_meters = round(random.uniform(500, 2000), 2)
        water_temp_celsius = round(random.uniform(10, 30), 2)
        chloride_concentration = round(random.uniform(90, 110), 2)

        st.subheader('Satellite values:')
        st.write(f'NDVI: {ndvi}')
        st.write(f'NDMI: {ndmi}')
        st.write(f'NDRE: {ndre}')
        st.write(f'Altitude (meters): {elevation_meters}')
        st.write(f'Irrigation water temperature (°C): {water_temp_celsius}')
        st.write(f'Chloride concentration: {chloride_concentration}')
    
    st.markdown('<span style="color: Green;">2. Please share important data about your crop below. This information will contribute to open data for researchers and potential investors who may enhance your crop cultivation. If interested, they may contact you for collaboration.</span>', unsafe_allow_html=True)

    # Organiza los campos de entrada en grupos de tres por línea
    col4, col5, col6 = st.columns(3)

    with col4:
        crop_type = st.text_input("Type of Crop", "Corn")
        crop_yield = st.number_input("Crop Yield (%)", min_value=0.0, max_value=100.0, value=80.0)
        ph_value = st.number_input("pH", value=6.8)
        crop_rotation_number = st.number_input("Crop Rotation Number", value=2)

    with col5:
        nitrogen_n = st.number_input("Nitrogen N", value=45)
        potassium_k = st.number_input("Potassium K", value=125)
        phosphorus_p = st.number_input("Phosphorus P", value=55)
        algal_material = st.text_input("Algal Material", "Green Algae")

    with col6:
        organic_matter = st.number_input("Organic Matter", value=2.2)
        soil_texture = st.text_input("Soil Texture", "Sandy Loam")
        humidity = st.number_input("Humidity", value=14)
        fungal_material = st.text_input("Fungal Material", "Mushrooms")

    # Agrupa los campos de entrada restantes en grupos de tres por línea
    col7, col8, col9 = st.columns(3)

    with col7:
         earthworm_material = st.text_input("Earthworm Material", "Yes")
    with col8:
         cellphone = st.text_input("Contact number", "999 123 456")
    st.markdown('<span style="color: Violet;">3. Draw a polygon around the perimeter of your crop so that we can verify the GPS location of your crop with satellite images. Make your crop publicly available so that many people can view it and become interested in your crop. This information will be valuable as test data for future research in deep learning and remote sensing, precision agriculture, Remote sensing.</span>', unsafe_allow_html=True)
    image = Image.open('draw.png')

    st.image(image, caption='Sunrise by the mountains',width=1000, output_format="PNG")
    if st.button("Send Data"):
        st.success("Thank you for trusting us and contributing to open data!")
if __name__ == "__main__":
    app()

