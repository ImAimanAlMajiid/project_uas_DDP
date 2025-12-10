import streamlit as st
from template_sidebar import sidebar_menu

sidebar_menu()

st.title("Hitung Luas Bangun Datar")

menu = st.selectbox(
    "Pilih jenis bangun datar:",
    ["Luas Persegi", "Luas Segitiga", "Luas Lingkaran"]
)

if menu == "Luas Persegi":
    st.subheader("Luas Persegi")
    sisi = st.number_input("Masukkan panjang sisi:", min_value=0)
    
    if st.button("Hitung"):
        hasil = sisi * sisi
        st.success(f"Luas Persegi: {hasil}")

elif menu == "Luas Segitiga":
    st.subheader("Luas Segitiga")
    alas = st.number_input("Masukkan alas:", min_value=0)
    tinggi = st.number_input("Masukkan tinggi:", min_value=0)

    if st.button("Hitung"):
        hasil = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga: {hasil}")

elif menu == "Luas Lingkaran":
    import math
    st.subheader("Luas Lingkaran")
    r = st.number_input("Masukkan jari-jari:", min_value=0)

    if st.button("Hitung"):
        hasil = math.pi * r * r
        st.success(f"Luas Lingkaran: {hasil}")
