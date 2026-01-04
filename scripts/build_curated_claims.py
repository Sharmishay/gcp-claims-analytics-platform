import csv

INPUT_FILE = "data/claims.csv"
OUTPUT_FILE = "data/curated_claims.csv"

def main():
    with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        rows_written = 0

        for row in reader:
            # Example normalization
            row["claim_status"] = row["claim_status"].upper()

            # Business rule: exclude zero-allowed claims
            if float(row["allowed_amount"]) <= 0:
                continue

            writer.writerow(row)
            rows_written += 1

    print(f"Curated dataset created with {rows_written} rows")

if __name__ == "__main__":
    main()
