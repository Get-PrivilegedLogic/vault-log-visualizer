# Vault Log Visualizer

This project is a visual dashboard for analyzing synthetic Password Vault log data. It demonstrates a secure and scalable cloud-native solution using AWS services and a static frontend.

---

## 🚀 Features

- **AWS Lambda + API Gateway**: Serverless architecture for log ingestion and statistics aggregation
- **DynamoDB**: Stores structured synthetic log data
- **Chart.js Dashboard**: Visualizes platform usage and failed account trends
- **Drilldown Interactions**: Click bar chart elements to view failed accounts per platform
- **CORS-enabled Public API**: Enables browser-based frontend access

---

## 🧱 Architecture

```
[Client (HTML/CSS/JS)]
        |
        v
[API Gateway (2 Routes)]
   /logs  --> Lambda (Ingest → DynamoDB)
   /stats --> Lambda (Read & Aggregate → Return JSON)
        |
        v
[DynamoDB Table]
```

---

## 📁 Repo Structure

```
vault-log-visualizer/
├── lambda/
│   ├── log_ingest.py
│   ├── stats_aggregator.py
│   └── vault_logs_synthetic.json
├── frontend/
│   ├── stats.html
│   ├── stats.js
│   └── stats.css
├── .gitignore
└── README.md
```

---

## ✅ Deployment

1. Deploy Lambda functions via AWS Console or SAM
2. Set DynamoDB table name as environment variable (`DDB_TABLE_NAME`)
3. Attach IAM roles with `dynamodb:PutItem` and `dynamodb:Scan`
4. Enable CORS on API Gateway routes
5. Upload frontend files to S3 bucket with static hosting

---

## 📌 Project Goals

This project was built to:
- Demonstrate serverless design skills
- Create a portfolio-quality visual dashboard
- Work with synthetic IAM-related log data

---

## 🔐 Security & Privacy

- No personal or real credentials are used
- Synthetic data is randomly generated
- Access is read-only to the public
