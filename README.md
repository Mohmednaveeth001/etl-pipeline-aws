ETL Pipeline with AWS (S3 & MySQL RDS)
📌 Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline using Python, AWS S3, and MySQL RDS. The pipeline extracts data from CSV, JSON, and XML files, transforms it, and loads it into an AWS RDS MySQL database.

🛠️ Technologies Used
Python (Pandas, SQLAlchemy, Boto3, dotenv)
AWS S3 (Storage for raw and transformed data)
AWS RDS (MySQL) (Stores transformed data)
SQLAlchemy (Database interaction)
Logging (Tracks ETL execution)
📁 Project Directory Structure
graphql

ETL_Project/
│── config/
│   ├── .env                 # Stores AWS & DB credentials
│   ├── aws_config.py        # Load AWS credentials
│   ├── db_config.py         # Load RDS credentials
│── data/
│   ├── unzipped/            # Raw data extracted from source.zip
│   ├── transformed/         # Processed CSV, JSON, XML files
│── etl/
│   ├── extract.py           # Extract raw data from S3 or local
│   ├── transform.py         # Transform data (cleaning, unit conversions)
│   ├── load.py              # Load data to S3 and RDS
│── logs/
│   ├── etl.log              # Stores ETL execution logs
│── main.py                  # ETL pipeline execution script
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
🚀 Features
✅ Extracts data from CSV, JSON, and XML files
✅ Downloads/uploads data from AWS S3
✅ Transforms data (unit conversion, cleaning)
✅ Loads data into AWS MySQL RDS
✅ Uses environment variables for secure credentials
✅ Implements logging for tracking ETL execution

🔧 Installation & Setup
1️⃣ Clone the Repository


git clone https://github.com/your-username/etl-pipeline-aws.git
cd etl-pipeline-aws
2️⃣ Create & Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.v.venv\Scripts\activate    # On Windows
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Configure AWS & MySQL Credentials
Create a .env file inside the config/ folder:

# AWS Credentials
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_REGION=your-aws-region
S3_BUCKET_NAME=your-s3-bucket-name

# MySQL RDS Credentials
RDS_HOST=your-rds-endpoint
RDS_PORT=3306
RDS_USER=your-db-username
RDS_PASSWORD=your-db-password
RDS_DB=your-database-name
5️⃣ Run the ETL Pipeline

python main.py
📊 Database Schema (MySQL RDS)

CREATE TABLE IF NOT EXISTS transformed_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    height FLOAT,
    weight FLOAT
);
⚡ AWS Setup Guide
🔹 Create an S3 Bucket
Open AWS Console → S3
Click Create Bucket → Name it (your-s3-bucket-name)
Enable public access settings if needed
🔹 Set Up MySQL RDS
Open AWS Console → RDS
Click Create Database → Select MySQL
Choose instance type (e.g., db.t2.micro)
Set username & password → Save the endpoint URL
📜 Logging
The ETL process logs events in logs/etl.log:

log
Copy
Edit
2025-02-27 10:00:00 - INFO - ETL Pipeline Started
2025-02-27 10:00:05 - INFO - Extracted data from file1.csv
2025-02-27 10:00:10 - INFO - Transformed data successfully
2025-02-27 10:00:15 - INFO - Loaded data into MySQL RDS
📌 To-Do List
 Extract data from different file formats
 Upload/download data from AWS S3
 Transform and clean data
 Load transformed data into AWS MySQL RDS
 Automate with AWS Glue (Optional)
 Schedule jobs with AWS Lambda (Optional)
