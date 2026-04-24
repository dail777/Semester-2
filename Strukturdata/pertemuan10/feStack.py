#visualisasi konsep stack dengan menggunakan streamlit
import streamlit as st
import stack
st.title("Visualisasi Stack dengan Streamlit")
#instance stack
mystack = stack.Stack()
#input data untuk push
data = st.text_input("Masukkan data untuk push:")
if st.button("Push"):
    mystack.push(data)
    st.success(f"Data '{data}' berhasil di-push ke stack.")
if st.button("Pop"):
    popped_data = mystack.pop()
    if popped_data is not None:
        st.success(f"Data '{popped_data}' berhasil di-pop dari stack.")
    else:
        st.warning("Stack kosong. Tidak ada data untuk di-pop.")

st.subheader("Isi Stack:")
current = mystack.top
while current:
    st.write(current.data)
    current = current.next
