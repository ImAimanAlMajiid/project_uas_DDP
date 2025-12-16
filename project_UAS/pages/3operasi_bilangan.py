import streamlit as st
from template_sidebar import sidebar_menu

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Operasi Bilangan",
    layout="wide"
)

# Sidebar
sidebar_menu()

# ======================
# JUDUL
# ======================
st.title("🔢 Kalkulator Operasi Bilangan")
st.write(
    "Halaman ini digunakan untuk melakukan operasi hitung dasar "
    "pada dua buah bilangan."
)

st.divider()

# ======================
# PILIH OPERASI
# ======================
operation = st.selectbox(
    "Pilih operasi hitung:",
    [
        "Penjumlahan (+)",
        "Pengurangan (-)",
        "Perkalian (×)",
        "Pembagian (÷)"
    ]
)

st.divider()

# ======================
# INPUT ANGKA
# ======================
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Masukkan angka pertama:", value=0.0)

with col2:
    num2 = st.number_input("Masukkan angka kedua:", value=0.0)

# ======================
# PROSES HITUNG
# ======================
if st.button("Hitung Hasil"):
    if operation == "Penjumlahan (+)":
        hasil = num1 + num2
        st.success(f"Hasil: {num1} + {num2} = {hasil}")

    elif operation == "Pengurangan (-)":
        hasil = num1 - num2
        st.success(f"Hasil: {num1} - {num2} = {hasil}")

    elif operation == "Perkalian (×)":
        hasil = num1 * num2
        st.success(f"Hasil: {num1} × {num2} = {hasil}")

    elif operation == "Pembagian (÷)":
        if num2 != 0:
            hasil = num1 / num2
            st.success(f"Hasil: {num1} ÷ {num2} = {hasil}")
        else:
            st.error("Pembagian dengan nol tidak diperbolehkan.")
