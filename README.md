# Natural Query

An AI-powered web app that allows users to upload datasets and ask questions in natural language. The app translates these questions into Pandas code or SQL queries, executes them, and displays the results as tables or visualizations.

## 🏗 System Architecture
```
┌────────────────────────────────────────────┐
│                Frontend (UI)               │
│  - File upload (CSV/Excel)                 │
│  - Natural language query input            │
│  - Output area: tables & charts            │
└────────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────┐
│          Backend Server (FastAPI)          │
│  - Receives query + dataset                │
│  - Validates and preprocesses data         │
│  - Calls AI Wrapper Service                │
└────────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────┐
│         AI Wrapper Service (Gemini)        │
│  - Sends natural language + data schema    │
│    to Gemini for code generation           │
│  - Receives Pandas code or SQL query       │
└────────────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────┐
│          Code Execution & Validation         │
│  - Runs Pandas code or SQL safely            │
│  - Sanitizes code to prevent malicious input │
│  - Executes query on uploaded data           │
└──────────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────────┐
│            Visualization Engine                │
│  - Displays table or chart (Plotly/Matplotlib) │
└────────────────────────────────────────────────┘
```

## 🔎 Key Features

- Upload CSV or Excel datasets.
- Ask questions in plain English.
- AI translates queries into executable code.
- Displays results as tables or charts.
- Secure code execution and validation.

## 🧠 Technologies

- **Frontend:** HTML-CSS
- **Backend:** FastAPI
- **AI:** Gemini
- **Data Handling:** Pandas / SQL
- **Visualization:** Plotly / Matplotlib

## Running
- **Frontend:**
```
cd frontend
python3 -m http.server 8001
```

- **Backend:**
```
cd backend
uvicorn main:app --reload
```

- **Run All Together:**
```
./run.sh
```