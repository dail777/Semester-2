"""
Aplikasi Streamlit untuk Sistem Antrian Tiket
Dengan login admin/user, pembelian tiket, top-up saldo, dan antrian tiket otomatis.
"""

import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import datetime
from ticket_system import SistemAntrian


st.set_page_config(
    page_title="🎟️ Sistem Antrian Tiket Keren",
    page_icon="🎪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .stMetric {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00D9FF;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00D9FF, #0099FF);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 10px;
        transition: transform 0.2s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.8);
    }
    .header-title {
        text-align: center;
        font-size: 3em;
        background: linear-gradient(90deg, #00D9FF, #0099FF, #FF006E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .info-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #00D9FF;
        margin: 10px 0;
    }
    .status-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
    }
    .status-waiting {
        background-color: #FFA500;
        color: white;
    }
    .status-done {
        background-color: #00FF00;
        color: black;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 10px;
    }
    .chat-bubble {
        padding: 18px;
        border-radius: 20px;
        max-width: 72%;
        line-height: 1.4;
        white-space: pre-wrap;
        word-wrap: break-word;
        margin-bottom: 8px;
    }
    .chat-right {
        background: #0099ff;
        color: white;
        margin-left: auto;
        text-align: right;
    }
    .chat-left {
        background: rgba(255, 255, 255, 0.18);
        color: white;
        margin-right: auto;
        text-align: left;
    }
    .chat-bubble strong {
        display: block;
        margin-bottom: 4px;
        font-size: 0.95rem;
    }
    .chat-bubble p {
        margin: 0;
        padding: 0;
    }
    .chat-meta {
        font-size: 0.78rem;
        color: #ddd;
        margin-top: 4px;
    }
    .chat-notification {
        padding: 18px;
        border-radius: 12px;
        background: rgba(0, 217, 255, 0.12);
        border: 1px solid rgba(0, 217, 255, 0.25);
        margin-bottom: 16px;
    }
    .chat-notification strong {
        display: block;
        margin-bottom: 4px;
        color: #00D9FF;
    }
    .info-box-cancelled {
        border-left: 5px solid #FF4D4D;
        background: rgba(255, 77, 77, 0.08);
    }
    .chat-bubble p {
        margin: 5px 0 0;
        padding: 0;
    }
    .chat-meta {
        font-size: 0.8rem;
        color: #bbb;
        margin-top: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'sistem' not in st.session_state:
    st.session_state.sistem = SistemAntrian(pusat_x=50, pusat_y=50)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.full_name = None

if 'menu' not in st.session_state:
    st.session_state.menu = "🔐 Login"

if 'menu_redirect' not in st.session_state:
    st.session_state.menu_redirect = None


def login_section():
    st.markdown("### 🔐 Login Akun")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Masuk", use_container_width=True):
        username = username.strip()
        if not username or not password:
            st.error("Masukkan username dan password.")
            return
        role = st.session_state.sistem.authenticate(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.user_role = role
            st.session_state.username = username
            user_info = st.session_state.sistem.get_user_info(username)
            st.session_state.full_name = user_info["name"] if user_info else username
            st.session_state.menu_redirect = "🏠 Dashboard Admin" if role == "admin" else "🏠 Dashboard"
            st.success(f"Selamat datang, {st.session_state.full_name}! Role: {role}")
        else:
            st.error("Username atau password salah.")


def register_section():
    st.markdown("### 📝 Registrasi Akun User")
    username = st.text_input("Username baru", key="register_username")
    password = st.text_input("Password baru", type="password", key="register_password")
    name = st.text_input("Nama lengkap", key="register_name")
    saldo = st.number_input("Saldo awal", min_value=0, value=50000, step=10000, key="register_saldo")
    if st.button("Daftar Akun", use_container_width=True):
        username = username.strip()
        name = name.strip()
        if username and password and name:
            result = st.session_state.sistem.register_user(username, password, name, saldo)
            if result:
                st.success("Akun berhasil dibuat! Silakan login.")
            else:
                st.error("Username sudah terpakai atau data tidak lengkap. Silakan coba lagi.")
        else:
            st.error("Lengkapi semua form registrasi.")


def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.full_name = None
    st.success("Anda telah logout.")


def handle_user_chat_submit(username):
    message = st.session_state.user_chat_input.strip()
    if message:
        st.session_state.sistem.send_user_message(username, message)
        st.session_state.sistem.reload_data()
        st.session_state.user_chat_submit_status = "sent"
        st.session_state.user_chat_input = ""
    else:
        st.session_state.user_chat_submit_status = "error"


def handle_admin_chat_submit(chat_id):
    reply = st.session_state.admin_chat_reply.strip()
    if reply:
        st.session_state.sistem.send_admin_message(chat_id, reply)
        st.session_state.sistem.reload_data()
        st.session_state.admin_chat_submit_status = "sent"
        st.session_state.admin_chat_reply = ""
    else:
        st.session_state.admin_chat_submit_status = "error"


def select_admin_chat(chat_id):
    st.session_state.admin_chat_selected = chat_id


def reset_all_chats() -> bool:
    if hasattr(st.session_state.sistem, "reset_chats"):
        return st.session_state.sistem.reset_chats()
    if hasattr(st.session_state.sistem, "db") and hasattr(st.session_state.sistem.db, "reset_chats"):
        st.session_state.sistem.db.reset_chats()
        st.session_state.sistem.reload_data()
        return True
    return False


def handle_user_ticket_purchase(username: str, category: str):
    order = st.session_state.sistem.purchase_ticket(username, category)
    if order:
        st.session_state.sistem.reload_data()
        position = st.session_state.sistem.get_queue_position(order.ticket_number)
        pending = st.session_state.sistem.get_pending_orders()
        has_different_user_ahead = any(
            item.username != username
            for item in pending[:position-1]
        ) if position and position > 2 else False
        warning = " Pemesanan tiket akan dibatalkan dalam 30 detik karena antrian penuh." if has_different_user_ahead else ""
        st.session_state.user_purchase_message = f"Tiket berhasil dibeli! Nomor tiket: {order.ticket_number}. Antrian ke: {position}.{warning}"
    else:
        st.session_state.user_purchase_message = "Saldo tidak cukup atau kategori tidak valid."





def setup_auto_refresh(interval_seconds: int = 3):
    st.session_state.sistem.reload_data()
    components.html(f"""
        <script>
        if (!window.__auto_refresh_active) {{
            window.__auto_refresh_active = true;
            setTimeout(() => window.location.reload(), {interval_seconds * 1000});
        }}
        </script>
    """, height=0)


def render_user_dashboard():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown(f"### 🏠 Dashboard User - {user['name']}")
    setup_auto_refresh()
    st.info("Data akan disegarkan otomatis setiap 3 detik.")

    stats = st.session_state.sistem.get_statistik()
    order_history = st.session_state.sistem.get_user_purchase_history(username)
    chat = st.session_state.sistem.get_user_chat(username)
    chat_notification = None
    if chat:
        last_message = chat.get('messages', [])[-1] if chat.get('messages') else None
        if chat.get('status') == 'Menunggu':
            position = st.session_state.sistem.get_chat_queue_position(chat['chat_id'])
            chat_notification = f"Chat Anda sedang menunggu respon admin." + (f" Antrian ke {position}." if position else "")
        elif last_message and last_message.get('sender') == 'admin':
            chat_notification = "Admin sudah membalas chat Anda. Cek halaman Chat Admin untuk melihat pesan terbaru."
        else:
            chat_notification = "Anda sedang menunggu balasan admin pada chat terakhir Anda."

    col1, col2 = st.columns(2)
    col1.metric("💰 Saldo", f"Rp {user['saldo']:,}")
    col2.metric("🎫 Tiket Dibeli", len(order_history))

    if chat_notification:
        st.markdown(f"<div class='chat-notification'><strong>Notifikasi Chat</strong><span>{chat_notification}</span></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🛍️ Riwayat Pembelian Tiket")
    if order_history:
        for order in reversed(order_history[-10:]):
            queue_info = f"<p><b>Antrian ke:</b> {order['queue_position']}</p>" if order.get('queue_position') else ""
            status_label = order.get('status_label', order['status'])
            order_class = "info-box info-box-cancelled" if order['status'] == 'Dibatalkan' else "info-box"
            st.markdown(f"""
            <div class=\"{order_class}\">
            <h4>🎫 {order['ticket_number']} - {order['category']}</h4>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            <p><b>Status:</b> {status_label}</p>
            {queue_info}
            <p><b>Waktu Pembelian:</b> {order['purchase_time']}</p>
            """ + (f"<p><b>Served by:</b> {order['served_by']} pada {order['served_time']}</p>" if order['status'] == 'Selesai' else "") + (f"<p><b>Ditolak oleh:</b> {order.get('cancelled_by', 'admin')} pada {order.get('cancelled_time', '-')}</p>" if order['status'] == 'Dibatalkan' else "") + "</div>", unsafe_allow_html=True)
    else:
        st.info("Belum ada pembelian tiket.")


def render_user_buy_ticket():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown("### 🎟️ Beli Tiket")
    categories = st.session_state.sistem.get_categories()
    category_names = [cat['name'] for cat in categories]
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Pilih kategori tiket", category_names)
        amount = next((cat['price'] for cat in categories if cat['name'] == category), 0)
        st.write(f"Harga tiket: Rp {amount:,}")
    with col2:
        st.markdown("### Info User")
        st.write(f"Nama: {user['name']}")
        st.write(f"Username: {user['username']}")
        st.write(f"Saldo: Rp {user['saldo']:,}")
    
    if st.button("✅ Beli Tiket", use_container_width=True, key="buy_ticket", on_click=handle_user_ticket_purchase, args=(username, category)):
        pass

    if st.session_state.get("user_purchase_message"):
        st.success(st.session_state.user_purchase_message)
        st.session_state.user_purchase_message = None


def render_user_topup():
    username = st.session_state.username
    st.markdown("### 💳 Top Up Saldo")
    amount = st.number_input("Jumlah top up (Rp)", min_value=0, step=10000)
    if st.button("Top Up Sekarang", use_container_width=True):
        if amount > 0:
            st.session_state.sistem.top_up_balance(username, amount)
            st.success(f"Saldo berhasil ditambah Rp {amount:,}")
        else:
            st.error("Masukkan nominal top up yang valid.")


def render_user_history():
    username = st.session_state.username
    st.markdown("### 📋 Riwayat Pembelian")
    setup_auto_refresh()
    st.info("Riwayat akan disegarkan otomatis setiap 3 detik.")
    history = st.session_state.sistem.get_user_purchase_history(username)
    if history:
        for order in reversed(history[-10:]):
            queue_info = f"<p><b>Antrian ke:</b> {order['queue_position']}</p>" if order.get('queue_position') else ""
            status_label = order.get('status_label', order['status'])
            order_class = "info-box info-box-cancelled" if order['status'] == 'Dibatalkan' else "info-box"
            st.markdown(f"""
            <div class=\"{order_class}\">
            <h4>🎫 {order['ticket_number']} - {order['category']}</h4>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            <p><b>Status:</b> {status_label}</p>
            {queue_info}
            <p><b>Waktu:</b> {order['purchase_time']}</p>
            {f"<p><b>Served by:</b> {order['served_by']} pada {order['served_time']}</p>" if order['status'] == 'Selesai' else ''}
            {f"<p><b>Ditolak oleh:</b> {order.get('cancelled_by', 'admin')} pada {order.get('cancelled_time', '-')}</p>" if order['status'] == 'Dibatalkan' else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada riwayat pembelian.")


def render_user_chat():
    username = st.session_state.username
    st.markdown("### 💬 Chat dengan Admin")
    setup_auto_refresh()
    st.info("Chat akan disegarkan otomatis setiap 3 detik.")

    if "user_chat_input" not in st.session_state:
        st.session_state.user_chat_input = ""
    if "user_chat_submit_status" not in st.session_state:
        st.session_state.user_chat_submit_status = None

    if st.session_state.user_chat_submit_status == "sent":
        st.success("Pesan terkirim ke admin.")
        st.session_state.user_chat_submit_status = None
    elif st.session_state.user_chat_submit_status == "error":
        st.error("Masukkan pesan terlebih dahulu.")
        st.session_state.user_chat_submit_status = None

    chat = st.session_state.sistem.get_user_chat(username)
    if chat:
        status = chat.get('status', 'Menunggu')
        position = st.session_state.sistem.get_chat_queue_position(chat['chat_id'])
        if status == 'Menunggu' and position is not None:
            st.info(f"Chat Anda saat ini berada di antrian ke {position} untuk direspon oleh admin.")
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for message in chat.get('messages', []):
            bubble_class = 'chat-right' if message['sender'] == username else 'chat-left'
            sender_label = 'Anda' if message['sender'] == username else 'Admin'
            st.markdown(f"<div class='chat-bubble {bubble_class}'><strong>{sender_label}</strong><p>{message['text']}</p><div class='chat-meta'>{message['timestamp']}</div></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Belum ada chat dengan admin. Kirim pesan pertama untuk memulai.")

    st.text_area("Tulis pesan untuk admin", key="user_chat_input", height=140)
    st.button("Kirim Pesan", use_container_width=True, key="user_send_chat", on_click=handle_user_chat_submit, args=(username,))


def render_user_account():
    username = st.session_state.username
    user = st.session_state.sistem.get_user_info(username)
    st.markdown("### ⚙️ Informasi Akun")
    st.write(f"Nama: {user['name']}")
    st.write(f"Username: {user['username']}")
    st.write(f"Saldo: Rp {user['saldo']:,}")
    st.markdown("---")
    new_name = st.text_input("Ubah Nama", value=user['name'])
    if st.button("Simpan Nama Baru", use_container_width=True):
        if new_name and new_name != user['name']:
            st.session_state.sistem.update_user_name(username, new_name)
            st.success("Nama berhasil diperbarui.")
        else:
            st.error("Masukkan nama baru yang berbeda.")


def render_admin_dashboard():
    st.markdown("### 🏠 Dashboard Admin")
    setup_auto_refresh()
    st.info("Data admin akan disegarkan otomatis setiap 3 detik.")

    stats = st.session_state.sistem.get_statistik()
    pending_orders = st.session_state.sistem.get_pending_orders()
    order_history = st.session_state.sistem.get_admin_purchase_history()
    pending_chats = st.session_state.sistem.get_pending_chat_count()
    cancelled_orders = [order for order in order_history if order['status'] == 'Dibatalkan']

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("🕒 Pesanan Menunggu", stats['pending'])
    col2.metric("✅ Pesanan Selesai", stats['completed'])
    col3.metric("💰 Total Pendapatan", f"Rp {stats['revenue']:,}")
    col4.metric("📈 Selesai", f"{stats['completion_rate']:.1f}%")
    col5.metric("❌ Pesanan Dibatalkan", stats.get('cancelled', 0))
    
    st.markdown("---")
    st.markdown("### 📋 Riwayat Pembelian Tiket")
    if order_history:
        for order in reversed(order_history[-10:]):
            queue_info = f"<p><b>Antrian ke:</b> {order['queue_position']}</p>" if order.get('queue_position') else ""
            status_label = order.get('status_label', order['status'])
            order_class = "info-box info-box-cancelled" if order['status'] == 'Dibatalkan' else "info-box"
            st.markdown(f"""
            <div class=\"{order_class}\">
            <h4>🎫 {order['ticket_number']} - {order['category']} ({status_label})</h4>
            <p><b>User:</b> {order['username']} - {order['name']}</p>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            {queue_info}
            <p><b>Lokasi:</b> ({order['lokasi_x']}, {order['lokasi_y']})</p>
            <p><b>Waktu:</b> {order['purchase_time']}</p>
            {f"<p><b>Served by:</b> {order['served_by']} pada {order['served_time']}</p>" if order['status'] == 'Selesai' else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada pesan tiket.")

    if cancelled_orders:
        st.markdown("---")
        st.markdown("### ❌ Riwayat Pesanan Dibatalkan")
        for order in reversed(cancelled_orders[-10:]):
            st.markdown(f"""
            <div class=\"info-box info-box-cancelled\">
            <h4>🎫 {order['ticket_number']} - {order['category']} (Dibatalkan)</h4>
            <p><b>User:</b> {order['username']} - {order['name']}</p>
            <p><b>Harga:</b> Rp {order['price']:,}</p>
            <p><b>Waktu Pembelian:</b> {order['purchase_time']}</p>
            <p><b>Ditolak oleh:</b> {order.get('cancelled_by', 'admin')} pada {order.get('cancelled_time', '-')}</p>
            </div>
            """, unsafe_allow_html=True)


def render_admin_serve():
    st.markdown("### 🎫 Status Antrian (Otomatis)")
    st.info("⚙️ Sistem antrian berjalan otomatis: Depan (max 2) dilayani, belakang ditolak otomatis dalam 30 detik.")

    next_order = st.session_state.sistem.get_next_order()
    if next_order:
        st.markdown(f"#### Pesanan Depan Antrian: {next_order.ticket_number}")
        st.write(f"User: {next_order.username}")
        st.write(f"Nama: {next_order.name}")
        st.write(f"Kategori: {next_order.category}")
        st.write(f"Harga: Rp {next_order.price:,}")
        st.success("Pesanan ini sedang diproses otomatis oleh sistem.")
    else:
        st.info("Tidak ada pesanan dalam antrean.")

    st.markdown("---")
    pending = st.session_state.sistem.get_pending_orders()
    if pending:
        st.markdown("### 📍 Antrian Tiket (10 Teratas)")
        for idx, order in enumerate(pending[:10], 1):
            status_color = "🟢" if idx <= 2 else "🔴"
            info = f"{status_color} {idx}. {order.ticket_number} - {order.name} ({order.category}) - Antrian ke: {idx}"
            if idx <= 2:
                st.write(f"<span style='color: green;'>{info}</span>", unsafe_allow_html=True)
            elif idx > 2:
                st.write(f"<span style='color: red;'>{info} (akan ditolak otomatis)</span>", unsafe_allow_html=True)
    else:
        st.info("Tidak ada antrian saat ini.")


def render_admin_categories():
    st.markdown("### 🏷️ Harga Tiket & Kategori")
    categories = st.session_state.sistem.get_categories()
    for category in categories:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"**{category['name']}**")
        with col2:
            new_price = st.number_input(f"Harga {category['name']}", min_value=1000, value=category['price'], step=5000, key=f"cat_{category['name']}")
            if st.button(f"Simpan {category['name']}", key=f"save_{category['name']}"):
                st.session_state.sistem.update_category_price(category['name'], new_price)
                st.success(f"Harga {category['name']} diperbarui.")
    st.markdown("---")
    st.markdown("### ➕ Tambah Kategori Baru")
    name = st.text_input("Nama kategori baru", key="new_category_name")
    price = st.number_input("Harga kategori baru", min_value=1000, value=50000, step=5000, key="new_category_price")
    if st.button("Tambah Kategori", use_container_width=True):
        if name:
            if st.session_state.sistem.add_category(name, price):
                st.success("Kategori baru berhasil ditambahkan.")
            else:
                st.error("Kategori sudah ada.")
        else:
            st.error("Nama kategori tidak boleh kosong.")


def render_admin_user_management():
    st.markdown("### 🧑‍💻 Kelola Akun User")
    users = st.session_state.sistem.db.get_all_users()
    if users:
        user_options = [user['username'] for user in users]
        selected = st.selectbox("Pilih user", user_options)
        user = next((u for u in users if u['username'] == selected), None)
        if user:
            st.write(f"Nama: {user['name']}")
            st.write(f"Saldo: Rp {user['saldo']:,}")
            new_name = st.text_input("Ubah nama user", value=user['name'], key="edit_user_name")
            if st.button("Simpan perubahan", use_container_width=True, key="save_user"):
                if new_name and new_name != user['name']:
                    st.session_state.sistem.update_user_name(user['username'], new_name)
                    st.success("Nama user diperbarui.")
                else:
                    st.error("Masukkan nama baru.")
            if st.button("Hapus akun user", use_container_width=True, key="delete_user"):
                st.session_state.sistem.delete_user(user['username'])
                st.success("Akun user dihapus.")
    else:
        st.info("Belum ada user yang terdaftar.")


def render_admin_reset():
    st.markdown("### 🧹 Reset Riwayat Pembelian")
    st.warning("Reset data ini akan menghapus semua riwayat pesanan tanpa menghapus akun.")
    confirm_reset = st.checkbox(
        "Saya yakin ingin menghapus semua riwayat pesanan dan mengatur ulang posisi pembeli",
        key="confirm_reset_history"
    )
    if st.button("Reset Semua Riwayat", use_container_width=True, key="admin_reset_history"):
        if not confirm_reset:
            st.error("Centang konfirmasi sebelum melakukan reset.")
        elif st.session_state.sistem.reset_history():
            st.success("Semua riwayat pembelian telah direset. Akun tetap tersimpan.")

    st.markdown("---")
    st.markdown("### 🧹 Hapus Riwayat Chat")
    confirm_chat_reset = st.checkbox(
        "Saya yakin ingin menghapus semua riwayat chat pengguna",
        key="confirm_reset_chat"
    )
    if st.button("Hapus Semua Chat", use_container_width=True, key="admin_reset_chat"):
        if not confirm_chat_reset:
            st.error("Centang konfirmasi sebelum menghapus chat.")
        elif reset_all_chats():
            st.success("Semua riwayat chat telah dihapus.")

    st.markdown("---")
    st.markdown("Gunakan fitur ini bila Anda ingin mengosongkan semua riwayat chat tanpa mempengaruhi data pembelian atau akun.")


def render_admin_purchase_stats():
    st.markdown("### 📊 Statistik Pembelian per Tanggal")
    stats = st.session_state.sistem.get_purchase_statistics_by_date()
    if stats:
        for item in stats:
            st.write(f"{item['date']}: Total {item['count']}, Menunggu {item.get('waiting',0)}, Selesai {item.get('completed',0)}, Dibatalkan {item.get('cancelled',0)}")
    else:
        st.info("Belum ada pembelian untuk ditampilkan.")


def render_admin_chat():
    st.markdown("### 💬 Chat Pengguna")
    if "admin_chat_selected" not in st.session_state:
        st.session_state.admin_chat_selected = None

    setup_auto_refresh()
    st.info("Chat pengguna akan disegarkan otomatis setiap 3 detik.")

    if "admin_chat_reply" not in st.session_state:
        st.session_state.admin_chat_reply = ""
    if "admin_chat_submit_status" not in st.session_state:
        st.session_state.admin_chat_submit_status = None

    if st.session_state.admin_chat_submit_status == "sent":
        st.success("Balasan terkirim ke pengguna.")
        st.session_state.admin_chat_submit_status = None
    elif st.session_state.admin_chat_submit_status == "error":
        st.error("Masukkan pesan sebelum mengirim.")
        st.session_state.admin_chat_submit_status = None

    pending_chats = st.session_state.sistem.get_pending_chat_count()
    st.info(f"Ada {pending_chats} chat yang menunggu respon admin.")
    chats = st.session_state.sistem.get_admin_chats()
    if not chats:
        st.info("Belum ada chat dari pengguna.")
        return

    def parse_time(value: str):
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except Exception:
            return datetime.min

    def chat_sort_key(chat):
        status = chat.get("status", "Menunggu")
        created = parse_time(chat.get("created_at", "1970-01-01 00:00:00"))
        updated = parse_time(chat.get("updated_at", chat.get("created_at", "1970-01-01 00:00:00")))
        if status == "Menunggu":
            return (0, created, 0)
        return (1, -updated.timestamp(), created)

    chats = sorted(chats, key=chat_sort_key)

    user_display_names = {}
    chat_ids = []
    for chat in chats:
        user = st.session_state.sistem.get_user_info(chat['username'])
        display_name = user['name'] if user else chat['username']
        user_display_names[chat['chat_id']] = display_name
        chat_ids.append(chat['chat_id'])

    if st.session_state.admin_chat_selected not in chat_ids:
        st.session_state.admin_chat_selected = chat_ids[0]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("#### Daftar Chat")
        for chat_item in chats:
            chat_id = chat_item['chat_id']
            display_name = user_display_names.get(chat_id, chat_item['username'])
            is_selected = st.session_state.admin_chat_selected == chat_id
            button_label = f"{display_name} ({chat_item['status']})"
            if is_selected:
                st.markdown(
                    f"<div style='border:2px solid #00D9FF; padding:10px; border-radius:10px; margin-bottom:8px; background: rgba(0, 217, 255, 0.15);'><strong>{button_label}</strong></div>",
                    unsafe_allow_html=True
                )
            else:
                st.button(button_label, key=f"admin_chat_btn_{chat_id}", on_click=select_admin_chat, args=(chat_id,))

    chat = st.session_state.sistem.get_chat_by_id(st.session_state.admin_chat_selected)
    with col2:
        if chat:
            display_name = user_display_names.get(chat['chat_id'], chat['username'])
            st.markdown(f"#### Obrolan dengan {display_name}")
            if chat.get('status') == 'Menunggu':
                position = st.session_state.sistem.get_chat_queue_position(chat['chat_id'])
                if position is not None:
                    st.info(f"Chat ini berada di antrian ke {position} untuk dibalas.")
            st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
            for message in chat.get('messages', []):
                bubble_class = 'chat-right' if message['sender'] == 'admin' else 'chat-left'
                sender_label = 'Admin' if message['sender'] == 'admin' else display_name
                st.markdown(f"<div class='chat-bubble {bubble_class}'><strong>{sender_label}</strong><p>{message['text']}</p><div class='chat-meta'>{message['timestamp']}</div></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.text_area("Balas chat ini", key="admin_chat_reply", height=140)
            st.button("Kirim Balasan", use_container_width=True, key="admin_send_reply", on_click=handle_admin_chat_submit, args=(chat['chat_id'],))
        else:
            st.info("Chat tidak ditemukan.")


st.markdown('<div class="header-title">🎪 SISTEM ANTRIAN TIKET KEREN 🎪</div>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.markdown("# ⚙️ MENU KONTROL")
    st.markdown("---")
    if st.session_state.menu_redirect:
        st.session_state.menu = st.session_state.menu_redirect
        st.session_state.menu_redirect = None

    if not st.session_state.logged_in:
        options = ["🔐 Login", "📝 Register"]
    elif st.session_state.user_role == "admin":
        pending_chat_count = st.session_state.sistem.get_pending_chat_count()
        chat_label = f"💬 Chat ({pending_chat_count})" if pending_chat_count else "💬 Chat"
        options = ["🏠 Dashboard Admin", "🏷️ Harga Tiket", "🧑‍💻 Kelola User", "🧹 Reset Riwayat", chat_label, "📊 Statistik Pembelian", "📋 Riwayat", "🚪 Logout"]
    else:
        options = ["🏠 Dashboard", "🎫 Beli Tiket", "💳 Top Up", "💬 Chat Admin", "📋 Riwayat", "⚙️ Akun", "🚪 Logout"]

    if st.session_state.menu not in options:
        if st.session_state.menu.startswith("💬 Chat"):
            st.session_state.menu = chat_label
        else:
            st.session_state.menu = options[0]

    menu = st.radio("Menu:", options, key="menu", label_visibility="collapsed")

if not st.session_state.logged_in:
    if menu == "🔐 Login":
        login_section()
    else:
        register_section()
else:
    if menu == "🚪 Logout":
        logout()
    elif st.session_state.user_role == "admin":
        if menu == "🏠 Dashboard Admin":
            render_admin_dashboard()
        elif menu == "🏷️ Harga Tiket":
            render_admin_categories()
        elif menu == "🧑‍💻 Kelola User":
            render_admin_user_management()
        elif menu == "🧹 Reset Riwayat":
            render_admin_reset()
        elif menu.startswith("💬 Chat"):
            render_admin_chat()
        elif menu == "📊 Statistik Pembelian":
            render_admin_purchase_stats()
        elif menu == "📋 Riwayat":
            st.markdown("### 📋 Riwayat Semua Pembelian")
            render_admin_dashboard()
    else:
        if menu == "🏠 Dashboard":
            render_user_dashboard()
        elif menu == "🎫 Beli Tiket":
            render_user_buy_ticket()
        elif menu == "💳 Top Up":
            render_user_topup()
        elif menu == "💬 Chat Admin":
            render_user_chat()
        elif menu == "📋 Riwayat":
            render_user_history()
        elif menu == "⚙️ Akun":
            render_user_account()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
<p>🎪 <b>Sistem Antrian Tiket Keren</b> 🎪</p>
<p>Implementasi Queue & JSON Database</p>
<p>Antrian Otomatis: Depan dilayani, Belakang ditolak 30 detik</p>
<p>Powered by Streamlit ✨</p>
</div>
""", unsafe_allow_html=True)
