import streamlit as st
import pandas as pd
import joblib
import os

# --- ATURAN STREAMLIT: set_page_config() harus menjadi perintah pertama ---
# Konfigurasi halaman harus dijalankan tepat setelah import.
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# --- FUNGSI UNTUK MEMUAT MODEL ---
# Fungsi ini menggunakan cache agar model tidak perlu dimuat ulang setiap kali
# ada interaksi, sehingga aplikasi lebih cepat.
@st.cache_resource
def load_model(model_path):
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        return model
    else:
        st.error(f"File model tidak ditemukan di path: {model_path}")
        st.error("Pastikan file 'student_dropout_model.pkl' ada di dalam folder 'model'.")
        return None

# --- MEMUAT MODEL ---
model = load_model('model/student_dropout_model.pkl')

# --- JUDUL DAN DESKRIPSI APLIKASI ---
st.title('🎓 Aplikasi Prediksi Dropout Mahasiswa')
st.write(
    "Aplikasi ini menggunakan model Machine Learning untuk memprediksi "
    "kemungkinan seorang mahasiswa akan dropout berdasarkan data performa "
    "akademik dan demografis."
)

# --- SIDEBAR UNTUK INPUT PENGGUNA ---
st.sidebar.header('Masukkan Data Mahasiswa:')

def user_input_features():
    # Input yang paling berpengaruh berdasarkan analisis
    tuition = st.sidebar.selectbox('Status Pembayaran UKT?', ('Lunas', 'Menunggak'))
    scholarship = st.sidebar.selectbox('Penerima Beasiswa?', ('Ya', 'Tidak'))
    units_1st_sem_approved = st.sidebar.slider('Jumlah SKS Lulus Semester 1', 0, 26, 10, 1)
    units_2nd_sem_approved = st.sidebar.slider('Jumlah SKS Lulus Semester 2', 0, 20, 10, 1)
    age = st.sidebar.slider('Umur Saat Pendaftaran', 17, 70, 20, 1)
    gdp = st.sidebar.slider('Pertumbuhan Ekonomi (GDP)', -4.0, 4.0, 1.0, 0.1)

    # Mengubah input menjadi format yang dikenali model (0 atau 1)
    data = {
        'Tuition_fees_up_to_date': 1 if tuition == 'Lunas' else 0,
        'Scholarship_holder': 1 if scholarship == 'Ya' else 0,
        'Age_at_enrollment': age,
        'Curricular_units_1st_sem_approved': units_1st_sem_approved,
        'Curricular_units_2nd_sem_approved': units_2nd_sem_approved,
        'GDP': gdp
    }
    return pd.DataFrame(data, index=[0])

# --- PROSES PREDIKSI ---
# Hanya tampilkan dan jalankan prediksi jika model berhasil dimuat
if model is not None:
    input_df_user = user_input_features()

    # Menggabungkan input pengguna dengan dataframe default untuk fitur lainnya
    all_columns = model.feature_names_in_
    full_df = pd.DataFrame(columns=all_columns)
    full_df.loc[0] = 0 # Inisialisasi semua fitur dengan nilai 0 sebagai default

    # Timpa nilai default dengan input dari pengguna
    for col in input_df_user.columns:
        if col in full_df.columns:
            full_df[col] = input_df_user[col].values

    st.subheader('Data Mahasiswa yang Diinput:')
    st.write(input_df_user)

    # Tombol untuk melakukan prediksi
    if st.button('Lakukan Prediksi'):
        try:
            prediction = model.predict(full_df)[0]
            prediction_proba = model.predict_proba(full_df)[0]

            st.subheader('Hasil Prediksi:')
            if prediction == 1:
                st.error(f'Mahasiswa ini berpotensi **DROPOUT**.')
                st.write(f"**Tingkat Keyakinan:** {prediction_proba[1]*100:.2f}%")
            else:
                st.success(f'Mahasiswa ini kemungkinan **TIDAK AKAN DROPOUT**.')
                st.write(f"**Tingkat Keyakinan:** {prediction_proba[0]*100:.2f}%")
        except Exception as e:
            st.error(f"Terjadi error saat prediksi: {e}")
else:
    st.warning("Model tidak dapat dimuat. Silakan periksa file model dan path-nya.")