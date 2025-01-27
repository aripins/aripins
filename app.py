import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# **Judul Aplikasi**
st.title("📊 Data Visualization App")

# **Upload File CSV**
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# **Jika file diunggah**
if uploaded_file is not None:
    # Membaca data
    df = pd.read_csv(uploaded_file)

    # Menampilkan Dataframe
    st.subheader("📄 Dataset Preview")
    st.write(df.head())

    # Statistik Deskriptif
    st.subheader("📊 Statistik Deskriptif")
    st.write(df.describe())

    # Pilih Kolom untuk Visualisasi
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    # **1. Heatmap Korelasi**
    st.subheader("🔥 Heatmap Korelasi")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    st.pyplot(fig)

    # **2. Histogram untuk Variabel Numerik**
    st.subheader("📈 Histogram Variabel Numerik")
    selected_hist = st.selectbox("Pilih Variabel:", numeric_columns)
    fig, ax = plt.subplots()
    sns.histplot(df[selected_hist], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    # **3. Pie Chart untuk Variabel Kategori**
    categorical_columns = df.select_dtypes(exclude=['number']).columns.tolist()
    if categorical_columns:
        st.subheader("🥧 Pie Chart Variabel Kategori")
        selected_pie = st.selectbox("Pilih Variabel Kategori:", categorical_columns)
        pie_data = df[selected_pie].value_counts()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
        ax.axis("equal")
        st.pyplot(fig)

    # **4. Scatter Plot untuk Relasi Dua Variabel**
    st.subheader("📊 Scatter Plot")
    col1, col2 = st.columns(2)
    x_axis = col1.selectbox("Pilih Variabel X:", numeric_columns)
    y_axis = col2.selectbox("Pilih Variabel Y:", numeric_columns)
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], alpha=0.7, ax=ax)
    st.pyplot(fig)

# **Footer**
st.markdown("---")
st.markdown("🔹 **Dibuat oleh Aripin Sihabudin** | 📅 2025")
