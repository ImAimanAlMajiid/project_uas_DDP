import streamlit as st
from template_sidebar import sidebar_menu
import math

st.set_page_config(
    page_title="Keliling Bangun Datar",
    layout="wide"
)

sidebar_menu()

st.title("Hitung Keliling Bangun Datar")

menu = st.selectbox(
    "Pilih jenis bangun datar:",
    [
        "Keliling Persegi",
        "Keliling Persegi Panjang",
        "Keliling Segitiga",
        "Keliling Lingkaran",
        "Keliling Jajar Genjang",
        "Keliling Trapesium",
        "Keliling Belah Ketupat",
        "Keliling Layang-layang"
    ]
)

if menu == "Keliling Persegi":
    st.subheader("Keliling Persegi")
    sisi = st.number_input("Masukkan panjang sisi:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Persegi: {4 * sisi}")

elif menu == "Keliling Persegi Panjang":
    st.subheader("Keliling Persegi Panjang")
    panjang = st.number_input("Masukkan panjang:", min_value=0.0)
    lebar = st.number_input("Masukkan lebar:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Persegi Panjang: {2 * (panjang + lebar)}")

elif menu == "Keliling Segitiga":
    st.subheader("Keliling Segitiga")
    sisi1 = st.number_input("Masukkan sisi 1:", min_value=0.0)
    sisi2 = st.number_input("Masukkan sisi 2:", min_value=0.0)
    sisi3 = st.number_input("Masukkan sisi 3:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Segitiga: {sisi1 + sisi2 + sisi3}")

elif menu == "Keliling Lingkaran":
    st.subheader("Keliling Lingkaran")
    r = st.number_input("Masukkan jari-jari:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Lingkaran: {2 * math.pi * r:.2f}")

elif menu == "Keliling Jajar Genjang":
    st.subheader("Keliling Jajar Genjang")
    a = st.number_input("Masukkan sisi a:", min_value=0.0)
    b = st.number_input("Masukkan sisi b:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Jajar Genjang: {2 * (a + b)}")

elif menu == "Keliling Trapesium":
    st.subheader("Keliling Trapesium")
    a = st.number_input("Masukkan sisi a:", min_value=0.0)
    b = st.number_input("Masukkan sisi b:", min_value=0.0)
    c = st.number_input("Masukkan sisi c:", min_value=0.0)
    d = st.number_input("Masukkan sisi d:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Trapesium: {a + b + c + d}")

elif menu == "Keliling Belah Ketupat":
    st.subheader("Keliling Belah Ketupat")
    s = st.number_input("Masukkan panjang sisi:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Belah Ketupat: {4 * s}")

elif menu == "Keliling Layang-layang":
    st.subheader("Keliling Layang-layang")
    a = st.number_input("Masukkan sisi a:", min_value=0.0)
    b = st.number_input("Masukkan sisi b:", min_value=0.0)

    if st.button("Hitung"):
        st.success(f"Keliling Layang-layang: {2 * (a + b)}")
