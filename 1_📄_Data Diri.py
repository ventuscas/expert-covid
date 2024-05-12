# Import tool yang akan digunakan
import streamlit as st

# Konfigurasi tampilan tab halaman
st.set_page_config(
    page_title="Diagnosa Covid",
    page_icon="☢️",
)

# Menambahkan judul di dalam halaman
st.title("Data Diri")

# Memeriksa apakah variabel "my_input" sudah ada di session state
if "my_input" not in st.session_state:
    # Jika belum ada, maka variabel "my_input" akan bernilai kosong
    st.session_state["my_input"] = ""

# Membuat input text
my_input = st.text_input("Masukkan Nama", st.session_state["my_input"])

# Membuat tombol submit
submit = st.button("Submit")

# Mengecek apakah tombol submit sudah ditekan
if submit:
    # Mengupdate nilai dari "my_input" dengan nilai yang baru diinput
    st.session_state["my_input"] = my_input
    # Menampilkan text diikuti dengan nilai dari "my_input"
    st.write("Namamu adalah: ", my_input)
    # Menampilkan text
    st.write("Silakan lakukan diagnosa mandiri di halaman diagnosa")