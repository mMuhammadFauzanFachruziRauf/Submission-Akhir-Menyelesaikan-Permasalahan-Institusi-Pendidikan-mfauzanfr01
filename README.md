# Proyek Akhir: Prediksi Mahasiswa Dropout untuk Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan tinggi bereputasi, menghadapi tantangan signifikan berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya (*dropout*). Hal ini berdampak pada reputasi dan efisiensi institusi.

### Permasalahan Bisnis
Institusi ingin dapat mengidentifikasi mahasiswa yang berpotensi *dropout* sedini mungkin agar dapat memberikan bimbingan khusus dan mengurangi angka *dropout* secara keseluruhan.

### Cakupan Proyek
Proyek ini bertujuan membangun solusi data science yang mencakup analisis faktor-faktor penyebab *dropout*, pengembangan model prediksi, serta pembuatan dashboard monitoring untuk membantu manajemen mengambil keputusan berbasis data.

### Persiapan
- **Sumber Data:** [Students' Performance Dataset](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention)
- **Setup Environment:** `pip install -r requirements.txt`

## Business Dashboard
Sebuah dashboard monitoring interaktif telah dibuat menggunakan Looker Studio untuk memberikan gambaran umum mengenai performa siswa. Dashboard ini memvisualisasikan metrik kunci seperti tingkat dropout, serta menganalisis hubungannya dengan faktor ekonomi (status UKT) dan faktor akademik (SKS lulus).

**Link Dashboard:** [https://lookerstudio.google.com/reporting/c719d033-4599-4fd1-be23-642d173cf0fb]

## Menjalankan Sistem Machine Learning
Prototipe sistem machine learning telah dibuat dalam bentuk aplikasi web menggunakan Streamlit. Aplikasi ini memungkinkan pengguna (staf/dosen) untuk memasukkan data seorang mahasiswa dan mendapatkan prediksi status dropout secara real-time.

Aplikasi dapat diakses secara online melalui link berikut:

**Link Aplikasi:** [https://cruxzr7iwodidyg9f49rqp.streamlit.app/]

## Conclusion
Berdasarkan analisis data dan pemodelan, terbukti bahwa faktor ekonomi (status pembayaran UKT) dan performa akademik di semester awal (jumlah SKS yang disetujui) adalah prediktor terkuat untuk kasus *dropout* mahasiswa. Model *Random Forest* yang dikembangkan berhasil mencapai performa yang baik (Accuracy ~88%, Recall ~73%) dan mampu menjadi alat bantu yang efektif bagi Jaya Jaya Institut untuk melakukan deteksi dini.

### Rekomendasi Action Items
1.  **Implementasikan Sistem Peringatan Dini Keuangan:** Secara proaktif identifikasi mahasiswa yang mulai menunggak pembayaran UKT pada bulan-bulan awal. Tawarkan program konseling keuangan atau skema cicilan sebelum masalah berlanjut, karena ini adalah prediktor *dropout* nomor satu.
2.  **Program Mentoring Akademik Semester Awal:** Bentuk program di mana mahasiswa baru dipantau performa akademiknya di semester 1 dan 2. Mahasiswa yang jumlah SKS lulusnya rendah harus segera dimasukkan ke dalam program bimbingan atau tutorial tambahan.
3.  **Gunakan Dashboard untuk Evaluasi Rutin:** Manajemen dan dekanat harus menggunakan dashboard yang telah dibuat sebagai alat evaluasi bulanan untuk melacak tren dan mengidentifikasi program studi atau demografi mahasiswa yang memiliki tingkat risiko *dropout* lebih tinggi.
