import streamlit as st
import eda
import prediction


# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    page_title='Telco Customer Churn',
    layout='wide'
)

# Menyimpan state halaman aktif
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


# Styling tampilan aplikasi
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #172554,
        #1e293b
    );
    color: white;
}
h1, h2, h3, h4 {
    color: white !important;
}
p {
    color: #cbd5e1 !important;
}
/* Judul utama */
.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    margin-top: 40px;
}
/* Subjudul */
.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 22px;
    margin-bottom: 50px;
}
/* Card menu */
.card {
    background: rgba(255,255,255,0.06);
    padding: 35px;
    border-radius: 30px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    box-shadow:
        0 0 20px rgba(59,130,246,0.15),
        0 0 50px rgba(59,130,246,0.08);
    transition: 0.3s;
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
/* Hover card */
.card:hover {
    transform: translateY(-8px);
}
/* Judul card */
.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 15px;
}
/* Styling button */
.stButton > button {
    background: rgba(59,130,246,0.18) !important;
    color: white !important;
    border: 1px solid rgba(96,165,250,0.3) !important;
    border-radius: 14px !important;
    padding: 12px 18px !important;
    font-weight: 600 !important;
    transition: 0.3s !important;
}
/* Hover button */
.stButton > button:hover {
    background: rgba(96,165,250,0.28) !important;
    border: 1px solid rgba(147,197,253,0.5) !important;
    transform: translateY(-2px);
}
/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 80px;
    margin-bottom: 20px;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)


# Halaman home
if st.session_state.page == 'Home':

    # Judul utama aplikasi
    st.markdown(
        """
        <div class='main-title'>
        Telco Customer Churn
        </div>
        """,
        unsafe_allow_html=True
    )

    # Deskripsi aplikasi
    st.markdown(
        """
        <div class='sub-title'>
        Aplikasi machine learning untuk memprediksi customer churn
        berdasarkan karakteristik dan perilaku pelanggan.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<br>', unsafe_allow_html=True)

    # Layout card menu
    col1, col2 = st.columns(2)

    # Card halaman EDA
    with col1:

        st.markdown("""
        <div class='card'>
        <div class='section-title'>
        Exploratory Data Analysis
        </div>
        <p>
        Analisis data pelanggan untuk memahami pola churn,
        distribusi data, korelasi fitur,
        dan insight bisnis pelanggan.
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<br>', unsafe_allow_html=True)

        # Button menuju halaman EDA
        if st.button(
            'EDA Dashboard',
            use_container_width=True
        ):

            st.session_state.page = 'EDA'
            st.rerun()

    # Card halaman prediction
    with col2:

        st.markdown("""
        <div class='card'>
        <div class='section-title'>
        Customer Churn Prediction
        </div>
        <p>
        Prediksi apakah pelanggan akan churn
        atau tetap menggunakan layanan telekomunikasi.
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<br>', unsafe_allow_html=True)

        # Button menuju halaman prediction
        if st.button(
            'Prediction Page',
            use_container_width=True
        ):

            st.session_state.page = 'Prediction'
            st.rerun()


# Halaman EDA
elif st.session_state.page == 'EDA':

    # Button kembali ke home
    if st.button('Back to Home'):

        st.session_state.page = 'Home'
        st.rerun()

    # Menjalankan halaman EDA
    eda.run()


# Halaman prediction
elif st.session_state.page == 'Prediction':

    # Button kembali ke home
    if st.button('Back to Home'):

        st.session_state.page = 'Home'
        st.rerun()

    # Menjalankan halaman prediction
    prediction.run()


# Footer aplikasi
st.markdown(
    """
    <div class='footer'>
    Telco Customer Churn <br>
    Created by Aulia Putri
    </div>
    """,
    unsafe_allow_html=True
)