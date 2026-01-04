import csv
from collections import defaultdict
from datetime import datetime

INPUT_FILE = "data/curated_claims.csv"
OUTPUT_FILE = "data/mart_denial_rate_monthly.csv"

def main():
    stats = defaultdict(lambda: {
        "total_claims": 0,
        "denied_claims": 0
    })

    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            service_date = datetime.fromisoformat(row["service_date"])
            year_month = service_date.strftime("%Y-%m")

            stats[year_month]["total_claims"] += 1
            if row["claim_status"] == "DENIED":
                stats[year_month]["denied_claims"] += 1

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "year_month",
            "total_claims",
            "denied_claims",
            "denial_rate_percent"
        ])

        for ym, vals in sorted(stats.items()):
            rate = (vals["denied_claims"] / vals["total_claims"]) * 100
            writer.writerow([
                ym,
                vals["total_claims"],
                vals["denied_claims"],
                round(rate, 2)
            ])

    print(f"Denial rate mart created: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
