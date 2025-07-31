# Analisis dan Evaluasi Performa Pemain NBA untuk Mendukung Proses Scouting dan Trade pada Tim San Antonio Spurs

![San Antonio Spurs Logo](images/Banner.jpeg)

## 🗂 Struktur Repository

- `config/`  
  &nbsp;&nbsp;&nbsp;&nbsp;Konfigurasi Airflow dan pengaturan terkait.
- `dags/`  
  &nbsp;&nbsp;&nbsp;&nbsp;Script DAG Airflow untuk workflow proses data:  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBAPlayer_Preference_DAG.py`  
- `Data_Clean/`  
  &nbsp;&nbsp;&nbsp;&nbsp;Dataset yang sudah dibersihkan:  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBA_Player_Data_Clean.csv`
- `Dataset_Asli/`  
  &nbsp;&nbsp;&nbsp;&nbsp;Dataset mentah asli dari sumber:  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBA_Player_Stats.csv`, `NBA_Player_Stats_2.csv`
- `gx/`  
  &nbsp;&nbsp;&nbsp;&nbsp;Proyek Great Expectations untuk validasi data:  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBAPlayer_Preference_GX(BAHASA).ipynb`, `NBAPlayer_Preference_GX(ENGLISH).ipynb`
- `images/`  
  &nbsp;&nbsp;&nbsp;&nbsp;Screenshot visualisasi Kibana dan logo Spurs  
- Berkas lain:  
  &nbsp;&nbsp;&nbsp;&nbsp;`docker-compose.yaml`, `Dockerfile.airflow`, `README.md`,  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBAPlayer_Preference_Data_Raw.csv`,  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBAPlayer_Preference_DDL.txt`,  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBAPlayer_Preference_Presentation.pptx`,  
  &nbsp;&nbsp;&nbsp;&nbsp;`NBAPlayer_Preference_DAG_Graph.png`  

---

## Latar Belakang Masalah

Manajemen San Antonio Spurs berencana untuk melakukan perombakan susunan pemain untuk musim 2023 dengan tujuan meningkatkan performa tim secara keseluruhan. Oleh karena itu, dibutuhkan evaluasi objektif terhadap data performa pemain NBA untuk membantu proses scouting dan trade.

---

## Tujuan

Memberikan wawasan berbasis data mengenai performa pemain NBA selama beberapa tahun terakhir yang dapat digunakan oleh:
- Manajemen Tim
- Tim Scouting
- Pelatih

Untuk mendukung:
- Proses scouting pemain
- Proses trade pemain
- Strategi formasi dan pergantian pemain

---

## Data

Dataset: Statistik pemain NBA musim 2018–2022, meliputi data seperti menit bermain, tembakan, rebound, assist, turnover, dan poin dari berbagai posisi pemain.

Data telah melalui proses pembersihan untuk menghilangkan duplikat, nilai hilang, dan normalisasi format kolom.

---

## Metodologi

1. **ETL Pipeline**  
   Memindahkan data dari CSV ke PostgreSQL, melakukan transformasi dan pembersihan, lalu memasukkannya ke Elasticsearch.

2. **Workflow Orkestrasi**  
   Menggunakan Apache Airflow DAG dengan 3 tugas utama: `fetch_from_postgres`, `clean_data`, `post_to_elasticsearch`.

3. **Validasi Data**  
   Menggunakan Great Expectations dengan beberapa tipe ekspektasi untuk memastikan kualitas data.

4. **Visualisasi**  
   Membuat dashboard Kibana untuk analisis visual, menampilkan insight: 10 besar pemain per posisi, pemain dengan turnover terbanyak, statistik poin per game, dan lain-lain.

---

## Teknologi yang Digunakan

- Python  
- Apache Airflow  
- PostgreSQL  
- Elasticsearch & Kibana  
- Docker  

---

## Output Proyek

- Data bersih dalam CSV  
- DAG Airflow terjadwal  
- Data berhasil dimasukkan ke Elasticsearch  
- Dashboard visualisasi di Kibana  
- Presentasi hasil analisis dalam format PowerPoint

---

## Referensi

- Panduan markdown GitHub: https://docs.github.com/en/get-started/writing-on-github  
- Materi Airflow DAG: https://drive.google.com/drive/folders/1iZir_1W1-ihJBfuSHHFzrRhMFhA40-19?usp=drive_link  
- Elasticsearch & Kibana: https://github.com/ardhiraka/DEBlitz  
- Great Expectations tutorial: https://colab.research.google.com/github/FTDS-learning-materials/phase-2/blob/master/w2/P2W2D1AM%20-%20Data%20Ethics%20%26%20Data%20Validation.ipynb  

---

# Analysis and Performance Evaluation of NBA Players to Support Scouting and Trading for the San Antonio Spurs Team

![San Antonio Spurs Logo](images/Banner.jpeg)

## 🗂 Repository Structure

- `config/`  
  Airflow configurations and settings.
- `dags/`  
  Airflow DAG scripts for data processing workflow:  
  `NBAPlayer_Preference_DAG.py`
- `Data_Clean/`  
  Cleaned datasets:  
  `NBA_Player_Data_Clean.csv`
- `Dataset_Asli/`  
  Original raw datasets:  
  `NBA_Player_Stats.csv`, `NBA_Player_Stats_2.csv`
- `gx/`  
  Great Expectations project for data validation:  
  `NBAPlayer_Preference_GX(BAHASA).ipynb`, `NBAPlayer_Preference_GX(ENGLISH).ipynb`
- `images/`  
  Kibana visualization screenshots and Spurs logo  
- Other Files:  
  `docker-compose.yaml`, `Dockerfile.airflow`, `README.md`,  
  `NBAPlayer_Preference_data_raw.csv`,  
  `NBAPlayer_Preference_DDL.txt`,  
  `NBAPlayer_Preference_Presentation.pptx`,  
  `NBAPlayer_Preference_DAG_Graph.png`

---

## Background

The San Antonio Spurs management plans to rebuild the roster for the 2023 season aiming to improve the overall team performance. Therefore, an objective evaluation of NBA player performance data is required to assist scouting and trading decisions.

---

## Objectives

Provide data-driven insights on NBA player performance over recent years to be used by:
- Team Management
- Scouting Team
- Coaching Staff

For:
- Scouting players
- Trading players
- Formations and rotation strategies

---

## Data

Dataset contains NBA player stats from 2018 to 2022, including minutes played, shots, rebounds, assists, turnovers, and points, categorized by player position.

Data undergoes cleaning to remove duplicates, missing values, and normalize column formats.

---

## Methodology

1. **ETL Pipeline**  
   Move data from CSV to PostgreSQL, perform transformations and cleaning, then load into Elasticsearch.

2. **Workflow Orchestration**  
   Use Apache Airflow DAG with 3 main tasks: `fetch_from_postgres`, `clean_data`, `post_to_elasticsearch`.

3. **Data Validation**  
   Use Great Expectations with various expectation types to ensure data quality.

4. **Visualization**  
   Create Kibana dashboards for visual analysis highlighting top players per position, turnovers, points per game trends, etc.

---

## Tech Stack

- Python  
- Apache Airflow  
- PostgreSQL  
- Elasticsearch & Kibana  
- Docker  

---

## Project Outputs

- Clean CSV data  
- Scheduled Airflow DAG file  
- Data ingested successfully into Elasticsearch  
- Kibana dashboards visualization  
- PowerPoint presentation summarizing insights

---

## References

- GitHub markdown guide: https://docs.github.com/en/get-started/writing-on-github  
- Airflow DAG tutorial: https://drive.google.com/drive/folders/1iZir_1W1-ihJBfuSHHFzrRhMFhA40-19?usp=drive_link  
- Elasticsearch & Kibana repo: https://github.com/ardhiraka/DEBlitz  
- Great Expectations tutorial: https://colab.research.google.com/github/FTDS-learning-materials/phase-2/blob/master/w2/P2W2D1AM%20-%20Data%20Ethics%20%26%20Data%20Validation.ipynb  
