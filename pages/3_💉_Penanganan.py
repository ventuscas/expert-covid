# Import tool yang ingin digunakan
import streamlit as st

# Konfigurasi tampilan tab halaman
st.set_page_config(
    page_title="Diagnosa Covid",
    page_icon="☢️",
)

# Menambahkan judul di dalam halaman
st.title("Pengobatan Infeksi Covid")

# Menambahkan text
st.write("1. Meminum obat pereda nyeri tanpa resep, untuk mengurangi rasa sakit, demam, dan batuk. Namun, jangan berikan aspirin pada anak-anak. Selain itu, jangan berikan obat batuk pada anak di bawah empat tahun.")
st.write("2. Gunakan pelembap ruangan atau mandi air hangat untuk membantu meredakan sakit tenggorokan dan batuk.")
st.write("3. Perbanyak istirahat")
st.write("4. Perbanyak asupan cairan tubuh.")
st.write("5. Isolasi mandiri.")
st.write("6. Serial foto toraks sesuai indikasi.")
st.write("7. Terapi simptomatik.")
st.write("8. Terapi cairan.")
st.write("9. Ventilator mekanik (bila gagal napas).")
st.write("10. Antibiotik, jika disertai infeksi bakteri")

# Menambahkan judul di dalam halaman
st.title("Kapan Harus ke Dokter?")

# Menambahkan text
st.write("Jika gejala-gejala infeksi coronavirus Covid tak kunjung membaik dalam hitungan hari atau semakin memburuk, pastikan untuk langsung mengunjungi dokter.")