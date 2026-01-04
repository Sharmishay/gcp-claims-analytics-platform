import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "data/claims.csv"
NUM_ROWS = 1000000

def random_date():
    start = datetime.today() - timedelta(days=365)
    end = datetime.today()
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).date().isoformat()

def main():
    random.seed(42)

    headers = [
        "claim_id", "line_id", "member_id", "provider_id",
        "diagnosis_code", "procedure_code",
        "service_date", "allowed_amount", "paid_amount", "claim_status"
    ]

    statuses = ["PAID", "DENIED", "PENDED"]
    diag_codes = ["E11.9", "I10", "J45.909", "M54.5", "F32.9"]
    proc_codes = ["99213", "93000", "80053", "36415", "87086"]

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for i in range(1, NUM_ROWS + 1):
            allowed = round(random.uniform(50, 5000), 2)
            status = random.choice(statuses)

            paid = 0.0
            if status == "PAID":
                paid = round(allowed * random.uniform(0.5, 1.0), 2)
            elif status == "PENDED":
                paid = round(allowed * random.uniform(0.0, 0.2), 2)

            writer.writerow([
                f"C{i:07d}",
                random.randint(1, 3),
                f"M{random.randint(1, 1000):05d}",
                f"P{random.randint(1, 200):04d}",
                random.choice(diag_codes),
                random.choice(proc_codes),
                random_date(),
                allowed,
                paid,
                status
            ])

    print(f"✅ Generated {NUM_ROWS} rows in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
