# Vault Log Visualizer

A dashboard-based project for visualizing **redacted CyberArk Password Vault logs** using synthetic data.

This project showcases:
- ✅ Synthetic CyberArk-style log ingestion
- ✅ Lambda + DynamoDB backend pipeline (optional)
- ✅ Visual dashboard hosted on S3
- ✅ Privacy-first log structure (no real credentials or sensitive data)

---

## 🔐 Features

- Interactive charts (check-outs, failures, usage by safe/user)
- Redacted log processing pipeline
- Serverless-friendly deployment (AWS Lambda + S3 + DDB)

---

## 📁 Sample Log Format

```json
{
  "event_time": "2025-05-28T14:22:17Z",
  "action": "CheckOut",
  "user": "user-a1f3",
  "safe": "Windows-Admins",
  "platform": "Windows",
  "success": true
}
```

---

## 🚧 Project Status

✅ Synthetic data generated  
🔜 Dashboard wireframe and Lambda pipeline in progress

---

## 📜 License

MIT
