# 📈 Customer Deposit Purchase Prediction – DataQuest DSI 2025

![](/image/bank-deposit.png "Bank Deposit")

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![AUC Score](https://img.shields.io/badge/AUC%20Score-75.38%25-orange.svg)
![Tools](https://img.shields.io/badge/Tools-TabNet%20%7C%20scikit--learn%20%7C%20pandas-lightgrey.svg)

Proyek ini bertujuan membangun model *machine learning* berbasis **TabNet Regressor** untuk memprediksi kemungkinan seorang nasabah akan membeli produk **deposito berjangka**, berdasarkan data demografis dan interaksi selama kampanye pemasaran bank.

## Tujuan

Mengklasifikasikan nasabah ke dalam dua kelas:

- `1`: Diprediksi **akan membeli** deposito berjangka
- `0`: Diprediksi **tidak akan membeli** deposito berjangka

## Teknologi yang Digunakan

- Python 3.9+
- [TabNet (PyTorch Tabular)](https://github.com/dreamquark-ai/tabnet)
- Scikit-learn
- Pandas
- Matplotlib & Seaborn

## Struktur Dataset

Dataset terdiri dari 21 fitur dan 1 label (`berlangganan_deposito`). Fitur `customer_number` hanya digunakan di data uji (testing set).

**Contoh Kolom:**

| Kolom                         | Deskripsi Singkat                                    |
| ----------------------------- | ---------------------------------------------------- |
| `usia`                      | Usia nasabah dalam tahun                             |
| `pekerjaan`                 | Jenis pekerjaan nasabah                              |
| `status_perkawinan`         | Status perkawinan (termasuk cerai/janda/duda)        |
| `gagal_bayar_sebelumnya`    | Apakah pernah gagal bayar                            |
| `pinjaman_rumah`            | Status kepemilikan pinjaman rumah                    |
| `jenis_kontak`              | Media komunikasi dengan nasabah                      |
| `durasi_kontak`             | Durasi kontak terakhir (tidak digunakan dalam model) |
| `hasil_kampanye_sebelumnya` | Hasil kampanye sebelumnya                            |
| `berlangganan_deposito`     | Target klasifikasi (0/1)                             |

## Eksplorasi Data (EDA)

Notebook melakukan:

- Informasi dan statistik awal dataset
- Cek nilai hilang
- Distribusi numerik dengan KDE Plot
- Distribusi kategorikal dengan bar chart

## Hasil Akhir

Model mencapai skor **AUC = 75.38%** pada data validasi. Model telah ditingkatkan performanya melalui *hyperparameter tuning*.

## Instalasi & Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/aliffaturrohman/python_labs.git
cd python_labs/project/Costumer_deposit_prediction/
```

### 2. Install Library yang Dibutuhkan

```bash
pip install pandas matplotlib seaborn numpy gdown
```

### 3. Unduh Dataset

```python
# Jalankan di Jupyter Notebook / Colab
!gdown --id 1QlOEmXTwpQpCf2F8nA1GdnbTxrXrVRtu # validation_set.csv
!gdown --id 1ypgjcxdI0IMpLA2bQGrI02HaVG9afS0X # training_dataset.csv
```

### 4. Jalankan Notebook

Buka file `DCM_DMU_2025_Notebook_Pengen aja.ipynb` di Jupyter Notebook/JupyterLab dan jalankan semua sel secara berurutan.

![](/image/dataquest-auc-score.jpg "Dataquest auc score")

## Kontributor

[Alif Faturrohman](https://github.com/aliffaturrohman)

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT) – silakan digunakan dan dimodifikasi sesuai kebutuhan.
