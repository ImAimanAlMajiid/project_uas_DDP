import streamlit as st
from template_sidebar import sidebar_menu
import math

def konfigurasi_halaman():
    st.set_page_config(
        page_title="Keliling Bangun Datar",
        layout="wide"
    )
    sidebar_menu()
    st.title("📏 Keliling Bangun Datar")


# PILIH MODE & MENU
def pilih_mode():
    return st.radio(
        "Mode Pembelajaran:",
        ["Belajar", "Kalkulator"],
        horizontal=True
    )


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

# MODE BELAJAR
def mode_belajar(menu):
    col1, col2 = st.columns([2, 1])

    if menu == "Persegi":
        with col1:
            st.subheader("Keliling Persegi")
            st.write("Keliling persegi adalah jumlah keempat sisinya.")
        with col2:
            st.image("https://tse3.mm.bing.net/th/id/OIP.PQASlx1mRJXZpgaLwm_u7gHaEK?pid=Api&P=0&h=180", caption="Rumus: K = 4 × s")

    elif menu == "Persegi Panjang":
        with col1:
            st.subheader("Keliling Persegi Panjang")
            st.write("Keliling persegi panjang adalah dua kali jumlah panjang dan lebar.")
        with col2:
            st.image("https://tse1.mm.bing.net/th/id/OIP.yL-VkyTFQ4Jkps33TuGVmgHaEC?pid=Api&P=0&h=180", caption="Rumus: K = 2 × (p + l)")

    elif menu == "Segitiga":
        with col1:
            st.subheader("Keliling Segitiga")
            st.write("Keliling segitiga adalah jumlah ketiga sisinya.")
        with col2:
            st.image("https://tse2.mm.bing.net/th/id/OIP.tuSGo115p8HT6OwOW769NQHaEK?pid=Api&P=0&h=180", caption="Rumus: K = a + b + c")

    elif menu == "Lingkaran":
        with col1:
            st.subheader("Keliling Lingkaran")
            st.write("Keliling lingkaran dihitung menggunakan jari-jari atau diameter.")
        with col2:
            st.image("https://tse4.mm.bing.net/th/id/OIP.nC1e5kBK00kPo0df6oO_kQAAAA?pid=Api&P=0&h=180", caption="Rumus: K = 2 × π × r")

    elif menu == "Jajar Genjang":
        with col1:
            st.subheader("Keliling Jajar Genjang")
            st.write("Keliling jajar genjang adalah dua kali jumlah sisi sejajar.")
        with col2:
            st.image("https://tse4.mm.bing.net/th/id/OIP.nC1e5kBK00kPo0df6oO_kQAAAA?pid=Api&P=0&h=180", caption="Rumus: K = 2 × (a + b)")

    elif menu == "Trapesium":
        with col1:
            st.subheader("Keliling Trapesium")
            st.write("Keliling trapesium adalah jumlah semua sisinya.")
        with col2:
            st.image("https://tse1.mm.bing.net/th/id/OIP.ImCWrLMASecRzCmVoOzuKwAAAA?pid=Api&P=0&h=180", caption="Rumus: K = a + b + c + d")

    elif menu == "Belah Ketupat":
        with col1:
            st.subheader("Keliling Belah Ketupat")
            st.write("Belah ketupat memiliki empat sisi sama panjang.")
        with col2:
            st.image("https://tse4.mm.bing.net/th/id/OIP.1CWyHJTQKfEma4gts0emgQAAAA?pid=Api&P=0&h=180", caption="Rumus: K = 4 × s")

    elif menu == "Layang-layang":
        with col1:
            st.subheader("Keliling Layang-layang")
            st.write("Keliling layang-layang adalah jumlah semua sisinya.")
        with col2:
            st.image("https://tse4.mm.bing.net/th/id/OIP.84OLfzl0zwM1-tMfoSYyvAHaE8?pid=Api&P=0&h=180", caption="Rumus: K = 2 × (a + b)")


# MODE LATIHAN (KALKULATOR)
def mode_latihan(menu):
    st.subheader("🧮 Hitung Keliling")

    if menu == "Persegi":
        s = st.number_input("Masukkan sisi", min_value=0.0)
        st.success(f"Keliling = {4 * s}")

    elif menu == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0)
        l = st.number_input("Lebar", min_value=0.0)
        st.success(f"Keliling = {2 * (p + l)}")

    elif menu == "Segitiga":
        a = st.number_input("Sisi a", min_value=0.0)
        b = st.number_input("Sisi b", min_value=0.0)
        c = st.number_input("Sisi c", min_value=0.0)
        st.success(f"Keliling = {a + b + c}")

    elif menu == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0)
        st.success(f"Keliling = {2 * math.pi * r:.2f}")

    elif menu == "Jajar Genjang":
        a = st.number_input("Sisi a", min_value=0.0)
        b = st.number_input("Sisi b", min_value=0.0)
        st.success(f"Keliling = {2 * (a + b)}")

    elif menu == "Trapesium":
        a = st.number_input("Sisi a", min_value=0.0)
        b = st.number_input("Sisi b", min_value=0.0)
        c = st.number_input("Sisi c", min_value=0.0)
        d = st.number_input("Sisi d", min_value=0.0)
        st.success(f"Keliling = {a + b + c + d}")

    elif menu == "Belah Ketupat":
        s = st.number_input("Sisi", min_value=0.0)
        st.success(f"Keliling = {4 * s}")

    elif menu == "Layang-layang":
        a = st.number_input("Sisi a", min_value=0.0)
        b = st.number_input("Sisi b", min_value=0.0)
        st.success(f"Keliling = {2 * (a + b)}")

# PROGRAM UTAMA
def main():
    konfigurasi_halaman()
    mode = pilih_mode()
    menu = pilih_bangun()
    st.divider()

    if mode == "Belajar":
        mode_belajar(menu)
    else:
        mode_latihan(menu)
        
main()
