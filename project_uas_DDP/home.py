import streamlit as st
from template_sidebar import sidebar_menu

# KONFIGURASI HALAMAN
def konfigurasi_halaman():
    st.set_page_config(
        page_title="Home | Belajar Matematika",
        layout="wide"
    )
    sidebar_menu()


# HEADER
def tampilkan_header():
    st.markdown(
        """
        <div style="text-align:center; padding:30px;">
            <h1>📚 Belajar Bangun Ruang dan Matematika Dasar</h1>
            <h4>Mudah • Interaktif • Menyenangkan</h4>
            <p>Website pembelajaran matematika dasar untuk memahami konsep dan rumus soal</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()


# FITUR
def tampilkan_fitur():
    st.subheader("✨ Fitur Pembelajaran")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            ### 🔢 Deret Angka
            - Mode Belajar
            - Mode Latihan
            - Aritmatika, Geometri, Fibonacci
            """
        )

    with col2:
        st.markdown(
            """
            ### 📐 Bangun Datar
            - Hitung Luas
            - Hitung Keliling
            - Berbagai bentuk bangun datar
            """
        )

    with col3:
        st.markdown(
            """
            ### 🧮 Kalkulator
            - Penjumlahan
            - Pengurangan
            - Perkalian
            - Pembagian
            """
        )

    st.divider()

# CARA BELAJAR
def tampilkan_cara_belajar():
    st.subheader("🧠 Cara Belajar di Website Ini")

    st.markdown(
        """
        1. **Pelajari materi** pada menu yang tersedia  
        2. **Hitung otomatis** dan pahami hasilnya  
        3. **Ulangi sampai paham**  

        Website ini dirancang agar belajar matematika menjadi lebih mudah dan tidak membosankan.
        """
    )
    st.divider()


# CTA
def tampilkan_ajakan():
    st.markdown(
        """
        <div style="text-align:center; padding:20px;">
            <h3>🚀 Siap Belajar?</h3>
            <p>Pilih menu di sidebar untuk mulai belajar matematika sekarang</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# FOOTER
def tampilkan_footer():
    st.markdown(
        """
        <hr>
        <div style="text-align:center; font-size:14px;">
            © 2025 | Project UAS DDP <br>
            Dibuat dengan ❤️ mahasiswa STT Nurul Fikri
        </div>
        """,
        unsafe_allow_html=True
    )



# PROGRAM UTAMA
def main():
    konfigurasi_halaman()
    tampilkan_header()
    tampilkan_fitur()
    tampilkan_cara_belajar()
    tampilkan_ajakan()
    tampilkan_footer()


# EKSEKUSI
main()
