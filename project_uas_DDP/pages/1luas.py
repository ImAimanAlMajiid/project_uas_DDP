import streamlit as st
from template_sidebar import sidebar_menu
import math

# =========================
# KONFIGURASI HALAMAN
# =========================
def konfigurasi_halaman():
    st.set_page_config(page_title="Luas Bangun Datar", layout="wide")
    sidebar_menu()
    st.title("📐 Luas Bangun Datar")


# =========================
# PILIH MODE
# =========================
def pilih_mode():
    return st.radio("Mode Pembelajaran:", ["Belajar", "Kalkulator"], horizontal=True)


# =========================
# PILIH MENU
# =========================
def pilih_bangun():
    return st.selectbox(
        "Pilih Bangun Datar:",
        [
            "Persegi",
            "Persegi Panjang",
            "Segitiga",
            "Lingkaran",
            "Jajar Genjang",
            "Trapesium",
            "Belah Ketupat",
            "Layang-layang"
        ]
    )


# =========================
# FUNGSI RUMUS LUAS
# =========================
def luas_persegi(s):
    return s * s

def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def luas_lingkaran(r):
    return math.pi * r * r

def luas_jajar_genjang(a, t):
    return a * t

def luas_trapesium(a, b, t):
    return 0.5 * (a + b) * t

def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2


# =========================
# MODE BELAJAR
# =========================
def mode_belajar(menu):
    col1, col2 = st.columns([2, 1])

    rumus = {
        "Persegi": ("L = s × s", "https://cilacapklik.com/wp-content/uploads/2022/06/Rumus-Luas-Dan-Keliling-Persegi.png"),
        "Persegi Panjang": ("L = p × l", "https://tse1.mm.bing.net/th/id/OIP.yL-VkyTFQ4Jkps33TuGVmgHaEC?pid=Api&P=0&h=180"),
        "Segitiga": ("L = ½ × a × t", "https://tse2.mm.bing.net/th/id/OIP.FMRio0TKiNIbye3SdR5FjwHaE3?pid=Api&P=0&h=180"),
        "Lingkaran": ("L = π × r²", "https://tse2.mm.bing.net/th/id/OIP.YIW1MqoAIpX6v1fuUQvcjwHaEj?pid=Api&P=0&h=180"),
        "Jajar Genjang": ("L = a × t", "https://tse2.mm.bing.net/th/id/OIP.t34TiwruHJH2Vs6IuAcYcgHaEq?pid=Api&P=0&h=180"),
        "Trapesium": ("L = ½ × (a + b) × t", "https://tse3.mm.bing.net/th/id/OIP.QlFKC_GXHO4b0PhlPMBlhQHaEN?pid=Api&P=0&h=180"),
        "Belah Ketupat": ("L = ½ × d₁ × d₂", "https://1.bp.blogspot.com/-uyyp099vX6I/X7TFYZTMrgI/AAAAAAAARzU/EfyKY4EjbT0wqgZ5y0rURwv-ohpYPEyPQCLcBGAsYHQ/s1280/Rumus%2BLuas%2BBelah%2BKetupat.png"),
        "Layang-layang": ("L = ½ × d₁ × d₂", "https://tse1.mm.bing.net/th/id/OIP.3oOE4NCPlnbQB9f4tveoDgAAAA?pid=Api&P=0&h=180"),
    }

    with col1:
        st.subheader(f"Luas {menu}")
        st.write(f"**Rumus:** {rumus[menu][0]}")
        st.write("Materi ini digunakan untuk memahami cara menghitung luas bangun datar.")

    with col2:
        st.image(rumus[menu][1], caption=rumus[menu][0])


# =========================
# MODE KALKULATOR
# =========================
def mode_latihan(menu):
    st.subheader(f"🧮 Hitung Luas {menu}")

    if menu == "Persegi":
        s = st.number_input("Sisi", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_persegi(s)}")

    elif menu == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0)
        l = st.number_input("Lebar", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_persegi_panjang(p, l)}")

    elif menu == "Segitiga":
        a = st.number_input("Alas", min_value=0.0)
        t = st.number_input("Tinggi", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_segitiga(a, t)}")

    elif menu == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_lingkaran(r):.2f}")

    elif menu == "Jajar Genjang":
        a = st.number_input("Alas", min_value=0.0)
        t = st.number_input("Tinggi", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_jajar_genjang(a, t)}")

    elif menu == "Trapesium":
        a = st.number_input("Sisi sejajar a", min_value=0.0)
        b = st.number_input("Sisi sejajar b", min_value=0.0)
        t = st.number_input("Tinggi", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_trapesium(a, b, t)}")

    elif menu == "Belah Ketupat":
        d1 = st.number_input("Diagonal 1", min_value=0.0)
        d2 = st.number_input("Diagonal 2", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_belah_ketupat(d1, d2)}")

    elif menu == "Layang-layang":
        d1 = st.number_input("Diagonal 1", min_value=0.0)
        d2 = st.number_input("Diagonal 2", min_value=0.0)
        if st.button("Hitung"):
            st.success(f"Hasil = {luas_layang_layang(d1, d2)}")


# =========================
# PROGRAM UTAMA
# =========================
def main():
    konfigurasi_halaman()
    mode = pilih_mode()
    menu = pilih_bangun()
    st.divider()

    if mode == "Belajar":
        mode_belajar(menu)
    else:
        mode_latihan(menu)


# =========================
# EKSEKUSI
# =========================
main()
