import boto3
from datetime import date, timedelta

def get_spend():
    """Return month-to-date spend in USD from AWS Cost Explorer."""
    
    client = boto3.client("ce")

    today = date.today()
    start_of_month = today.replace(day=1).isoformat()

    # Cost Explorer excludes the end date
    end = (today + timedelta(days=1)).isoformat()

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_of_month,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
    )

    amount = float(
        response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    )

    return amount


if __name__ == "__main__":
    usd = get_spend()
    ngn = usd * 1500

    print(f"💰 Month-to-date AWS spend: ${usd:.2f} (~₦{ngn:,.0f})")

    if usd > 10:
        print("⚠️ Over $10. Check what's running.")
    else:
        print("✅ Within budget.")
