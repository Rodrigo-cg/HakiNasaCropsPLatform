import streamlit as st

def app():
    # Set the title and logo
    st.title("About HakiNasaCrops")
    st.image("logo2.jpg", use_column_width=True)

    # Set the color palette
    primary_color = "#5B7BA6"  # Blue
    secondary_color = "#AFD99C"  # Green
    tertiary_color = "#D1F2A0"  # Light green
    quaternary_color = "#A0CCF2"  # Light blue

    # Change text color
   
    # Center the markdown text
    st.markdown(
        f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center;">'
        f'<p style="color:{secondary_color}; font-size:24px;">HakiNasaCrops is a project that integrates farmers with the scientific community for reciprocal collaboration.</p>'
        '<p>This project seeks to pique the interest of farmers by providing them access to a wide range of valuable data about their crops. In addition, it aims to serve as a platform that attracts researchers and investors willing to collaborate with the agricultural community. Researchers will find a conducive environment here to apply their research and discover ways to improve crop quality and yield. On the other hand, farmers will receive significant support and have access to critical data provided by NASA satellites, which are essential to optimize their agricultural practices. This project has the potential to benefit all stakeholders involved in agriculture by fostering collaboration and knowledge sharing.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('Our team is made up of technology enthusiasts and nature lovers. We are committed to bringing the best of both worlds to your fingertips.')

    st.markdown('<p style="color:{quaternary_color}">*Founders:*</p>', unsafe_allow_html=True)
    st.markdown('- Rodrigo Arturo Cespedes Gonzales')
    st.markdown('- Shintia Jhasmy Luque Fernandez')
    st.markdown('- Jeanpier Miguel Valverde Ortega')
    st.markdown('- Ibeth Estefany Huamani Rubio')
    st.markdown('- Ibeth Estefany Huamani Rubio')

    st.markdown('<p style="color:{quaternary_color}">*Contact: 936418634*</p>', unsafe_allow_html=True)
    st.markdown('You can contact us via [email](mailto:your-email@example.com)')

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f'<p style="color:{quaternary_color}; text-align:center">© 2023 HakiNasaCrops</p>', unsafe_allow_html=True)
