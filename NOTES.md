# Web Intelligence & Data Extraction Notebook

## Module 1: Network Protocols & HTTP Mechanics

### Key Learnings

#### 1. HTTP Request-Response Cycle
- Every web extraction starts with a **Client GET/POST Request** and a **Server Response**.
- **Status Codes:**
  - `200 OK`: Successful fetch. Ready to parse.
  - `403 Forbidden`: Bot blocked (missing/invalid headers).
  - `429 Too Many Requests`: Rate limited (sending requests too fast).
  - `503 Service Unavailable`: Server busy or anti-bot shield active.

#### 2. Header Spoofing & Identity
- Default `requests` send `User-Agent: python-requests/...`, which marketing servers easily flag and block.
- **Solution:** Override headers using a realistic desktop browser signature (`Mozilla/5.0...`).

#### 3. Environment & Security Best Practices
- **Virtual Environments (`venv`):** Isolate project packages from global Python to avoid dependency conflicts.
- **`.gitignore`:** Crucial for keeping heavy binaries (`venv/`), temporary caches (`__pycache__/`), and private environment secrets out of version control.
- **Windows PowerShell Execution Policy:** Resolved using `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

---

## Useful Command Cheatsheet

### Git Workflow
```bash
git add .
git commit -m "your commit message"
git push origin main