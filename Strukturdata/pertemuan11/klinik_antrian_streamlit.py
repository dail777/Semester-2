import tempfile
from pathlib import Path

import streamlit as st
from gtts import gTTS


def initialize_state():
    if "queue" not in st.session_state:
        st.session_state.queue = []
    if "next_number" not in st.session_state:
        st.session_state.next_number = 1
    if "last_audio_bytes" not in st.session_state:
        st.session_state.last_audio_bytes = None


def format_queue_number(number: int) -> str:
    return f"A{number:03d}"


def create_announcement_text(item: dict) -> str:
    return (
        f"Antrian nomor {item['nomor']} untuk {item['nama']} "
        f"di layanan {item['jenis']} dipanggil. Silakan masuk ke ruang pemeriksaan."
    )


def generate_audio(text: str) -> bytes:
    tts = gTTS(text=text, lang="id")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts_name = tmp.name
    tts.save(tts_name)
    tmp_path = Path(tts_name)
    audio_bytes = tmp_path.read_bytes()
    tmp_path.unlink(missing_ok=True)
    st.session_state.last_audio_bytes = audio_bytes
    return audio_bytes


def add_to_queue(nama: str, jenis: str):
    nomor = format_queue_number(st.session_state.next_number)
    st.session_state.queue.append({
        "nomor": nomor,
        "nama": nama,
        "jenis": jenis,
    })
    st.session_state.next_number += 1


def call_next_queue():
    if not st.session_state.queue:
        st.warning("Tidak ada antrian. Tambahkan pasien terlebih dahulu.")
        return None, None

    item = st.session_state.queue.pop(0)
    announcement = create_announcement_text(item)
    audio_bytes = generate_audio(announcement)
    return item, audio_bytes


def main():
    st.set_page_config(
        page_title="Aplikasi Antrian Klinik",
        page_icon="🩺",
        layout="centered",
    )

    initialize_state()

    st.title("Aplikasi Antrian Klinik")
    st.write(
        "Aplikasi ini dapat menambahkan antrian pasien, memanggil antrian berikutnya, "
        "dan memutar suara panggilan berdasarkan nomor antrian dan nama pasien."
    )

    with st.form("add_queue_form"):
        nama = st.text_input("Nama Pasien", max_chars=50)
        jenis = st.selectbox(
            "Jenis Layanan",
            ["Umum", "BPJS", "Gigi", "Anak", "KIA", "Laboratorium"],
        )
        submitted = st.form_submit_button("Tambah Antrian")

    if submitted:
        if not nama.strip():
            st.error("Masukkan nama pasien terlebih dahulu.")
        else:
            add_to_queue(nama.strip(), jenis)
            st.success(f"Antrian {st.session_state.queue[-1]['nomor']} atas nama {nama} berhasil ditambahkan.")

    st.markdown("---")
    st.subheader("Daftar Antrian Saat Ini")

    if st.session_state.queue:
        st.table(st.session_state.queue)
    else:
        st.info("Belum ada pasien di antrian.")

    st.markdown("---")
    st.subheader("Panggil Antrian")

    if st.button("Panggil Antrian Berikutnya"):
        item, audio_bytes = call_next_queue()
        if item:
            st.success(f"Memanggil {item['nomor']} atas nama {item['nama']} ({item['jenis']}).")
            st.audio(audio_bytes, format="audio/mp3")

    if st.session_state.last_audio_bytes and st.button("Putar Ulang Panggilan Terakhir"):
        st.audio(st.session_state.last_audio_bytes, format="audio/mp3")

    st.markdown("---")
    st.caption("Gunakan aplikasi ini dengan koneksi internet karena gTTS memerlukan akses layanan Google.")


if __name__ == "__main__":
    main()
