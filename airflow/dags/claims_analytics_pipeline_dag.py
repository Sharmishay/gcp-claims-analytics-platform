from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "data-engineer",
    "retries": 1,
}

with DAG(
    dag_id="claims_analytics_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="python scripts/generate_synthetic_claims.py",
    )

    dq_check = BashOperator(
        task_id="data_quality_check",
        bash_command="python scripts/dq_check_claims.py",
    )

    build_curated = BashOperator(
        task_id="build_curated",
        bash_command="python scripts/build_curated_claims.py",
    )

    provider_mart = BashOperator(
        task_id="build_provider_monthly_mart",
        bash_command="python scripts/build_provider_monthly_mart.py",
    )

    denial_mart = BashOperator(
        task_id="build_denial_rate_mart",
        bash_command="python scripts/build_denial_rate_mart.py",
    )

    high_cost_mart = BashOperator(
        task_id="build_high_cost_member_mart",
        bash_command="python scripts/build_high_cost_member_mart.py",
    )

    generate_data >> dq_check >> build_curated >> provider_mart >> denial_mart >> high_cost_mart
