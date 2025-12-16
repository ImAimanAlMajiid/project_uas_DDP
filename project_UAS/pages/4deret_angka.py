import streamlit as st
from template_sidebar import sidebar_menu

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Deret Angka",
    layout="wide"
)

sidebar_menu()

st.title("📊 Deret Angka")
st.caption("Mode Belajar & Latihan dalam satu halaman")

# ======================
# MODE
# ======================
mode = st.radio(
    "Pilih Mode:",
    ["📘 Mode Belajar", "✏️ Mode Latihan"],
    horizontal=True
)

st.divider()

# ======================
# PILIH JENIS DERET
# ======================
jenis = st.selectbox(
    "Pilih Jenis Deret:",
    [
        "Aritmatika",
        "Geometri",
        "Fibonacci",
        "Bilangan Ganjil",
        "Bilangan Genap"
    ]
)

st.divider()

# ======================================================
# MODE BELAJAR
# ======================================================
if mode == "📘 Mode Belajar":

    st.header("📚 Materi Deret Angka")

    if jenis == "Aritmatika":
        st.subheader("Deret Aritmatika")
        st.write("Deret dengan selisih (beda) yang tetap.")
        st.latex("U_n = a + (n - 1)d")
        st.write("Contoh: 2, 4, 6, 8, 10")

    elif jenis == "Geometri":
        st.subheader("Deret Geometri")
        st.write("Deret dengan rasio yang tetap.")
        st.latex("U_n = a \\times r^{(n-1)}")
        st.write("Contoh: 2, 4, 8, 16")

    elif jenis == "Fibonacci":
        st.subheader("Deret Fibonacci")
        st.write("Setiap suku adalah jumlah dua suku sebelumnya.")
        st.latex("F_n = F_{n-1} + F_{n-2}")
        st.write("Contoh: 0, 1, 1, 2, 3, 5")

    elif jenis == "Bilangan Ganjil":
        st.subheader("Deret Bilangan Ganjil")
        st.latex("U_n = 2n - 1")
        st.write("Contoh: 1, 3, 5, 7, 9")

    elif jenis == "Bilangan Genap":
        st.subheader("Deret Bilangan Genap")
        st.latex("U_n = 2n")
        st.write("Contoh: 2, 4, 6, 8, 10")

# ======================================================
# MODE LATIHAN
# ======================================================
elif mode == "✏️ Mode Latihan":

    st.header("🧮 Latihan Menghitung Deret")

    n = st.number_input("Masukkan suku ke-n", min_value=1, value=5)

    if jenis == "Aritmatika":
        a = st.number_input("Suku pertama (a)", value=2)
        d = st.number_input("Beda (d)", value=3)

        if st.button("Hitung"):
            hasil = a + (n - 1) * d
            st.success(f"Hasil suku ke-{n} = {hasil}")

    elif jenis == "Geometri":
        a = st.number_input("Suku pertama (a)", value=2)
        r = st.number_input("Rasio (r)", value=2)

        if st.button("Hitung"):
            hasil = a * r ** (n - 1)
            st.success(f"Hasil suku ke-{n} = {hasil}")

    elif jenis == "Fibonacci":
        if st.button("Hitung"):
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[i-1] + fib[i-2])
            st.success(f"Hasil suku ke-{n} = {fib[n-1]}")
            st.write("Deret:", fib[:n])

    elif jenis == "Bilangan Ganjil":
        if st.button("Hitung"):
            hasil = 2 * n - 1
            st.success(f"Hasil suku ke-{n} = {hasil}")

    elif jenis == "Bilangan Genap":
        if st.button("Hitung"):
            hasil = 2 * n
            st.success(f"Hasil suku ke-{n} = {hasil}")
