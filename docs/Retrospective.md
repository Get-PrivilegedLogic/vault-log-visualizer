# 📖 Project Retrospective: Vault Log Visualizer

## ✅ What Went Well

- Lambda/API Gateway setup went smoothly with environment variable configuration
- Generating realistic synthetic data helped validate visualizations
- Frontend drilldown with Chart.js was easy to implement and visually effective
- Using DynamoDB was fast, reliable, and cost-efficient within free tier
- Keeping ingestion and stats Lambda functions separate made code cleaner and testable

## ⚠️ Challenges Faced

- Initial CORS configuration blocked frontend API calls
- API Gateway needed extra manual setup for integrations and route responses
- Testing fetch behavior locally returned CORS errors due to `null` origin
- JSON data required careful formatting to avoid ingestion failures

## 🔁 Lessons Learned

- Always verify API integration and deployment before testing frontend
- Use synthetic datasets to simulate real-world IAM scenarios safely
- Chart.js interactivity is powerful and easy to extend
- Splitting repos between content and backend can introduce complexity — good to document folder structures

## 💡 Ideas for Future Enhancements

- Add login events over time (line chart)
- Filter logs by date or username
- Search functionality
- Basic auth using AWS Cognito
- Export dashboard as PDF or image
- Integrate with real anonymized logs (internal demo)

---

This project showcases a modern, secure approach to building a small-scale observability tool for IAM/security-related logs.
