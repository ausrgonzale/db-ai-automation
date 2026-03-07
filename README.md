# DB AI Automation 🤖🗄️

An AI-powered automated testing framework for a fake e-commerce API using FastAPI, MySQL, Playwright, and pytest — with AI-generated test data via the Anthropic API.

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

### 3. Create the requirements.txt file
```bash
cat > requirements.txt << 'REQS'
# Web framework
fastapi==0.111.0
uvicorn==0.29.0

# Database
sqlalchemy==2.0.30
pymysql==1.1.1
cryptography==42.0.7

# Data validation
pydantic==2.7.1

# AI data generation
anthropic==0.25.8
faker==25.0.1
python-dotenv==1.0.1

# Testing
pytest==8.2.0
pytest-asyncio==0.23.6
pytest-html==4.1.1
pytest-playwright==0.5.0
httpx==0.27.0
REQS
```

### 4. Install all packages
```bash
pip install -r requirements.txt
playwright install
```

---

## 📂 Create Project Structure

### Create folders
```bash
mkdir app
mkdir data_gen
mkdir tests
mkdir tests/api
mkdir tests/ui
mkdir reports
```

### Create empty files
```bash
touch app/__init__.py
touch app/database.py
touch app/models.py
touch app/main.py
touch app/schemas.py
touch data_gen/__init__.py
touch data_gen/ai_generator.py
touch tests/conftest.py
touch tests/api/test_products.py
touch tests/api/test_users.py
touch tests/ui/test_storefront.py
touch pytest.ini
touch .env
```

### Verify structure
```bash
find . -not -path './venv/*' -type f
```
You should see 14 files listed.

---

## 📂 Project Structure
```
db-ai-automation/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app and routes
│   ├── models.py         # SQLAlchemy DB models
│   ├── database.py       # MySQL connection setup
│   └── schemas.py        # Pydantic request/response shapes
├── data_gen/
│   ├── __init__.py
│   └── ai_generator.py   # AI + Faker data generation
├── tests/
│   ├── conftest.py       # Shared pytest fixtures (DB seed/teardown)
│   ├── api/
│   │   ├── test_users.py
│   │   ├── test_products.py
│   │   └── test_orders.py
│   └── ui/
│       └── test_storefront.py
├── .env                  # API keys and DB credentials (never commit this)
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🔑 Configure Environment Variables

Edit `.env` and fill in your credentials:
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

---

## 🟢 Health Check

| Tool       | Command               | Expected Output         |
|------------|-----------------------|-------------------------|
| Homebrew   | `brew --version`      | `Homebrew 4.x.x`        |
| MySQL      | `mysql --version`     | `mysql  Ver 8.x.x`      |
| Python     | `python3 --version`   | `Python 3.12.12`        |
| Virtual env| check terminal prompt | starts with `(venv)`    |
| pip        | `which pip`           | path contains `/venv/`  |

---

## ▶️ Running the Project

### Start the API server (Terminal window 1)
```bash
uvicorn app.main:app --reload
```

### Run all tests (Terminal window 2)
```bash
pytest
```

### View the HTML test report
```bash
open reports/test_report.html
```

---

## 🗺️ Roadmap

- [x] Project scaffolding
- [x] MySQL + SQLAlchemy setup
- [x] AI data generation with Anthropic API
- [ ] API tests with pytest + httpx
- [ ] UI tests with Playwright
- [ ] Order tests with direct DB verification
- [ ] Edge case generation with Claude
- [ ] GitHub Actions CI pipeline
- [ ] Allure Reports integration
