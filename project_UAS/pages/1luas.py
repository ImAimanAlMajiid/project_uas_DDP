import streamlit as st
from template_sidebar import sidebar_menu
import math

st.set_page_config(
    page_title="Luas Bangun Datar",
    layout="wide"
)

sidebar_menu()

st.title("Hitung Luas Bangun Datar")

menu = st.selectbox(
    "Pilih jenis bangun datar:",
    [
        "Luas Persegi",
        "Luas Persegi Panjang",
        "Luas Segitiga",
        "Luas Lingkaran",
        "Luas Jajar Genjang",
        "Luas Trapesium",
        "Luas Belah Ketupat",
        "Luas Layang-layang"
    ]
)


# 1. Persegi
if menu == "Luas Persegi":
    st.subheader("Luas Persegi")
    sisi = st.number_input("Masukkan panjang sisi:", min_value=0.0)

    if st.button("Hitung"):
        hasil = sisi * sisi
        st.success(f"Luas Persegi: {hasil}")

# 2. Persegi Panjang
elif menu == "Luas Persegi Panjang":
    st.subheader("Luas Persegi Panjang")
    panjang = st.number_input("Masukkan panjang:", min_value=0.0)
    lebar = st.number_input("Masukkan lebar:", min_value=0.0)

    if st.button("Hitung"):
        hasil = panjang * lebar
        st.success(f"Luas Persegi Panjang: {hasil}")

# 3. Segitiga
elif menu == "Luas Segitiga":
    st.subheader("Luas Segitiga")
    alas = st.number_input("Masukkan alas:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi:", min_value=0.0)

    if st.button("Hitung"):
        hasil = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga: {hasil}")

# 4. Lingkaran
elif menu == "Luas Lingkaran":
    st.subheader("Luas Lingkaran")
    r = st.number_input("Masukkan jari-jari:", min_value=0.0)

    if st.button("Hitung"):
        hasil = math.pi * r * r
        st.success(f"Luas Lingkaran: {hasil:.2f}")

# 5. Jajar Genjang
elif menu == "Luas Jajar Genjang":
    st.subheader("Luas Jajar Genjang")
    alas = st.number_input("Masukkan alas:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi:", min_value=0.0)

    if st.button("Hitung"):
        hasil = alas * tinggi
        st.success(f"Luas Jajar Genjang: {hasil}")

# 6. Trapesium
elif menu == "Luas Trapesium":
    st.subheader("Luas Trapesium")
    a = st.number_input("Masukkan sisi sejajar a:", min_value=0.0)
    b = st.number_input("Masukkan sisi sejajar b:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi:", min_value=0.0)

    if st.button("Hitung"):
        hasil = 0.5 * (a + b) * tinggi
        st.success(f"Luas Trapesium: {hasil}")

# 7. Belah Ketupat
elif menu == "Luas Belah Ketupat":
    st.subheader("Luas Belah Ketupat")
    d1 = st.number_input("Masukkan diagonal 1:", min_value=0.0)
    d2 = st.number_input("Masukkan diagonal 2:", min_value=0.0)

    if st.button("Hitung"):
        hasil = 0.5 * d1 * d2
        st.success(f"Luas Belah Ketupat: {hasil}")

# 8. Layang-layang
elif menu == "Luas Layang-layang":
    st.subheader("Luas Layang-layang")
    d1 = st.number_input("Masukkan diagonal 1:", min_value=0.0)
    d2 = st.number_input("Masukkan diagonal 2:", min_value=0.0)

    if st.button("Hitung"):
        hasil = 0.5 * d1 * d2
        st.success(f"Luas Layang-layang: {hasil}")
