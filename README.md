# Analisis dan Evaluasi Performa Pemain NBA untuk Mendukung Pengambilan Keputusan Scouting dan Trading Tim San Antonio Spurs

![San Antonio Spurs Logo](images/Banner.jpeg)

## 🗂 Repository Structure

- `dags/`  
  &nbsp;&nbsp;&nbsp;&nbsp;└─ `NBAPlayer_Preference_DAG.py` — Script DAG untuk workflow Airflow  
- `Data_Clean/`  
  &nbsp;&nbsp;&nbsp;&nbsp;└─ `NBA_Player_Data_Clean.csv` — Data setelah dibersihkan  
- `Dataset_Asli/`  
  &nbsp;&nbsp;&nbsp;&nbsp;└─ `NBA_Player_Stats.csv`, `NBA_Player_Stats_2.csv` 
- `gx/`  
  &nbsp;&nbsp;&nbsp;&nbsp;└─ Great Expectations project: checkpoints, expectations, dll  
- `images/`  
  &nbsp;&nbsp;&nbsp;&nbsp;└─ Screenshot visualisasi Kibana + `spurs.png`  
- `logs/`  
  &nbsp;&nbsp;&nbsp;&nbsp;└─ Log dari eksekusi Airflow  
- `config/airflow.cfg`  
- `docker-compose.yaml` — Konfigurasi Docker  
- `Dockerfile.airflow` — Dockerfile khusus Airflow  
- `NBA_Player_Data_Raw.csv` — Data mentah awal  
- `NBAPlayer_Preference_DAG_Graph.png` — Screenshot graph DAG  
- `NBAPlayer_Preference_DDL.txt` — SQL untuk DDL dan DML  
- `NBAPlayer_Preference_GX.ipynb` — Notebook validasi dengan Great Expectations  
- `NBAPlayer_Preference_Presentation.pptx` — File presentasi  
- `README.md` — Dokumentasi utama project  

---

## Problem Background

Manajemen tim San Antonio Spurs berencana melakukan perombakan roster untuk musim 2023 dengan tujuan meningkatkan performa tim secara menyeluruh. Salah satu kebutuhan utama adalah melakukan evaluasi data performa pemain NBA yang dapat membantu proses **scouting** dan **trading** secara objektif.  
Statistik historis dari berbagai posisi (PG, SG, SF, PF, C) akan dianalisis untuk menemukan pemain dengan performa terbaik sesuai kebutuhan tim.

---

## Objective

Memberikan insight berbasis data terhadap performa pemain NBA dari tahun ke tahun. Insight akan digunakan oleh:
- **Manajemen Tim**
- **Tim Scouting**
- **Pelatih**

Dalam proses:
- **Scouting pemain**
- **Pertukaran pemain (trading)**
- **Strategi formasi & rotasi line-up**

---

## Data

Dataset: [NBA Player Stats 2018–2022](https://www.kaggle.com/datasets/raunakpandey030/nba-player-stats)  
Dataset berisi informasi penting terkait statistik pemain NBA seperti:
- Minutes Played, Field Goals, FG%, 3P%, Rebounds, Assists, Turnovers, Points
- Terdapat campuran data kategorikal (Posisi, Team, Nama) dan numerikal (statistik performa)

Dataset dibersihkan dari:
- Duplikasi data
- Missing values
- Format kolom dinormalisasi
- Kolom baru ditambahkan untuk keperluan validasi

---

## Methodology

1. **ETL Pipeline**
   - Ekstraksi data dari CSV ke PostgreSQL
   - Transformasi (pembersihan, normalisasi, validasi)
   - Load ke Elasticsearch

2. **Orkestrasi Workflow**
   - Menggunakan Apache Airflow DAG dengan 3 task utama:
     - `fetch_from_postgres`
     - `clean_data`
     - `post_to_elasticsearch`

3. **Validasi Data**
   - Menggunakan `Great Expectations` dengan 7 jenis expectations berbeda untuk memastikan kualitas data

4. **Visualisasi**
   - Menggunakan Kibana untuk analisis visual dan insight pemain unggulan
   - Insight meliputi: Top 10 Pemain per-posisi, top turnover, Poin per-game pemain dari tahun ke tahun, Top 3 Pointer, Pemain Starter - Non Starter dan rebound tertinggi

---

## Tech Stack

- **Bahasa**: Python
- **Workflow Orchestration**: Apache Airflow
- **Database**: PostgreSQL
- **Search & Visualization**: Elasticsearch & Kibana
- **Environment**: Docker Compose
- **Code Editor**: VS Code

### Library:
- `airflow` — orkestrasi DAG
- `pandas` — manipulasi data
- `psycopg2` — koneksi PostgreSQL
- `elasticsearch`, `helpers` — push data ke ES
- `great_expectations` — validasi data

---

## Project Output

- Data pemain NBA bersih dalam format `.csv`
- File DAG Airflow yang terjadwal otomatis
- Data clean berhasil masuk ke Elasticsearch
- Dashboard Kibana dengan insight:
  - Top 10 Pemain berdasarkan posisi
  - Pemain Starter dan Non Starter di Tim San Antonio Spurs
  - Top Rebounder
  - Pemain dengan 3 Point terbanyak
  - Turnover terbanyak
  - Trend pemain berdasarkan point per game
- Rekomendasi lanjutan untuk manajemen Spurs

---

## Dokumentasi Visual

- Screenshot DAG (sukses semua task)
- 10+ visualisasi dan insight pada Kibana
- Markdown Kibana untuk identitas & kesimpulan

---

## References

- Penulisan markdown: https://docs.github.com/en/get-started/writing-on-github
- Airflow DAG + Tutorial:  
  https://drive.google.com/drive/folders/1iZir_1W1-ihJBfuSHHFzrRhMFhA40-19?usp=drive_link
- Elasticsearch & Kibana:  
  https://github.com/ardhiraka/DEBlitz
- Great Expectations Tutorial:  
  https://colab.research.google.com/github/FTDS-learning-materials/phase-2/blob/master/w2/P2W2D1AM%20-%20Data%20Ethics%20%26%20Data%20Validation.ipynb
- Airflow Concepts: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html

---

