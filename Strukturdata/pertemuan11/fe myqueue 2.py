import queue
import streamlit as st
import gtts
import playsound

#antrian klinik
st.title("Antrian Klinik")
st.write("Masukkan nama pasien untuk mendaftar antrian klinik.")
#inisiasi state
if 'antrian' not in st.session_state:
    st.session_state.antrian = queue.Queue()

#membuat tombol untuk mendaftar antrian
input_antrian = st.text_input("Nama Pasien:")
if st.button("Daftar Antrian"):
    if input_antrian:
        st.session_state.antrian.put(input_antrian)
        st.success(f"{input_antrian} berhasil didaftarkan dalam antrian.")
    else:
        st.error("Nama pasien tidak boleh kosong.")
#membuat tombol panggil antrian
if st.button("Panggil Antrian"):
    if not st.session_state.antrian.empty():
        pasien_dipanggil = st.session_state.antrian.get()
        tts = gtts.gTTS(pasien_dipanggil, lang='id')
        tts.save("panggil_antrian.mp3")
        playsound.playsound("panggil_antrian.mp3")
        st.info(f"Pasien yang dipanggil: {pasien_dipanggil}")
    else:
        st.warning("Antrian kosong. Tidak ada pasien yang dapat dipanggil.")

#menampilkan antrian
st.subheader("Antrian:")
current = st.session_state.antrian.queue
while current:
    st.write(current[0])
    current = current[1:]
