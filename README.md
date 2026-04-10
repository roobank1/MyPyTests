![CI](https://github.com/roobank1/PlayPyTest/actions/workflows/playwright.yml/badge.svg)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-green)
![Playwright](https://img.shields.io/badge/tested%20with-Playwright-45ba4b)

# 🚀 Playwright Python Automation Framework

## 📊 Live Test Report

👉 **View latest test execution report here:**
🔗 https://roobank1.github.io/PlayPyTests/playwright-report.html

* ⏱ Runs automatically every **3 hours**
* 📸 Includes screenshots for each test step
* ❌ Captures failure state for debugging
* 📊 Displays pass/fail status with detailed logs



## ⚙️ Tech Stack

* 🐍 Python
* 🎭 Playwright
* 🧪 Pytest
* 📄 Pytest-HTML (custom enhanced reporting)
* 🤖 GitHub Actions (CI/CD)



## 🔄 CI/CD Workflow

* Tests run:

  * On every push to `main`
  * Every **3 hours** via scheduled workflow
* Generates HTML report
* Publishes report to GitHub Pages



## 📁 Project Structure

```
.
├── tests/                 # Test cases
├── conftest.py            # Hooks & reporting logic
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Dependencies
└── .github/workflows/     # CI/CD pipeline
```



## ▶️ Run Tests Locally

```bash
pip install -r requirements.txt
playwright install
pytest
```

After execution:

```
playwright-report.html
```

Open it in your browser to view results.



## 📸 Reporting Features

* Step-level screenshots (even for passed tests)
* Inline screenshots in HTML report
* Failure screenshots for quick debugging
* Clean single-file report (no clutter)



## 💡 Highlights

* Lightweight and fast execution
* CI-ready setup
* No external reporting tools required
* Easy to scale for larger test suites

---

## 📬 Future Enhancements

* Slack notifications for failures
* Parallel test execution
* Advanced reporting dashboard
* Environment-based test runs

---

## 👨‍💻 Author

Maintained by **Rooban**
