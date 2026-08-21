# Web Intelligence & Data Extraction Notebook

## Module 1: Network Protocols & HTTP Mechanics

### Key Learnings

#### 1. HTTP Request-Response Cycle

- Every website extraction starts with a **Client GET/POST Request** and a **Server Response**.
- **Status Codes:**
  - **200 OK:** Request succeeded and the server returned the expected data.
  - **301 Moved Permanently:**  Resource has been assigned a new permanent URL.
  - **302 Found:**  Temporary redirect to another URL.
  - **400 Bad Request:**  The request was malformed or invalid.
  - **401 Unauthorized:**  Authentication is required.
  - **403 Forbidden:**  Access is denied despite authentication.
  - **404 Not Found:**  The requested resource does not exist.
  - **500 Internal Server Error:**  The server encountered an unexpected condition.
  - **503 Service Unavailable:** The server is temporarily unable to handle the request.

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
```
---
### Module 1.3: DOM Parsing & CSS Selectors with BeautifulSoup

#### 1. What is the DOM?
- The **Document Object Model (DOM)** is the tree structure created by the browser after parsing raw HTML.
- In BeautifulSoup, we turn HTML text into a searchable DOM tree using `BeautifulSoup(html_text, "html.parser")`.

#### 2. CSS Selectors Reference
| Target Type | Syntax | Example | Description |
| :--- | :--- | :--- | :--- |
| **Tag Name** | `tag` | `h3` | Selects all `<h3>` elements |
| **Class** | `.class` | `.price_color` | Selects elements with `class="price_color"` |
| **ID** | `#id` | `#main_title` | Selects the unique element with `id="main_title"` |
| **Nested Child** | `parent child` | `h3 a` | Selects `<a>` tags inside `<h3>` tags |
| **Multiple Classes**| `.class1.class2` | `.instock.availability` | Selects elements containing *both* classes |

#### 3. Core BeautifulSoup Methods
- `soup.select("selector")`: Returns a **list** of all matching nodes (e.g., all product cards on a page).
- `node.select_one("selector")`: Returns the **first** matching node or `None`.
- `.text` / `.text.strip()`: Extracts the visible text inside an HTML tag.
- `node["attribute"]` or `node.attrs.get("attribute")`: Extracts tag attributes (e.g., `href` links or `title` text).

#### 4. Safe Defensive Extraction
- Web pages change or miss fields. Always use defensive checks (e.g., ternary operators or `if node:`) to avoid `AttributeError: 'NoneType' object has no attribute 'text'`.