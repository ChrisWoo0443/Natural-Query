# Natural-Query

┌────────────────────────────────────────────┐
│                Frontend (UI)               │
│  - File upload (CSV/Excel)                 │
│  - Natural language query input            │
│  - Output area: tables & charts            │
└────────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────┐
│           Backend Server (FastAPI)         │
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
┌────────────────────────────────────────────┐
│          Code Execution & Validation       │
│  - Runs Pandas code or SQL safely          │
│  - Sanitizes code to prevent bad input     │
│  - Executes query on uploaded data         │
└────────────────────────────────────────────┘
                  │
                  ▼
┌───────────────────────────────────────────────┐
│            Visualization Engine               │
│  - Displays table or chart (Plotly/Matplotlib)│
└───────────────────────────────────────────────┘
