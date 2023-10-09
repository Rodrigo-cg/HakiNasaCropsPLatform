import streamlit as st

def app():
    st.subheader('Search for images related to the crop you want')

    # Campo de búsqueda con valor por defecto "quinoa"
    search_query = st.text_input("Enter crop name:", "quinoa")

    if st.button("Search"):
        # Aquí puedes agregar la lógica para buscar imágenes relacionadas con el cultivo
        # En este ejemplo, se muestran imágenes locales relacionadas con la quinoa
        if search_query.lower() == "quinoa":
            # Rutas locales de las imágenes de quinoa
            quinoa_images = [
                "image1.png",
                "image2.png",
                "image3.png",
            ]

            # Mostrar las imágenes locales con un ancho máximo de 500 píxeles
            for image_path in quinoa_images:
                st.image(image_path, caption="Quinoa Image", width=500)

if __name__ == "__main__":
    app()
