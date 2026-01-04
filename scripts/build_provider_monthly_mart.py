import csv
from collections import defaultdict
from datetime import datetime

INPUT_FILE = "data/curated_claims.csv"
OUTPUT_FILE = "data/mart_provider_monthly_cost.csv"

def main():
    metrics = defaultdict(lambda: {
        "total_allowed": 0.0,
        "total_paid": 0.0,
        "claim_count": 0
    })

    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            provider = row["provider_id"]
            service_date = datetime.fromisoformat(row["service_date"])
            year_month = service_date.strftime("%Y-%m")

            key = (provider, year_month)

            metrics[key]["total_allowed"] += float(row["allowed_amount"])
            metrics[key]["total_paid"] += float(row["paid_amount"])
            metrics[key]["claim_count"] += 1

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "provider_id",
            "year_month",
            "total_allowed_amount",
            "total_paid_amount",
            "claim_count"
        ])

        for (provider, year_month), vals in metrics.items():
            writer.writerow([
                provider,
                year_month,
                round(vals["total_allowed"], 2),
                round(vals["total_paid"], 2),
                vals["claim_count"]
            ])

    print(f"✅ Provider monthly mart created: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
