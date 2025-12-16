import streamlit as st

# ======================
# PAGE CONFIG (WAJIB PALING ATAS)
# ======================
st.set_page_config(
    page_title="Deret Angka",
    layout="wide"
)

from template_sidebar import sidebar_menu

sidebar_menu()

col1, col2, col3 = st.columns([1, 2, 1])

with col3:
    st.markdown(
        """
        <style>
        .gif-row {
            display:flex;
            justify-content:center;
            gap:6px;
            flex-wrap: wrap;
        }
        </style>

        <div class="gif-row">
            <img src="https://media.giphy.com/media/cKKilkePjBAh0tbmBU/giphy.gif" width="500">
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="gif-row">
            <img src="https://media.giphy.com/media/s3LOGptCH4vgk/giphy.gif" width="400">
        </div>
        """,
        unsafe_allow_html=True
    )

with col1:
    st.title("Aplikasi Deret Angka Lengkap")
    st.caption("Materi + Penyelesai Soal Deret Angka")

menu = st.selectbox(
    "Pilih Menu",
    [
        "Materi Deret Angka",
        "Eksplorasi Deret",
        "Penyelesai Soal"
    ]
)

if menu == "Materi Deret Angka":
    st.header("Materi Dasar Deret Angka")

    st.subheader("Pengertian")
    st.write("""
    Deret angka adalah susunan bilangan yang mengikuti pola tertentu.
    """)

    st.subheader("Jenis Deret Angka")
    st.write("""
    - Deret Aritmatika  
    - Deret Geometri  
    - Deret Fibonacci  
    - Deret Ganjil  
    - Deret Genap  
    """)

elif menu == "Eksplorasi Deret":
    st.header("Eksplorasi Deret Angka")

    jenis = st.selectbox(
        "Pilih Jenis Deret",
        ["Aritmatika", "Geometri", "Fibonacci", "Ganjil", "Genap"]
    )

    n = st.slider("Jumlah suku", 1, 20, 10)

    if jenis == "Aritmatika":
        a = st.number_input("Suku pertama", value=1)
        d = st.number_input("Beda", value=2)
        st.write([a + i*d for i in range(n)])

    elif jenis == "Geometri":
        a = st.number_input("Suku pertama", value=1)
        r = st.number_input("Rasio", value=2)
        st.write([a * (r**i) for i in range(n)])

    elif jenis == "Fibonacci":
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        st.write(fib[:n])

    elif jenis == "Ganjil":
        st.write([2*i + 1 for i in range(n)])

    elif jenis == "Genap":
        st.write([2*i for i in range(n)])

elif menu == "Penyelesai Soal":
    st.header("Penyelesai Soal Deret Angka")

    soal = st.selectbox(
        "Pilih Jenis Soal",
        [
            "Aritmatika",
            "Geometri",
            "Fibonacci",
            "Ganjil",
            "Genap"
        ]
    )

    if soal == "Aritmatika":
        a = st.number_input("a", value=2)
        d = st.number_input("d", value=3)
        n = st.number_input("n", min_value=1, value=5)
        st.success(f"Hasil: {a + (n-1)*d}")

    elif soal == "Geometri":
        a = st.number_input("a", value=2)
        r = st.number_input("r", value=2)
        n = st.number_input("n", min_value=1, value=5)
        st.success(f"Hasil: {a * r**(n-1)}")

    elif soal == "Fibonacci":
        n = st.number_input("n", min_value=1, value=7)
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        st.success(f"Hasil: {fib[n-1]}")

    elif soal == "Ganjil":
        n = st.number_input("n", min_value=1, value=5)
        st.success(f"Hasil: {2*n - 1}")

    elif soal == "Genap":
        n = st.number_input("n", min_value=1, value=5)
        st.success(f"Hasil: {2*n}")
