import os
import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import upload_to_s3, load_to_rds

# Configure logging
logging.basicConfig(filename="logs/etl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DATA_FOLDER = "data/unzipped/"
OUTPUT_FILE = "data/transformed/transformed_data.csv"

if __name__ == "__main__":
    logging.info("ETL Pipeline Started")

    # Extract
    raw_data = extract_data(DATA_FOLDER)

    # Transform
    transformed_data = transform_data(raw_data)

    # Save locally
    transformed_data.to_csv(OUTPUT_FILE, index=False)

    # Load to S3
    upload_to_s3("transformed_data.csv", OUTPUT_FILE)

    # Load to RDS
    load_to_rds(transformed_data)

    logging.info("ETL Pipeline Completed")


