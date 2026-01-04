import csv
from datetime import date

INPUT_FILE = "data/claims.csv"

def main():
    total_rows = 0
    errors = 0
    seen_keys = set()

    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1

            # Required fields
            for field in ["claim_id", "member_id", "provider_id", "service_date"]:
                if not row[field]:
                    errors += 1

            # Uniqueness check
            key = (row["claim_id"], row["line_id"])
            if key in seen_keys:
                errors += 1
            seen_keys.add(key)

            # Amount sanity
            if float(row["paid_amount"]) > float(row["allowed_amount"]):
                errors += 1

            # Date sanity
            if date.fromisoformat(row["service_date"]) > date.today():
                errors += 1

    print(f"Rows checked: {total_rows}")
    print(f"Total data quality errors: {errors}")

    if errors == 0:
        print("DATA QUALITY PASSED")
    else:
        print("DATA QUALITY FAILED")

if __name__ == "__main__":
    main()
