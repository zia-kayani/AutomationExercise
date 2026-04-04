#   AutomationExercise 

A complete end-to-end QA automation project built on industry best practices. This project demonstrates manual testing, API automation, UI automation, performance testing, and CI/CD integration using modern tools and a scalable framework design.

---

## 📌 Project Overview

This repository contains a full-fledged QA automation framework developed for the AutomationExercise web application.

It showcases:

* Real-world test automation architecture
* Clean and scalable framework design
* Integration of UI, API, and performance testing
* CI/CD pipeline using GitHub Actions

---

## 🧰 Tech Stack

| Category            | Tools & Technologies                |
| ------------------- | ----------------------------------- |
| Language            | Python                              |
| Test Framework      | Pytest                              |
| UI Automation       | Playwright                          |
| API Automation      | Requests (Python), Postman (Manual) |
| Performance Testing | JMeter                              |
| Reporting           | Allure Reports , pytest-html                      |
| CI/CD               | GitHub Actions                      |
| Bug Tracking        | Excel Sheets                       |

---

## 🏗️ Framework Architecture

The project follows a **modular and scalable design**:

```
qa-automation-framework/
│
├── tests/                 # Test cases (UI + API)
├── framework/             # Core framework (POM, API clients, utils)
├── test_data/             # Test data (JSON)
├── performance/           # JMeter scripts
├── reports/               # Allure reports
├── manual/                # Manual QA artifacts
├── .github/workflows/     # CI/CD pipelines
```

### Key Design Patterns:

* ✅ Page Object Model (POM)
* ✅ API Client Abstraction
* ✅ Reusable Fixtures
* ✅ Separation of Concerns

---


## Test Coverage

### 🔹 UI Automation

* Login / Signup
* Product search
* Add to cart
* Checkout flow

### 🔹 API Automation

* Get products list
* User authentication
* Create / validate users

### 🔹 Manual Testing

* Test cases documented
* Exploratory testing
* Bug reporting

### 🔹 Performance Testing

* Login API load testing
* Product API performance validation

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/zia-kayani/AutomationExercise.git
cd automationexercise
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest
```

### Run UI tests

```bash
pytest tests/ui
```

### Run API tests

```bash
pytest tests/api
```

### Run by marker

```bash
pytest -m smoke
pytest -m regression
```

---

## 📊 Allure Reporting

### Generate report

```bash
#for API 
pytest --alluredir=reports/allure
allure serve reports/allure
```

### Features:

* Test execution summary
* Step-wise reporting
* Screenshots on failure
* Logs and attachments

---

## CI/CD Pipeline

Implemented using GitHub Actions.

### Workflows:

* ✅ API tests on push
* ✅ UI tests on pull request
* ✅ Automated reporting

### Benefits:

* Continuous testing
* Faster feedback
* Reliable builds

---

## 📈 Performance Testing

* Tool: **JMeter**
* Location: `performance/jmeter/`

### Scenarios:

* Load testing (Login API)
* Stress testing (Product APIs)

---

## 🐞 Bug Tracking

* Managed via **Google Sheets**
* Includes:

  * Bug description
  * Steps to reproduce
  * Severity & priority
  * Status tracking

---

## 📁 Manual Testing Artifacts

Located in `/manual`:

* Test Plan
* Test Cases
* Bug Reports

---

##  Key Highlights

* ✅ End-to-end QA coverage (Manual + Automation)
* ✅ Clean and maintainable framework
* ✅ Real-world CI/CD integration
* ✅ Scalable architecture
* ✅ Industry best practices followed

---

## 📌 Future Enhancements

* Docker integration
* Parallel test execution
* Advanced reporting dashboards
* Cross-browser execution matrix

---

##  Contribution

This is a personal portfolio project, but suggestions and improvements are welcome.

---

## 📬 Contact

For queries or collaboration, feel free to reach out.
ziakayani.official@gmail.com

---

## ⭐ Final Note

This project is designed to demonstrate practical QA engineering skills including:

* Framework design
* Automation strategy
* CI/CD integration
* Real-world testing practices

---
