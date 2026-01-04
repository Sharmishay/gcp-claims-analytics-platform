import csv
import matplotlib.pyplot as plt

# ---------- 1. Denial Rate Trend ----------
dates = []
rates = []

with open("data/mart_denial_rate_monthly.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row["year_month"])
        rates.append(float(row["denial_rate_percent"]))

plt.figure(figsize=(10, 5))
plt.plot(dates, rates, marker="o")
plt.xticks(rotation=45)
plt.title("Monthly Claim Denial Rate Trend")
plt.xlabel("Month")
plt.ylabel("Denial Rate (%)")
plt.tight_layout()
plt.savefig("visuals/denial_rate_trend.png")
plt.close()

# ---------- 2. Top Providers by Cost ----------
providers = []
costs = []

with open("data/mart_provider_monthly_cost.csv", "r") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        if i == 10:
            break
        providers.append(row["provider_id"])
        costs.append(float(row["total_allowed_amount"]))

plt.figure(figsize=(10, 5))
plt.bar(providers, costs)
plt.title("Top Providers by Allowed Amount")
plt.xlabel("Provider ID")
plt.ylabel("Total Allowed Amount")
plt.tight_layout()
plt.savefig("visuals/top_providers_cost.png")
plt.close()

print("✅ Visual analytics generated successfully.")
