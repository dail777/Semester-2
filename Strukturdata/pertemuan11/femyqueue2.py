import streamlit as st
from gtts import gTTS
import playsound

# Judul
st.title("Antrian Klinik")
st.write("Masukkan nama pasien untuk mendaftar antrian klinik.")

# Inisialisasi session state
if "antrian" not in st.session_state:
    st.session_state.antrian = []

# Input nama pasien
nama = st.text_input("Nama Pasien:")

# Tombol daftar
if st.button("Daftar Antrian"):
    if nama.strip() != "":
        st.session_state.antrian.append(nama)
        st.success(f"{nama} berhasil didaftarkan dalam antrian.")
    else:
        st.error("Nama pasien tidak boleh kosong.")

# Tombol panggil
if st.button("Panggil Antrian"):
    if len(st.session_state.antrian) > 0:
        pasien = st.session_state.antrian.pop(0)

        # Text to speech
        tts = gTTS(text=f"Pasien {pasien} silakan masuk", lang="id")
        file_audio = "panggil.mp3"
        tts.save(file_audio)

        st.info(f"Pasien yang dipanggil: {pasien}")

        # Play audio di Streamlit
        playsound.playsound(file_audio)

    else:
        st.warning("Antrian kosong.")

# Tampilkan antrian
st.subheader("Daftar Antrian")

if len(st.session_state.antrian) > 0:
    for i, pasien in enumerate(st.session_state.antrian, start=1):
        st.write(f"{i}. {pasien}")
else:
    st.write("Belum ada antrian.")