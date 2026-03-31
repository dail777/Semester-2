import streamlit as st
from datetime import datetime

# Inisialisasi session state
if 'users' not in st.session_state:
    st.session_state.users = {
        'penjual1': {'nama': 'Toko ABC', 'role': 'penjual', 'password': '1234'},
        'pembeli1': {'nama': 'Budi', 'role': 'pembeli', 'password': '1234'}
    }

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if 'products' not in st.session_state:
    st.session_state.products = [
        {'id': 1, 'nama': 'Laptop', 'harga': 5000000, 'penjual': 'penjual1', 'deskripsi': 'Laptop gaming'},
        {'id': 2, 'nama': 'Mouse', 'harga': 150000, 'penjual': 'penjual1', 'deskripsi': 'Mouse wireless'},
        {'id': 3, 'nama': 'Keyboard', 'harga': 300000, 'penjual': 'penjual1', 'deskripsi': 'Mechanical keyboard'}
    ]

if 'chats' not in st.session_state:
    st.session_state.chats = []

if 'cart' not in st.session_state:
    st.session_state.cart = []

# Fungsi login
def login(username, password):
    if username in st.session_state.users:
        if st.session_state.users[username]['password'] == password:
            st.session_state.current_user = username
            return True
    return False

# Fungsi logout
def logout():
    st.session_state.current_user = None

# Halaman Login
def page_login():
    st.title("🛍️ Shopping App")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("### Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if login(username, password):
                st.success("Login berhasil!")
                st.rerun()
            else:
                st.error("Username atau password salah")
    
    with col2:
        st.write("### Demo Akun")
        st.write("**Penjual:**")
        st.code("Username: penjual1\nPassword: 1234")
        st.write("**Pembeli:**")
        st.code("Username: pembeli1\nPassword: 1234")

# Halaman Produk (Pembeli)
def page_products():
    st.title("📦 Daftar Produk")
    
    for product in st.session_state.products:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{product['nama']}** - Rp {product['harga']:,.0f}")
            st.write(f"_{product['deskripsi']}_")
        with col2:
            if st.button("Beli", key=f"buy_{product['id']}"):
                st.session_state.cart.append(product)
                st.success("Ditambahkan ke keranjang!")
        st.divider()

# Halaman Keranjang (Pembeli)
def page_cart():
    st.title("🛒 Keranjang")
    
    if not st.session_state.cart:
        st.info("Keranjang kosong")
        return
    
    total = 0
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{item['nama']} - Rp {item['harga']:,.0f}")
        with col2:
            if st.button("Hapus", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
        total += item['harga']
    
    st.divider()
    st.write(f"**Total: Rp {total:,.0f}**")
    if st.button("Checkout"):
        st.success("Pesanan berhasil! Hubungi penjual untuk konfirmasi.")
        st.session_state.cart = []
        st.rerun()

# Halaman Chat
def page_chat():
    st.title("💬 Chat")
    current_role = st.session_state.users[st.session_state.current_user]['role']
    
    if current_role == 'pembeli':
        st.write("**Chat dengan Penjual**")
        other_user = 'penjual1'
    else:
        st.write("**Chat dengan Pembeli**")
        other_user = 'pembeli1'
    
    # Tampilkan pesan
    for chat in st.session_state.chats:
        if (chat['from'] == st.session_state.current_user and chat['to'] == other_user) or \
           (chat['from'] == other_user and chat['to'] == st.session_state.current_user):
            if chat['from'] == st.session_state.current_user:
                st.write(f"**Anda**: {chat['message']} _{chat['time']}_")
            else:
                st.write(f"**{st.session_state.users[other_user]['nama']}**: {chat['message']} _{chat['time']}_")
    
    # Input pesan baru
    message = st.text_input("Ketik pesan...")
    if st.button("Kirim"):
        if message.strip():
            st.session_state.chats.append({
                'from': st.session_state.current_user,
                'to': other_user,
                'message': message,
                'time': datetime.now().strftime("%H:%M")
            })
            st.rerun()

# Halaman Kelola Produk (Penjual)
def page_seller():
    st.title("🏪 Kelola Produk")
    
    with st.form("add_product"):
        st.write("### Tambah Produk Baru")
        nama = st.text_input("Nama Produk")
        harga = st.number_input("Harga", min_value=0)
        deskripsi = st.text_input("Deskripsi")
        submit = st.form_submit_button("Tambah Produk")
        
        if submit:
            if nama and harga > 0:
                new_id = max([p['id'] for p in st.session_state.products]) + 1
                st.session_state.products.append({
                    'id': new_id,
                    'nama': nama,
                    'harga': harga,
                    'penjual': st.session_state.current_user,
                    'deskripsi': deskripsi
                })
                st.success("Produk berhasil ditambahkan!")
                st.rerun()
    
    st.divider()
    st.write("### Produk Anda")
    for product in st.session_state.products:
        if product['penjual'] == st.session_state.current_user:
            st.write(f"**{product['nama']}** - Rp {product['harga']:,.0f}")

# Main App
def main():
    if st.session_state.current_user is None:
        page_login()
    else:
        # Sidebar
        with st.sidebar:
            st.write(f"**User**: {st.session_state.users[st.session_state.current_user]['nama']}")
            st.write(f"**Role**: {st.session_state.users[st.session_state.current_user]['role']}")
            
            current_role = st.session_state.users[st.session_state.current_user]['role']
            
            if current_role == 'pembeli':
                page = st.radio("Menu", ["Produk", "Keranjang", "Chat"])
            else:
                page = st.radio("Menu", ["Kelola Produk", "Chat"])
            
            if st.button("Logout"):
                logout()
                st.rerun()
        
        # Tampilkan halaman sesuai pilihan
        if current_role == 'pembeli':
            if page == "Produk":
                page_products()
            elif page == "Keranjang":
                page_cart()
            else:
                page_chat()
        else:
            if page == "Kelola Produk":
                page_seller()
            else:
                page_chat()

if __name__ == "__main__":
    main()
