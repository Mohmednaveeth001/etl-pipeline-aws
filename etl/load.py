import boto3
import logging
import pandas as pd
from sqlalchemy import create_engine, text
from config.aws_config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME
from config.db_config import RDS_HOST, RDS_PORT, RDS_USER, RDS_PASSWORD, RDS_DB

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Configure logging
logging.basicConfig(filename="logs/etl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Create MySQL database connection
engine = create_engine(f"mysql+pymysql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DB}")

def create_table():
    """Ensure the MySQL table exists before inserting data."""
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS transformed_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        height FLOAT,
        weight FLOAT
    );
    """
    try:
        with engine.connect() as conn:
            conn.execute(text(table_creation_query))
            logging.info("Checked/Created MySQL table: transformed_table.")
    except Exception as e:
        logging.error(f"Failed to create MySQL table: {e}")

def upload_to_s3(file_name, local_path):
    """Upload a file to S3."""
    try:
        s3_client.upload_file(local_path, S3_BUCKET_NAME, file_name)
        logging.info(f"Uploaded {file_name} to S3.")
    except Exception as e:
        logging.error(f"Failed to upload {file_name} to S3: {e}")

def load_to_rds(data):
    """Load data into the MySQL table in RDS."""
    create_table()  # Ensure table exists
    try:
        data.to_sql("transformed_table", engine, if_exists="append", index=False)
        logging.info("Data successfully loaded into MySQL RDS table: transformed_table.")
    except Exception as e:
        logging.error(f"Failed to load data into RDS: {e}")
