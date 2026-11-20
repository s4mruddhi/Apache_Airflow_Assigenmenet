from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="assignment4_workflow",
    start_date=datetime(2026, 8, 21),
    schedule=None,
    catchup=False,
    tags=["MLOps", "Assignment4"],
)
def assignment4_workflow():

    @task
    def extract_data():
        print("Step 1: Extracting data...")
        data = [10, 20, 30, 40, 50]
        print(f"Extracted data: {data}")
        return data

    @task
    def process_data(data):
        print("Step 2: Processing data...")
        processed = [x * 2 for x in data]
        print(f"Processed data: {processed}")
        return processed

    @task
    def save_result(processed):
        print("Step 3: Saving result...")
        total = sum(processed)

        with open("/opt/airflow/output/result.txt", "w") as file:
            file.write(f"Processed data: {processed}\n")
            file.write(f"Total: {total}\n")

        print(f"Result saved successfully. Total = {total}")

    data = extract_data()
    processed = process_data(data)
    save_result(processed)


assignment4_workflow()