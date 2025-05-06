import streamlit as st
import random

st.title("🎯 Game Tebak Angka (1 - 100)")

# Inisialisasi angka acak di session_state
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.tebakan_terakhir = None
    st.session_state.pesan = ""

# Input dari pengguna
tebakan = st.number_input("Masukkan tebakanmu:", min_value=1, max_value=100, step=1)

if st.button("Tebak"):
    st.session_state.tebakan_terakhir = tebakan

    if tebakan < st.session_state.angka_rahasia:
        st.session_state.pesan = "🔻 Terlalu rendah!"
    elif tebakan > st.session_state.angka_rahasia:
        st.session_state.pesan = "🔺 Terlalu tinggi!"
    else:
        st.session_state.pesan = "🎉 Benar! Kamu menebak angka yang tepat!"

# Tampilkan hasil
if st.session_state.tebakan_terakhir is not None:
    st.write(f"Tebakanmu: **{int(st.session_state.tebakan_terakhir)}**")
    st.success(st.session_state.pesan)

# Tombol untuk mengulang game
if st.button("Ulangi Game"):
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.tebakan_terakhir = None
    st.session_state.pesan = ""
    st.rerun()

