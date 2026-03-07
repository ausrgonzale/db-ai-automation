# DB AI Automation 🤖🗄️

An AI-powered automated testing framework for a fake e-commerce API using FastAPI, MySQL, Playwright, and pytest — with AI-generated test data via the Anthropic Claude API.

![CI](https://github.com/ausrgonzale/db-ai-automation/actions/workflows/ci.yml/badge.svg)

---

## 🧰 Prerequisites

- Intel MacBook running macOS
- Python 3.10+ (this project uses 3.12.12)
- Terminal access

---

## ⚙️ Initial Mac Setup

### 1. Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Enter your Mac login password when prompted (you won't see it typing — that's normal).

### 2. Install MySQL
```bash
brew install mysql
```

### 3. Start MySQL and set it to auto-start on reboot
```bash
brew services start mysql
```

### 4. Secure MySQL and set a password
```bash
mysql_secure_installation
```
When prompted:
- **VALIDATE PASSWORD component?** → `N`
- **New password** → `root`
- **Remove anonymous users?** → `Y`
- **Disallow root login remotely?** → `Y`
- **Remove test database?** → `Y`
- **Reload privilege tables?** → `Y`

### 5. Verify MySQL is running
```bash
mysql -u root -p
```
Type `root` as the password. If you see a `mysql>` prompt you are in.
Type `exit` to leave.

### 6. Create the project database
```bash
mysql -u root -p -e "CREATE DATABASE db_ai_automation;"
```
Type `root` when prompted. No output = success.

---

## 📁 Project Setup

### 1. Navigate to your projects folder
```bash
cd /Users/rongonzalez/Programming/Code
```

### 2. Create the project folder and virtual environment
```bash
mkdir db-ai-automation
cd db-ai-automation
python3 -m venv venv
source venv/bin/activate
```
You will know it worked when your terminal prompt shows `(venv)` at the start.

> 💡 Every time you return to work on this project run:
> `cd /Users/rongonzalez/Programming/Code/db-ai-automation && source venv/bin/activate`

### 3. Install all packages
```bash
pip install -r requirements.txt
playwright install
```

---

## 📂 Project Structure
```
db-ai-automation/
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI pipeline
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app and routes
│   ├── models.py             # SQLAlchemy DB models
│   ├── database.py           # MySQL connection setup
│   └── schemas.py            # Pydantic request/response shapes
├── data_gen/
│   ├── __init__.py
│   └── ai_generator.py       # AI + Faker data generation
├── tests/
│   ├── conftest.py           # Shared pytest fixtures (DB seed/teardown)
│   ├── api/
│   │   ├── test_users.py
│   │   ├── test_products.py
│   │   ├── test_orders.py
│   │   ├── test_db_integrity.py
│   │   ├── test_edge_cases.py
│   │   └── test_e2e_shopping.py
│   └── ui/
│       ├── conftest.py       # Playwright browser fixture
│       ├── test_storefront.py
│       └── test_e2e_shopping.py
├── reports/                  # Auto-generated HTML test reports
├── .env                      # API keys and DB credentials (never commit!)
├── .env.example              # Example environment variables (safe to commit)
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🔑 Configure Environment Variables

Copy the example file and fill in your credentials:
```bash
cp .env.example .env
```

Edit `.env`:
```
# MySQL
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=root
DB_NAME=db_ai_automation

# Anthropic
ANTHROPIC_API_KEY=your_api_key_here
```
Get your Anthropic API key at: https://console.anthropic.com under API Keys.

> ⚠️ Never commit your `.env` file. It is listed in `.gitignore` and will never be tracked by Git.

---

## 🟢 Health Check

| Tool        | Command               | Expected Output         |
|-------------|-----------------------|-------------------------|
| Homebrew    | `brew --version`      | `Homebrew 4.x.x`        |
| MySQL       | `mysql --version`     | `mysql  Ver 8.x.x`      |
| Python      | `python3 --version`   | `Python 3.12.12`        |
| Virtual env | check terminal prompt | starts with `(venv)`    |
| pip         | `which pip`           | path contains `/venv/`  |

---

## ▶️ Running the Project Locally

### Start the API server (Terminal window 1)
```bash
uvicorn app.main:app --reload
```

### Run all tests (Terminal window 2)
```bash
pytest
```

### Run only API tests
```bash
pytest tests/api/ -v
```

### Run only UI tests
```bash
pytest tests/ui/ -v
```

### View the HTML test report
```bash
open reports/test_report.html
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Every push to `main` automatically triggers the CI pipeline which:

1. Spins up a MySQL 8.0 Docker service container
2. Installs Python dependencies
3. Installs Playwright Chromium browser
4. Creates a `.env` file using GitHub Secrets
5. Starts the FastAPI server
6. Runs the full test suite
7. Uploads the HTML test report as a downloadable artifact

### Setting up GitHub Secrets

Before the pipeline can run you need to add your Anthropic API key as a GitHub secret:

1. Go to your repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `ANTHROPIC_API_KEY`
4. Value: your Anthropic API key
5. Click **Add secret**

### Viewing pipeline results

Go to your repo on GitHub and click the **Actions** tab to see all pipeline runs, logs, and downloadable test reports.

---

## 🗺️ Roadmap

- [x] Project scaffolding
- [x] MySQL + SQLAlchemy setup
- [x] AI data generation with Anthropic API
- [x] API tests with pytest + httpx
- [x] UI tests with Playwright
- [x] Order tests with direct DB verification
- [x] Edge case generation with Claude
- [x] GitHub Actions CI pipeline
- [ ] Allure Reports integration
