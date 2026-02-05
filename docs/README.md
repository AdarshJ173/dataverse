# VelocityMart Operations Dashboard

🎯 **Interactive Dashboard for DATAVERSE Challenge**

This Streamlit dashboard provides comprehensive visualization and analysis of VelocityMart's warehouse operations, including:
- Real-time operational metrics
- Warehouse Health "Chaos Score"
- Aisle congestion heatmaps
- Temperature violation tracking
- Picker performance analysis
- Demand pattern insights

## 📁 File Structure

```
streamlit-dashboard/
├── dashboard.py              # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── sku_master.csv           # Product data (upload this)
├── order_transactions.csv   # Order history (upload this)
├── warehouse_constraints.csv # Warehouse layout (upload this)
└── picker_movement.csv      # GPS tracking data (upload this)
```

## 🚀 Quick Start

### Option 1: Run Locally

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Place CSV files** in the same directory as `dashboard.py`:
   - sku_master.csv
   - order_transactions.csv
   - warehouse_constraints.csv
   - picker_movement.csv

3. **Run the dashboard:**
```bash
streamlit run dashboard.py
```

4. **Open browser** at `http://localhost:8501`

### Option 2: Deploy to Streamlit Cloud (Recommended for Submission)

1. **Create GitHub repository:**
   - Create new repo on GitHub (e.g., `velocitymart-dashboard`)
   - Upload all files including CSVs

2. **Deploy to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repo
   - Select `dashboard.py` as main file
   - Click "Deploy"

3. **Get live URL:**
   - You'll get a URL like: `https://velocitymart-dashboard.streamlit.app`
   - Share this URL for competition submission

## 📊 Dashboard Features

### 1. 🏠 Overview
- Warehouse Health "Chaos Score" gauge
- Key operational metrics
- Hourly order distribution
- Zone utilization
- Top high-velocity SKUs

### 2. 🔥 Heatmap Analysis
- Aisle congestion heatmap (24-hour view)
- Aisle B bottleneck visualization
- Hour-by-hour traffic patterns
- Top 10 congested aisles

### 3. ❄️ Temperature Violations
- Total violations and critical issues
- Value at risk (₹245K)
- Violation breakdown by type
- Category distribution
- Temperature zone capacity analysis

### 4. 👤 Picker Performance
- Picker efficiency comparison
- PICKER-07 shortcut paradox analysis
- Distance vs speed metrics
- Complete picker statistics table

### 5. 📈 Demand Patterns
- 24-hour order patterns
- Day of week trends
- 90-week volume analysis
- Top 20 high-velocity SKUs
- Category distribution

## 🎥 Recording Demo Video

For competition submission, record a screen-share demo:

1. **Open dashboard** (local or deployed)
2. **Navigate through all 5 pages**
3. **Highlight key insights:**
   - Chaos Score (37.69 - High Risk)
   - Peak hour congestion at 19:00
   - 61.3% temperature violations
   - PICKER-07 shortcut anomaly
   - Aisle B bottleneck

4. **Show interactivity:**
   - Change hour filter on heatmap
   - Scroll through tables
   - Hover over charts

5. **Save as MP4** (use OBS Studio or similar)

## 📝 Competition Submission

Submit the following:

1. **Dashboard Link:**
   - Live URL from Streamlit Cloud
   - Example: `https://velocitymart-dashboard.streamlit.app`

2. **Demo Video:**
   - Screen recording (3-5 minutes)
   - Upload to Google Drive or YouTube
   - Include link in submission

3. **GitHub Repository:**
   - Link to your repo with all code
   - Example: `https://github.com/username/velocitymart-dashboard`

## ⚙️ Technical Details

**Built with:**
- Python 3.10+
- Streamlit 1.31.0
- Plotly 5.18.0 (interactive charts)
- Pandas 2.1.4 (data processing)

**Performance:**
- Data caching for fast load times
- Optimized queries for large datasets
- Responsive layout for all screen sizes

**Data Processing:**
- 436,052 order transactions
- 174,421 picker movements
- 800 SKUs across 18,000 slots
- 90 weeks of historical data

## 🐛 Troubleshooting

**Issue: "FileNotFoundError: No such file or directory: 'sku_master.csv'"**
- Ensure all 4 CSV files are in the same directory as `dashboard.py`

**Issue: Dashboard loads slowly**
- First load caches data (may take 10-15 seconds)
- Subsequent loads are instant

**Issue: Charts not displaying**
- Clear browser cache
- Try different browser (Chrome recommended)

**Issue: Deployment fails on Streamlit Cloud**
- Check CSV files are included in repo
- Verify requirements.txt has correct versions
- Check repo is public (not private)

## 📧 Support

For competition queries, refer to DATAVERSE Challenge manual or contact organizers.

---

**Created for:** DATAVERSE Challenge - VelocityMart Operations Analysis  
**Date:** February 5, 2026  
**Author:** Operations Analytics Team
