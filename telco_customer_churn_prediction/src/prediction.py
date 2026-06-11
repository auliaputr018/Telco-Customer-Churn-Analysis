import streamlit as st
import pandas as pd
import pickle
from PIL import Image


# Membaca model machine learning
with open('./src/best_model.pkl', 'rb') as file:
    model = pickle.load(file)


def run():

    # Styling tampilan halaman prediction
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a,
            #111827,
            #1e293b
        );
        color: white;
    }
    h1, h2, h3, h4 {
        color: white !important;
    }
    p, label {
        color: #e5e7eb !important;
    }
    /* Card hasil prediction */
    .pred-box {
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        margin-top: 20px;
    }
    /* Styling gambar */
    .hero-img img {
        border-radius: 30px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow:
            0 0 20px rgba(59,130,246,0.25),
            0 0 50px rgba(59,130,246,0.12);
        opacity: 0.95;
    }
    </style>
    """, unsafe_allow_html=True)

    # Menampilkan judul halaman
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 55px;'>
        Telco Customer Churn Prediction
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Menampilkan deskripsi aplikasi
    st.markdown(
        """
        <h4 style='text-align: center; color: #cbd5e1; margin-bottom: 35px;'>
        Memprediksi apakah pelanggan akan melakukan churn atau tetap menggunakan layanan telekomunikasi berdasarkan karakteristik dan perilaku pelanggan.
        </h4>
        """,
        unsafe_allow_html=True
    )

    # Menampilkan gambar prediction
    image = Image.open('./src/pic.png')

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image(
            image,
            width=800
        )

    st.markdown('---')

    # Membuat form input prediction
    with st.form('churn_form'):

        st.subheader('Customer Information')

        col1, col2, col3 = st.columns(3)

        # Input informasi pelanggan
        with col1:

            gender = st.selectbox(
                'Gender',
                ['Male', 'Female']
            )

            senior = st.selectbox(
                'Senior Citizen',
                [0, 1]
            )

            partner = st.selectbox(
                'Partner',
                ['Yes', 'No']
            )

            dependents = st.selectbox(
                'Dependents',
                ['Yes', 'No']
            )

        # Input informasi tagihan pelanggan
        with col2:

            tenure = st.slider(
                'Tenure (Months)',
                0,
                72,
                12
            )

            monthly = st.number_input(
                'Monthly Charges',
                0.0,
                200.0,
                70.0
            )

            total = st.number_input(
                'Total Charges',
                0.0,
                10000.0,
                1000.0
            )

        # Input layanan pelanggan
        with col3:

            contract = st.selectbox(
                'Contract',
                [
                    'Month-to-month',
                    'One year',
                    'Two year'
                ]
            )

            payment = st.selectbox(
                'Payment Method',
                [
                    'Electronic check',
                    'Mailed check',
                    'Bank transfer (automatic)',
                    'Credit card (automatic)'
                ]
            )

            internet = st.selectbox(
                'Internet Service',
                [
                    'DSL',
                    'Fiber optic',
                    'No'
                ]
            )

        # Section layanan tambahan
        st.subheader('Additional Services')

        col4, col5, col6 = st.columns(3)

        # Input layanan tambahan pertama
        with col4:

            phone = st.selectbox(
                'Phone Service',
                ['Yes', 'No']
            )

            multiple = st.selectbox(
                'Multiple Lines',
                ['Yes', 'No', 'No phone service']
            )

            security = st.selectbox(
                'Online Security',
                ['Yes', 'No', 'No internet service']
            )

        # Input layanan tambahan kedua
        with col5:

            backup = st.selectbox(
                'Online Backup',
                ['Yes', 'No', 'No internet service']
            )

            protection = st.selectbox(
                'Device Protection',
                ['Yes', 'No', 'No internet service']
            )

            support = st.selectbox(
                'Tech Support',
                ['Yes', 'No', 'No internet service']
            )

        # Input layanan tambahan ketiga
        with col6:

            tv = st.selectbox(
                'Streaming TV',
                ['Yes', 'No', 'No internet service']
            )

            movies = st.selectbox(
                'Streaming Movies',
                ['Yes', 'No', 'No internet service']
            )

            paperless = st.selectbox(
                'Paperless Billing',
                ['Yes', 'No']
            )

        # Button prediction
        predict = st.form_submit_button(
            'Predict Churn'
        )

    # Menjalankan prediction
    if predict:

        # Membuat dataframe input
        data_inf = pd.DataFrame({

            'gender': [gender],
            'SeniorCitizen': [senior],
            'Partner': [partner],
            'Dependents': [dependents],
            'tenure': [tenure],
            'PhoneService': [phone],
            'MultipleLines': [multiple],
            'InternetService': [internet],
            'OnlineSecurity': [security],
            'OnlineBackup': [backup],
            'DeviceProtection': [protection],
            'TechSupport': [support],
            'StreamingTV': [tv],
            'StreamingMovies': [movies],
            'Contract': [contract],
            'PaperlessBilling': [paperless],
            'PaymentMethod': [payment],
            'MonthlyCharges': [monthly],
            'TotalCharges': [total]

        })

        # Melakukan prediction
        prediction = model.predict(data_inf)

        # Menghitung probabilitas prediction
        probability = model.predict_proba(data_inf)

        churn_prob = probability[0][1] * 100

        st.markdown('---')

        # Menampilkan hasil prediction
        st.subheader('Prediction Result')

        # Kondisi jika customer diprediksi churn
        if prediction[0] == 1:

            st.error(
                f'Customer Berpotensi Churn ({churn_prob:.2f}%)'
            )

            st.markdown("""
            <div class='pred-box'>
            <h3>Note</h3>
            <p>
            Pelanggan memiliki kemungkinan tinggi 
            untuk berhenti berlangganan.
            </p>
            <ul>
                <li>Kontrak bulanan</li>
                <li>Biaya bulanan tinggi</li>
                <li>Tenure rendah</li>
                <li>Layanan Fiber Optic</li>
                <li>Electronic check</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        # Kondisi jika customer diprediksi tidak churn
        else:

            st.success(
                f'Customer Cenderung Bertahan ({100 - churn_prob:.2f}%)'
            )

            st.markdown("""
            <div class='pred-box'>
            <h3>Note</h3>
            <p>
            Pelanggan memiliki kemungkinan 
            untuk tetap menggunakan layanan.
            </p>
            <ul>
                <li>Tenure tinggi</li>
                <li>Kontrak jangka panjang</li>
                <li>Biaya stabil</li>
                <li>Menggunakan layanan tambahan</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        # Menampilkan data input customer
        with st.expander('Show Input Data'):

            st.dataframe(data_inf)


if __name__ == "__main__":
    run()