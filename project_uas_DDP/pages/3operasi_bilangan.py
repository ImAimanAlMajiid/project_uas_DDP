import streamlit as st
from template_sidebar import sidebar_menu

# ======================
# KONFIGURASI HALAMAN
# ======================
def konfigurasi_halaman():
    st.set_page_config(
        page_title="Operasi Bilangan",
        layout="wide"
    )
    sidebar_menu()
    st.title("🔢 Kalkulator Operasi Bilangan")
    st.write(
        "Halaman ini digunakan untuk melakukan operasi hitung dasar "
        "pada dua buah bilangan."
    )
    st.divider()


# ======================
# PILIH OPERASI
# ======================
def pilih_operasi():
    return st.selectbox(
        "Pilih operasi hitung:",
        [
            "Penjumlahan (+)",
            "Pengurangan (-)",
            "Perkalian (×)",
            "Pembagian (÷)"
        ]
    )


# ======================
# INPUT ANGKA
# ======================
def input_angka():
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Masukkan angka pertama:", value=0.0)
    with col2:
        num2 = st.number_input("Masukkan angka kedua:", value=0.0)
    return num1, num2


# ======================
# FUNGSI OPERASI HITUNG
# ======================
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return None
    return a / b


# ======================
# PROSES HITUNG
# ======================
def proses_hitung(operasi, num1, num2):
    if operasi == "Penjumlahan (+)":
        hasil = penjumlahan(num1, num2)
        st.success(f"Hasil: {num1} + {num2} = {hasil}")

    elif operasi == "Pengurangan (-)":
        hasil = pengurangan(num1, num2)
        st.success(f"Hasil: {num1} - {num2} = {hasil}")

    elif operasi == "Perkalian (×)":
        hasil = perkalian(num1, num2)
        st.success(f"Hasil: {num1} × {num2} = {hasil}")

    elif operasi == "Pembagian (÷)":
        hasil = pembagian(num1, num2)
        if hasil is None:
            st.error("Pembagian dengan nol tidak diperbolehkan.")
        else:
            st.success(f"Hasil: {num1} ÷ {num2} = {hasil}")


# ======================
# PROGRAM UTAMA
# ======================
def main():
    konfigurasi_halaman()
    operasi = pilih_operasi()
    st.divider()
    num1, num2 = input_angka()

    if st.button("Hitung Hasil"):
        proses_hitung(operasi, num1, num2)


# ======================
# EKSEKUSI
# ======================
main()
