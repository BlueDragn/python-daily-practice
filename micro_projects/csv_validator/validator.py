"""
CSV Validator

Checks:
- Required columns
- Missing values
"""

import csv
from pathlib import Path


REQUIRED_COLUMNS = {"name", "email", "age"}


def validate_csv(file_path: Path) -> None:
    with file_path.open(newline="") as file:
        reader = csv.DictReader(file)

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return

        for row_number, row in enumerate(reader, start=1):
            for column in REQUIRED_COLUMNS:
                if not row.get(column):
                    print(f"Row {row_number}: missing value in '{column}'")


def main():
    validate_csv(Path("sample.csv"))


if __name__ == "__main__":
    main()
