import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# ---------- 1. Denial Rate Trend with Rolling Average ----------
denials = pd.read_csv("data/mart_denial_rate_monthly.csv")
denials["rolling_avg"] = denials["denial_rate_percent"].rolling(3).mean()

plt.figure(figsize=(10,5))
plt.plot(denials["year_month"], denials["denial_rate_percent"], label="Monthly")
plt.plot(denials["year_month"], denials["rolling_avg"], label="3-Month Avg", linewidth=3)
plt.xticks(rotation=45)
plt.title("Denial Rate Trend with Rolling Average")
plt.legend()
plt.tight_layout()
plt.savefig("visuals/denial_rate_trend_rolling_avg.png")
plt.close()

# ---------- 2. Provider Cost Pareto ----------
providers = pd.read_csv("data/mart_provider_monthly_cost.csv")
provider_totals = providers.groupby("provider_id")["total_allowed_amount"].sum().sort_values(ascending=False)
cum_pct = provider_totals.cumsum() / provider_totals.sum() * 100

plt.figure(figsize=(10,5))
plt.plot(cum_pct.values)
plt.axhline(80, color="red", linestyle="--")
plt.title("Provider Cost Concentration (Pareto Analysis)")
plt.ylabel("Cumulative % of Cost")
plt.xlabel("Providers Ranked by Cost")
plt.tight_layout()
plt.savefig("visuals/provider_cost_pareto.png")
plt.close()

# ---------- 3. High-Cost Member Curve ----------
members = pd.read_csv("data/mart_high_cost_members.csv")
members_sorted = members.sort_values("total_allowed_amount", ascending=False)

plt.figure(figsize=(10,5))
plt.plot(members_sorted["total_allowed_amount"].values)
plt.title("High-Cost Member Distribution")
plt.xlabel("Members Ranked by Cost")
plt.ylabel("Total Allowed Amount")
plt.tight_layout()
plt.savefig("visuals/high_cost_member_curve.png")
plt.close()

print("✅ Advanced visual analytics generated successfully.")