# AWS Cost Summariser (boto3)

This project is a simple AWS cost monitoring tool built using Python and boto3. It retrieves the month-to-date AWS spending using the AWS Cost Explorer API and displays it in USD and an estimated NGN value.

## Features

- Retrieves month-to-date AWS cost using AWS Cost Explorer API
- Uses boto3 with IAM authentication
- Converts USD cost to NGN (approximate rate)
- Provides a basic budget warning if cost exceeds a threshold
- Lightweight and easy to run in any Linux environment

## Project Structure

```
aws-cost/
│
├── cost_check.py       # Main Python script
├── requirements.txt    # Project dependencies
├── .gitignore          # Ignored files
└── README.md           # Project documentation
```

## Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/YOUR-USERNAME/aws-cost.git
cd aws-cost
```

### 2. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure AWS credentials
```bash
aws configure
```

Provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. us-east-1)
- Output format (json)

### 5. Run the script
```bash
python3 cost_check.py
```

## Sample Output

```
💰 Month-to-date AWS spend: $0.00 (~₦0)
✅ Within budget.
```

If cost exceeds threshold:

```
⚠️ Over $10. Check what's running: aws ec2 describe-instances
```

## Security Notes

- Do not commit AWS credentials or `.env` files
- Ensure `.gitignore` is properly configured

## Future Improvements

- Daily cost tracking dashboard
- Email/Telegram cost alerts
- Service-level cost breakdown (EC2, S3, RDS)
- Automated scheduling with cron jobs or GitHub Actions

## Author

Oluwapelumi Odetayo
