# Import tool yang akan digunakan
import streamlit as st

# Konfigurasi tampilan tab halaman
st.set_page_config(
    page_title="Diagnosa Covid",
    page_icon="☢️",
)

# Menambahkan judul di dalam halaman
st.title("Diagnosa")

# Memeriksa apakah variabel "my_input" sudah ada di session state
if "my_input" not in st.session_state:
    # Jika belum ada, maka variabel "my_input" akan bernilai kosong
    st.session_state["my_input"] = ""

# Menampilkan text diikuti dengan nilai dari "my_input"
st.write("Hai, ", st.session_state["my_input"])

# Menampilakn text
st.write("Silakan isi form berikut ini untuk mendiagnosis")

# Deklarasi fungsi "diagnosis_covid" dan memiliki 13 parameter gejala covid
def diagnosis_covid(hidung, kepala, batuk, tenggorokan, demam, badan, perasa, bau, napas, dada, diare, mata, ruam):
    # Jika demam, batuk, dan kesulitan napas ada, maka kemungkinan covid besar
    if demam == "Ada" and batuk == "Ada" and napas == "Ada":
        return "Kemungkinan Covid: Besar"
    # Jika demam ada dan hilangnya perasa atau hilangnya indera penciuman ada, maka kemungkinan covid besar
    elif demam == "Ada" and (perasa == "Ada" or bau == "Ada"):
        return "Kemungkinan Covid: Besar"
    # Jika kesulitan napas ada dan nyeri dada atau batuk ada, maka kemungkinan covid besar
    elif napas == "Ada" and (dada == "Ada" or batuk == "Ada"):
        return "Kemungkinan Covid: Besar"
    # Jika batuk, sakit tenggorokan, atau hidung berair ada, maka kemungkinan covid sedang
    elif batuk == "Ada" or tenggorokan == "Ada" or hidung == "Ada":
        return "Kemungkinan Covid: Sedang"
    # Jika demam, sakit kepala, atau tubuh lemas ada, maka kemungkinan covid sedang
    elif demam == "Ada" or kepala == "Ada" or badan == "Ada":
        return "Kemungkinan Covid: Sedang"
    # Jika demam dan batuk ada, maka kemungkinan covid sedang
    elif demam == "Ada" and batuk == "Ada":
        return "Kemungkinan Covid: Sedang"
    # Jika demam dan muncul ruam kulit, diare, atau mata merah, maka kemungkinan covid sedang
    elif demam == "Ada" and (ruam == "Ada" or diare == "Ada" or mata == "Ada"):
        return "Kemungkinan Covid: Sedang"
    # Jika tidak ada gejala di atas, maka kemungkinan covid rendah
    else:
        return "Kemungkinan Covid: Rendah"

# Membuat radio button dengan 2 pilihan (Tidak dan Ada) untuk setiap gejala
demam = st.radio("Demam:", ["Tidak", "Ada"])
batuk = st.radio("Batuk:", ["Tidak", "Ada"])
hidung = st.radio("Hidung Berair:", ["Tidak", "Ada"])
kepala = st.radio("Sakit Kepala:", ["Tidak", "Ada"])
tenggorokan = st.radio("Sakit Tenggorokan:", ["Tidak", "Ada"])
badan = st.radio("Tidak Enak Badan:", ["Tidak", "Ada"])
perasa = st.radio("Hilangnya kemampuan indera perasa:", ["Tidak", "Ada"])
bau = st.radio("Hilangnya Kemampuan untuk Mencium Bau:", ["Tidak", "Ada"])
napas = st.radio("Sesak Napas:", ["Tidak", "Ada"])
dada = st.radio("Nyeri Dada:", ["Tidak", "Ada"])
diare = st.radio("Diare:", ["Tidak", "Ada"])
mata = st.radio("Konjungtivitis (Mata Merah):", ["Tidak", "Ada"]) 
ruam = st.radio("Ruam di Kuliat:", ["Tidak", "Ada"])

# Memeriksa apakah tombol "Diagnosa" sudah ditekan 
if st.button("Diagnosa"):
    # Memanggil fungsi "diagnosis_covid" dengan parameter yang telah ditetapkan
    result = diagnosis_covid(hidung, kepala, batuk, tenggorokan, demam, badan, perasa, bau, napas, dada, diare, mata, ruam)
    # Menampilkan hasil diagnosa dari fungsi "diagbosis_covid" 
    st.write(result)
    # Menampilkan text
    st.write("Untuk mengetahui cara meredakan gejala Covid, silakan ke halaman Penanganan")