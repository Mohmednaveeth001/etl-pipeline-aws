import logging

def transform_data(data):
    logging.info("Starting data transformation...")
    data["height"] = data["height"] * 2.54  # Inches to cm
    data["weight"] = data["weight"] * 0.453592  # Pounds to kg
    data = data.drop_duplicates()
    logging.info("Data transformation completed.")
    return data
