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