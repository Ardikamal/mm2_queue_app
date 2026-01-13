import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Sistem Antrian M/M/2 - UNIBBA",
    page_icon="📊",
    layout="centered"
)

# =========================
# HEADER
# =========================
st.markdown(
    """
    <div style="text-align:center;">
        <h1>📊 Aplikasi Sistem Antrian M/M/2</h1>
        <h4>Teori Pemodelan dan Simulasi</h4>
        <p><b>Universitas Bale Bandung (UNIBBA)</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =========================
# IDENTITAS PEMBUAT
# =========================
with st.expander("👤 Identitas Pembuat Program", expanded=True):
    st.write("""
    **Nama:** Ardi Kamal Karima  
    **NIM:** 31230023  
    **Kelas:** 5C  
    **Program Studi:** S1 Teknik Informatika  
    **Fakultas:** Teknologi Informasi  
    **Universitas:** Universitas Bale Bandung (UNIBBA)
    """)

st.markdown("---")

# =========================
# PENJELASAN MODEL
# =========================
st.subheader("📌 Deskripsi Model Antrian")

st.write("""
Model **M/M/2** adalah sistem antrian dengan karakteristik:

- Kedatangan pelanggan mengikuti distribusi **Poisson**
- Waktu pelayanan mengikuti distribusi **Eksponensial**
- Terdapat **2 pelayan (server)**
- Disiplin antrian: **First Come First Served (FCFS)**

Model ini cocok digunakan untuk sistem pelayanan seperti loket bank, kasir, atau layanan administrasi dengan dua petugas.
""")

st.markdown("---")

# =========================
# FORM INPUT
# =========================
st.subheader("📝 Input Parameter Sistem")

st.write("Masukkan nilai waktu rata-rata dalam satuan **menit**.")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        arrival_time = st.number_input(
            "⏳ Waktu Antar Kedatangan (menit)",
            min_value=0.01,
            value=4.0,
            step=0.1,
            help="Rata-rata waktu antara dua pelanggan datang"
        )

    with col2:
        service_time = st.number_input(
            "⚙️ Waktu Pelayanan per Pelayan (menit)",
            min_value=0.01,
            value=3.0,
            step=0.1,
            help="Rata-rata waktu yang dibutuhkan pelayan untuk melayani satu pelanggan"
        )

    submitted = st.form_submit_button("🔍 Hitung Sistem Antrian")

# =========================
# PERHITUNGAN
# =========================
if submitted:

    lam = 1 / arrival_time
    mu = 1 / service_time
    rho = lam / (2 * mu)

    if rho >= 1:
        st.error("❌ Sistem tidak stabil karena nilai utilisasi (ρ) ≥ 1. Silakan ubah parameter input.")
    else:
        W = 1 / (mu - lam / 2)
        Wq = (lam ** 2) / (2 * mu * (mu - lam / 2))

        st.success("✅ Perhitungan berhasil dilakukan")

        st.markdown("---")
        st.subheader("📈 Hasil Perhitungan")

        colA, colB = st.columns(2)

        with colA:
            st.metric("Laju Kedatangan (λ)", f"{lam:.4f} pelanggan/menit")
            st.metric("Laju Pelayanan (μ)", f"{mu:.4f} pelanggan/menit")

        with colB:
            st.metric("Utilisasi Sistem (ρ)", f"{rho:.4f}")
            st.metric("Jumlah Pelayan", "2 Server")

        st.markdown("### ⏱️ Waktu Rata-rata")

        colC, colD = st.columns(2)

        with colC:
            st.metric("Waktu dalam Sistem (W)", f"{W:.4f} menit")

        with colD:
            st.metric("Waktu dalam Antrian (Wq)", f"{Wq:.4f} menit")

        # =========================
        # LANGKAH PERHITUNGAN
        # =========================
        st.markdown("---")
        st.subheader("🧮 Langkah-Langkah Perhitungan")

        st.write("Rumus yang digunakan dalam model antrian M/M/2:")

        st.latex(r"\lambda = \frac{1}{\text{waktu antar kedatangan}}")
        st.latex(r"\mu = \frac{1}{\text{waktu pelayanan}}")
        st.latex(r"\rho = \frac{\lambda}{2\mu}")
        st.latex(r"W = \frac{1}{\mu - \lambda/2}")
        st.latex(r"W_q = \frac{\lambda^2}{2\mu(\mu - \lambda/2)}")

        st.info("""
        Karena aplikasi menggunakan rumus teori antrian secara langsung, maka hasil perhitungan
        akan sama dengan perhitungan manual. Perbedaan hanya akan muncul jika menggunakan simulasi
        berbasis bilangan acak.
        """)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("© 2026 — Aplikasi Sistem Antrian M/M/2 | Fakultas Teknologi Informasi UNIBBA")
