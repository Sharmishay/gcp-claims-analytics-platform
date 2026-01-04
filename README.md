# gcp-claims-analytics-platform
End-to-end healthcare-style claims analytics platform using Python, Airflow, and BigQuery with data quality gates and CI/CD.

## Orchestration (Airflow)

This project includes an Apache Airflow DAG that orchestrates the full
claims analytics pipeline:

generate → data quality → curated → analytics marts

Due to known Apache Airflow SQLite limitations on Windows environments,
the DAG is provided as production-ready code and intended for execution
on Linux-based environments such as:
- Google Cloud Composer
- AWS MWAA
- Docker / Kubernetes

The DAG structure, dependencies, and task logic follow Airflow best practices.
