import boto3
import pandas as pd
import json
import logging
import os
import xml.etree.ElementTree as ET
from config.aws_config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME

# Configure logging
logging.basicConfig(filename="logs/etl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def download_from_s3(file_name, local_path):
    """Download a file from S3 bucket."""
    try:
        s3_client.download_file(S3_BUCKET_NAME, file_name, local_path)
        logging.info(f"Downloaded {file_name} from S3.")
    except Exception as e:
        logging.error(f"Failed to download {file_name} from S3: {e}")

def extract_csv(file_path):
    return pd.read_csv(file_path)

def extract_json(file_path):
    with open(file_path, "r") as json_file:
        return pd.DataFrame([json.loads(line) for line in json_file])

def extract_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    xml_data = [{"name": p.find("name").text, "height": float(p.find("height").text), "weight": float(p.find("weight").text)} for p in root.findall("person")]
    return pd.DataFrame(xml_data)

def extract_data(folder_path):
    logging.info("Starting data extraction...")
    combined_data = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if file_name.endswith(".csv"):
                combined_data.append(extract_csv(file_path))
            elif file_name.endswith(".json"):
                combined_data.append(extract_json(file_path))
            elif file_name.endswith(".xml"):
                combined_data.append(extract_xml(file_path))
            logging.info(f"Extracted data from {file_name}.")
        except Exception as e:
            logging.error(f"Failed to extract data from {file_name}: {e}")

    logging.info("Data extraction completed.")
    return pd.concat(combined_data, ignore_index=True)
