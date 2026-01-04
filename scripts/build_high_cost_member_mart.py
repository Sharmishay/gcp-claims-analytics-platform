import csv
from collections import defaultdict

INPUT_FILE = "data/curated_claims.csv"
OUTPUT_FILE = "data/mart_high_cost_members.csv"

def main():
    member_costs = defaultdict(float)
    member_claims = defaultdict(int)

    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            member = row["member_id"]
            member_costs[member] += float(row["allowed_amount"])
            member_claims[member] += 1

    # Sort members by total cost descending
    top_members = sorted(
        member_costs.items(),
        key=lambda x: x[1],
        reverse=True
    )[:100]

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "member_id",
            "total_allowed_amount",
            "claim_count"
        ])

        for member, total_cost in top_members:
            writer.writerow([
                member,
                round(total_cost, 2),
                member_claims[member]
            ])

    print(f"High-cost member mart created: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
