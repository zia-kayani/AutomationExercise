# TEST PLAN DOCUMENT

## AutomationExercise

---

## 1. Introduction

### 1.1 Purpose

The purpose of this test plan is to define the testing strategy, scope, approach, tools, and deliverables for the AutomationExercise web application. This project demonstrates end-to-end QA practice including manual testing, UI automation, API automation, performance testing, and CI/CD integration.

### 1.2 Objective

* Ensure the application is functionally correct and stable
* Validate APIs and UI flows
* Measure performance under load
* Build a scalable and maintainable automation framework
* Showcase industry-standard QA practices

---

## 2. Scope

### 2.1 In Scope

* Functional testing (UI + API)
* End-to-End testing (user flows)
* Smoke & regression testing
* API automation using Python (requests)
* UI automation using Playwright + Pytest
* Performance testing using JMeter
* CI/CD pipeline execution via GitHub Actions
* Reporting using Allure, html and other.
* Manual test case design and execution

### 2.2 Out of Scope

* Security testing (e.g., penetration testing)
* Accessibility testing (WCAG compliance)
* Cross-browser deep compatibility testing (limited coverage only)

---

## 3. Application Under Test (AUT)

Website: https://automationexercise.com

### Key Features:

* User Registration & Login
* Product Listing & Search
* Add to Cart & Checkout
* Contact Us Form
* API endpoints (products, users, authentication)

---

## 4. Test Strategy

### 4.1 Testing Levels

#### 🔹 Manual Testing

* Test case creation (excel Sheets)
* Exploratory testing
* Bug reporting and tracking

#### 🔹 API Testing

* Manual testing via Postman
* Automation using Python (requests)
* Validate:

  * Status codes
  * Response structure
  * Data correctness

#### 🔹 UI Testing

* Automation using Playwright + Pytest
* Focus on:

  * Critical user journeys
  * End-to-end flows
  * UI validations

#### 🔹 Performance Testing

* Tool: JMeter
* Scenarios:

  * Login API load test
  * Product listing API
* Metrics:

  * Response time
  * Throughput
  * Error rate

---

## 5. Test Types

* Smoke Testing
* Regression Testing
* Functional Testing
* End-to-End Testing
* API Testing
* Performance Testing

---

## 6. Test Environment

| Component      | Details               |
| -------------- | --------------------- |
| OS             | Windows / Linux / Mac |
| Language       | Python                |
| UI Tool        | Playwright            |
| Test Framework | Pytest                |
| API Tool       | Requests / Postman    |
| Performance    | JMeter                |
| CI/CD          | GitHub Actions        |
| Reporting      | Allure Reports        |

---

## 7. Test Data Management

* Stored in JSON files
* Separate test data for:

  * Users
  * Products
* Dynamic data generation where needed

---

## 8. Test Automation Strategy

### 8.1 UI Automation

* Page Object Model (POM)
* Reusable components and flows
* Fixtures for browser setup
* Assertions and validations

### 8.2 API Automation

* API client abstraction layer
* Reusable request methods
* Response validation and schema checks
* Data driven testing 

### 8.3 Test Execution

* Local execution via pytest
* CI execution via GitHub Actions

---

## 9. CI/CD Integration

### Tool: GitHub Actions

#### Pipelines:

* API Tests (on push)
* UI Tests (on pull request)
* Scheduled runs (optional)

#### Features:

* Automated test execution
* Allure report generation
* Failure notifications

---

## 10. Defect Management

* Tool: Excel Sheets
* Defect fields:

  * ID
  * Description
  * Steps to Reproduce
  * Severity
  * Priority
  * Status

---

## 11. Reporting

* Tool: Allure Reporting, pytest-html, traceviewers and screenshots 

### Includes:

* Test execution summary
* Passed/Failed tests
* Screenshots on failure
* Logs and steps

---

## 12. Entry and Exit Criteria

### Entry Criteria

* Application is accessible
* Test environment is ready
* Test data is prepared

### Exit Criteria

* All critical test cases executed
* No high severity bugs open
* Test reports generated

---

## 13. Risks and Mitigation

| Risk                      | Mitigation Strategy               |
| ------------------------- | --------------------------------- |
| Unstable test environment | Use retries and proper waits      |
| Flaky UI tests            | Use Playwright auto-waits         |
| Test data dependency      | Use dynamic or isolated test data |
| CI failures               | Debug logs and rerun strategy     |

---

## 14. Deliverables

* Test Plan Document
* Test Cases (Manual)
* Automation Framework
* API & UI Test Scripts
* Performance Test Scripts (JMeter)
* Allure Reports
* CI/CD Pipelines
* Bug Reports

---

## 15. Timeline (High-Level)

1. Setup framework
2. Manual test design
3. API automation
4. UI automation
5. Performance testing
6. CI/CD integration
7. Final reporting

---

## 16. Conclusion

This project aims to demonstrate a complete QA lifecycle including manual and automated testing practices. The framework is designed to be scalable, maintainable, and aligned with industry standards, making it suitable as a professional portfolio project.

---
