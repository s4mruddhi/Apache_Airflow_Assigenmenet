# Apache Airflow Workflow Assignment (MLOps)

This repository contains the implementation of an Apache Airflow workflow pipeline (Assignment 4) developed for Machine Learning and Operations (MLOps).

---

## 📌 Project Overview

The pipeline orchestrates an ETL (Extract, Transform, Load) workflow using Apache Airflow and TaskFlow API (`@dag` and `@task` decorators).

### Pipeline Workflow:
1. **`extract_data`**: Simulates reading/extracting input data.
2. **`process_data`**: Transforms extracted values (doubles each element).
3. **`save_result`**: Aggregates processed values (computes total sum) and persists the result to `/opt/airflow/output/result.txt`.

---

## 📁 Repository Structure

```text
├── dags/
│   └── assignment4_workflow.py    # Apache Airflow DAG definition
├── data/
│   └── input_data.csv             # Sample input dataset
├── output/
│   └── result.txt                 # Pipeline output and execution results
├── config/
│   └── airflow.cfg                # Airflow configuration file
├── Screenshots/                   # Execution screenshots & verification
│   ├── 01_Airflow_Dashboard.png
│   ├── assignment4_workflow-graph.png
│   ├── Dags.png
│   ├── extract_data.png
│   ├── process_data.png
│   ├── save_resultpng.png
│   ├── report.png
│   ├── report_file.png
│   ├── Successful Workflow Execution.png
│   └── sucessful dag run.png
├── docker-compose.yaml            # Docker Compose configuration for Airflow
└── .gitignore
```

---

## 🚀 Running the Workflow with Docker Compose

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with WSL 2 backend on Windows)
- Docker Compose v2+

### 1. Initialize Airflow Environment
```bash
docker compose up airflow-init
```

### 2. Start Airflow Services
```bash
docker compose up -d
```

### 3. Access Airflow UI
Once services are running, open your browser:
- **URL**: [http://localhost:8085](http://localhost:8085) (Port 8085 is used to avoid port 8080 conflict with Jenkins)
- **Username**: `airflow`
- **Password**: `airflow`

### 4. Trigger the DAG
1. In the Airflow Web UI, locate `assignment4_workflow`.
2. Unpause the DAG (toggle to Active).
3. Click the **Trigger DAG** button (play icon).
4. Monitor the Graph and Grid views for successful task execution (`extract_data` ➔ `process_data` ➔ `save_result`).

### 5. Check Output
Inspect the generated output file at `output/result.txt`:
```text
Processed data: [20, 40, 60, 80, 100]
Total: 300
```

---

## 📸 Execution Verification
Screenshots validating successful deployment, DAG run, task logs, and output generation are documented in the [`Screenshots/`](Screenshots/) directory.
