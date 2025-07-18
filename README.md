# 📊 Google Sheets Auto-Updater

This project automatically extracts key insights from a large CSV dataset using Python and updates a Google Sheet with a clean, summarized dashboard for stakeholders.

---

## ✨ Features

* ✅ Reads large CSV files
* ✅ Extracts and pivots key columns (in this case, e.g. `State`, `Profit`, `R&D Spend`)
* ✅ Automatically updates a specific Google Sheet
* ✅ Can be scheduled daily using Windows Task Scheduler or Unix cron
* ✅ Zero-cost setup using Google API free tier

---

## 📁 Project Structure

```
gsheetsauto/
│
├── main.py                     # Main script to process and upload data
├── 50_Startups.csv             # Example dataset (or your actual data source)
├── analog-signal-xxxxx.json    # Google Service Account credentials
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo and set up a virtual environment

```bash
git clone https://github.com/yourname/gsheetsauto.git
cd gsheetsauto
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate for Mac/Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Enable Google Sheets API and Drive API

* Visit: [Google Cloud Console](https://console.cloud.google.com/)
* Create a project → Enable **Google Sheets API** and **Google Drive API**
* Create a **Service Account** → Download the JSON key

### 4. Share your Google Sheet

* Create a Google Sheet titled **"Stakeholder Dashboard"**
* Share it with the email in your service account JSON
  (e.g. `gsheets-bot@your-project.iam.gserviceaccount.com`) with **Editor** access

### 5. Run the script

```bash
python main.py
```


---

## 📌 Example Output

A pivot summary like this will be written to your Google Sheet:

| State      | Profit | R\&D Spend |
| ---------- | ------ | ---------- |
| California | 250000 | 120000     |
| Florida    | 190000 | 80000      |
| New York   | 210000 | 100000     |

---

## 📦 Dependencies

Listed in `requirements.txt`:

```txt
pandas
gspread
gspread_dataframe
oauth2client
```

---

## 🛠 Customize

You can:

* Change pivot groupings (e.g., by `Category`, `Region`)
* Use other aggregations like `mean`, `count`, etc.
* Upload multiple sheets or tabs using `worksheet = sheet.worksheet('TabName')`

---

## 📄 License

MIT License – feel free to use, fork, and adapt!
