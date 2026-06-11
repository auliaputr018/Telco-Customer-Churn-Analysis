import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image


def run():

    # Styling tampilan dashboard
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
    /* Card metric */
    .metric-card {
        background-color: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(8px);
        text-align: center;
    }
    /* Card insight */
    .glass {
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Menampilkan judul dashboard
    st.markdown(
        """
        <h1 style='text-align: center;'>
        Telco Customer Churn Analysis
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Menampilkan deskripsi dashboard
    st.markdown(
        """
        <h4 style='text-align: center; color: gray;'>
        Analisis perilaku pelanggan dan faktor-faktor yang memengaruhi customer churn.
        </h4>
        """,
        unsafe_allow_html=True
    )

    # Menampilkan gambar utama dashboard
    image = Image.open('./src/pic22.png')

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image(
            image,
            width=1200
        )

    # Membaca dataset
    df = pd.read_csv('./src/Telco-Customer-Churn.csv')

    # Mengubah tipe data TotalCharges menjadi numerik
    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'],
        errors='coerce'
    )

    # Mengisi missing value menggunakan median
    df['TotalCharges'] = df['TotalCharges'].fillna(
        df['TotalCharges'].median()
    )

    # Menampilkan overview dataset
    st.markdown('---')
    st.write('## Dataset Overview')

    # Menghitung persentase churn
    churn_rate = round(
        (df['Churn'].value_counts(normalize=True)['Yes']) * 100,
        1
    )

    col1, col2, col3 = st.columns(3)

    # Menampilkan total customer
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{df.shape[0]}</h2>
            <p>Total Customers</p>
        </div>
        """, unsafe_allow_html=True)

    # Menampilkan total fitur
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{df.shape[1]}</h2>
            <p>Total Features</p>
        </div>
        """, unsafe_allow_html=True)

    # Menampilkan churn rate
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{churn_rate}%</h2>
            <p>Churn Rate</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('---')

    # Menampilkan dataset
    with st.expander('Show Dataset'):
        st.dataframe(df)

    st.markdown('---')

    # Visualisasi distribusi churn
    st.write('## Churn Distribution')

    col1, col2 = st.columns([1,1])

    # Pie chart churn
    with col1:

        fig = px.pie(
            df,
            names='Churn',
            color='Churn',
            hole=0.6,
            color_discrete_map={
                'Yes': '#ef4444',
                'No': '#22c55e'
            }
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Menampilkan insight churn
    with col2:

        st.markdown("""
        <div class="glass">
        - Mayoritas pelanggan berada pada kategori non-churn.
        - Dataset memiliki kondisi imbalanced.
        - Pelanggan churn sekitar 26% dari total data.
        </div>
        """, unsafe_allow_html=True)

    st.markdown('---')

    # Visualisasi churn berdasarkan gender
    st.header('Churn Berdasarkan Gender')

    fig = px.histogram(
        df,
        x='gender',
        color='Churn',
        barmode='group',
        text_auto=True,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        'Jumlah churn laki-laki dan perempuan relatif seimbang.'
    )

    st.markdown('---')

    # Visualisasi churn berdasarkan senior citizen
    st.header('Churn Berdasarkan Senior Citizen')

    fig = px.histogram(
        df,
        x='SeniorCitizen',
        color='Churn',
        barmode='group',
        text_auto=True,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        'Pelanggan senior memiliki proporsi churn lebih tinggi.'
    )

    st.markdown('---')

    # Visualisasi churn berdasarkan partner
    st.header('Churn Berdasarkan Partner')

    fig = px.histogram(
        df,
        x='Partner',
        color='Churn',
        barmode='group',
        text_auto=True,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        'Pelanggan tanpa partner cenderung lebih sering churn.'
    )

    st.markdown('---')

    # Visualisasi churn berdasarkan contract
    st.write('## Contract')

    fig = px.histogram(
        df,
        x='Contract',
        color='Churn',
        barmode='group',
        text_auto=True,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        'Pelanggan dengan kontrak month-to-month memiliki churn paling tinggi.'
    )

    st.markdown('---')

    # Visualisasi distribusi tenure
    st.write('## Tenure Distribution')

    fig = px.histogram(
        df,
        x='tenure',
        color='Churn',
        marginal='box',
        nbins=30,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        'Pelanggan baru cenderung lebih sering melakukan churn.'
    )

    st.markdown('---')

    # Visualisasi monthly charges terhadap churn
    st.write('## Churn Berdasarkan Monthly Charges')

    fig = px.box(
        df,
        x='Churn',
        y='MonthlyCharges',
        color='Churn',
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.warning(
        'Pelanggan churn cenderung memiliki biaya bulanan lebih tinggi.'
    )

    st.markdown('---')

    # Visualisasi churn berdasarkan metode pembayaran
    st.write('## Churn Berdasarkan Payment Method')

    fig = px.histogram(
        df,
        x='PaymentMethod',
        color='Churn',
        barmode='group',
        text_auto=True,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        xaxis_tickangle=-15,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.warning(
        'Electronic Check memiliki tingkat churn paling tinggi.'
    )

    st.markdown('---')

    # Visualisasi churn berdasarkan internet service
    st.write('## Churn Berdasarkan Internet Service')

    fig = px.histogram(
        df,
        x='InternetService',
        color='Churn',
        barmode='group',
        text_auto=True,
        color_discrete_map={
            'Yes': '#ef4444',
            'No': '#3b82f6'
        }
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.02)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        'Pengguna Fiber Optic memiliki tingkat churn lebih tinggi.'
    )

    st.markdown('---')

    # Membuat heatmap correlation
    st.write('## Correlation Heatmap')

    # Membuat salinan dataframe
    corr_df = df.copy()

    # Mengubah label churn menjadi numerik
    corr_df['Churn'] = corr_df['Churn'].map({
        'No': 0,
        'Yes': 1
    })

    # Memilih fitur numerik
    numeric_df = corr_df[
        [
            'tenure',
            'MonthlyCharges',
            'TotalCharges',
            'Churn'
        ]
    ]

    # Menghitung korelasi spearman
    corr = numeric_df.corr(method='spearman')

    # Membuat visualisasi heatmap
    fig = px.imshow(
        corr,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r'
    )

    fig.update_layout(
        title='Spearman Correlation Matrix',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        'Tenure memiliki hubungan negatif terhadap churn, sedangkan MonthlyCharges memiliki hubungan positif terhadap churn.'
    )


if __name__ == "__main__":
    run()