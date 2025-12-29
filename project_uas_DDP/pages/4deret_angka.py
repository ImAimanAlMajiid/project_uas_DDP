import streamlit as st
from template_sidebar import sidebar_menu

# ======================
# KONFIGURASI HALAMAN
# ======================
def konfigurasi_halaman():
    st.set_page_config(
        page_title="Deret Angka",
        layout="wide"
    )
    sidebar_menu()
    st.title("📊 Deret Angka")
    st.caption("Mode Belajar & Latihan dalam satu halaman")
    st.divider()


# ======================
# PILIH MODE
# ======================
def pilih_mode():
    return st.radio(
        "Pilih Mode:",
        ["📘 Mode Belajar", "✏️ Mode Latihan"],
        horizontal=True
    )


# ======================
# PILIH JENIS DERET
# ======================
def pilih_jenis_deret():
    return st.selectbox(
        "Pilih Jenis Deret:",
        [
            "Aritmatika",
            "Geometri",
            "Fibonacci",
            "Bilangan Ganjil",
            "Bilangan Genap"
        ]
    )


# ======================
# MODE BELAJAR
# ======================
def mode_belajar(jenis):
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


# ======================
# FUNGSI PERHITUNGAN
# ======================
def aritmatika(a, d, n):
    return a + (n - 1) * d

def geometri(a, r, n):
    return a * r ** (n - 1)

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def bilangan_ganjil(n):
    return 2 * n - 1

def bilangan_genap(n):
    return 2 * n


# ======================
# MODE LATIHAN
# ======================
def mode_latihan(jenis):
    st.header("🧮 Latihan Menghitung Deret")

    n = st.number_input("Masukkan suku ke-n", min_value=1, value=5)

    if jenis == "Aritmatika":
        a = st.number_input("Suku pertama (a)", value=2)
        d = st.number_input("Beda (d)", value=3)

        if st.button("Hitung"):
            hasil = aritmatika(a, d, n)
            st.success(f"Hasil suku ke-{n} = {hasil}")

    elif jenis == "Geometri":
        a = st.number_input("Suku pertama (a)", value=2)
        r = st.number_input("Rasio (r)", value=2)

        if st.button("Hitung"):
            hasil = geometri(a, r, n)
            st.success(f"Hasil suku ke-{n} = {hasil}")

    elif jenis == "Fibonacci":
        if st.button("Hitung"):
            fib = fibonacci(n)
            st.success(f"Hasil suku ke-{n} = {fib[n - 1]}")
            st.write("Deret:", fib[:n])

    elif jenis == "Bilangan Ganjil":
        if st.button("Hitung"):
            hasil = bilangan_ganjil(n)
            st.success(f"Hasil suku ke-{n} = {hasil}")

    elif jenis == "Bilangan Genap":
        if st.button("Hitung"):
            hasil = bilangan_genap(n)
            st.success(f"Hasil suku ke-{n} = {hasil}")


# ======================
# PROGRAM UTAMA
# ======================
def main():
    konfigurasi_halaman()
    mode = pilih_mode()
    jenis = pilih_jenis_deret()
    st.divider()

    if mode == "📘 Mode Belajar":
        mode_belajar(jenis)
    else:
        mode_latihan(jenis)


# ======================
# EKSEKUSI
# ======================
main()

