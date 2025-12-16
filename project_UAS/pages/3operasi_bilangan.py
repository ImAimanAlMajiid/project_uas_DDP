import streamlit as st
from template_sidebar import sidebar_menu

sidebar_menu()

st.title("Kalkulator Operasi Bilangan")


operation = st.selectbox("Pilih operasi", ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (*)", "Pembagian (/)"])

num1 = st.number_input("Masukkan angka pertama", value=0)
num2 = st.number_input("Masukkan angka kedua", value=0)

if st.button("Hitung"):
    if operation == "Penjumlahan (+)":
        result = num1 + num2
        st.write(f"Hasil: {num1} + {num2} = {result}")
    elif operation == "Pengurangan (-)":
        result = num1 - num2
        st.write(f"Hasil: {num1} - {num2} = {result}")
    elif operation == "Perkalian (*)":
        result = num1 * num2
        st.write(f"Hasil: {num1} * {num2} = {result}")
    elif operation == "Pembagian (/)":
        if num2 != 0:
            result = num1 / num2
            st.write(f"Hasil: {num1} / {num2} = {result}")
        else:
            st.error("Error: Pembagian dengan nol tidak diperbolehkan!")