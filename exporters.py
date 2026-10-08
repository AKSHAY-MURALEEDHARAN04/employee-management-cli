import csv
import json
import os
from logger import logger

EXPORT_DIR = "exports"

JSON_EXPORT_FILE = os.path.join(EXPORT_DIR,"employees.json")

CSV_EXPORT_FILE = os.path.join(EXPORT_DIR,"employees.csv")


def export_to_json(employees):

    try:
        if not employees:
            print("No employee data available to export.")
            logger.warning("JSON export attempted with no employee data.")
            return False

        os.makedirs(EXPORT_DIR,exist_ok=True)

        with open(JSON_EXPORT_FILE,"w",encoding="utf-8") as file:

            json.dump(employees,file,indent=4)

        print(f"Employee data exported to {JSON_EXPORT_FILE}")
        logger.info("Employee data exported successfully to JSON.")
        return True

    except OSError as e:
        print("Error: Unable to export employee data to JSON.")
        logger.error(f"JSON export failed: {e}")
        return False


def export_to_csv(employees):
    try:
        if not employees:
            print("No employee data available to export.")
            logger.warning("CSV export attempted with no employee data.")
            return False

        os.makedirs(EXPORT_DIR,exist_ok=True)
        fieldnames = [
            "id",
            "name",
            "age",
            "department",
            "role",
            "salary",
            "email"
        ]

        with open(CSV_EXPORT_FILE,"w",newline="",encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)
        print(f"Employee data exported to {CSV_EXPORT_FILE}")
        logger.info("Employee data exported successfully to CSV.")
        return True

    except OSError as e:
        print("Error: Unable to export employee data to CSV.")
        logger.error(f"CSV export failed: {e}")
        return False