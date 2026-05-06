# Performance Test Strategy – AutomationExercise API

## 1. Objective

The objective of this performance testing effort is to evaluate the responsiveness, stability, and scalability of key APIs of the AutomationExercise application under different load conditions.

This includes identifying performance bottlenecks and ensuring the system meets defined Service Level Agreements (SLAs).

---

## 2. Scope

### In Scope APIs

The following APIs are selected based on real user behavior and business criticality:

* Get All Products List
* Get All Brands List
* Search Product
* Verify Login (valid users)
* Create/Register User
* Get User Details by Email

### Out of Scope APIs

The following APIs are excluded as they represent negative or low-frequency scenarios:

* Invalid login scenarios
* Missing parameter APIs
* Delete user account
* Update brand/product APIs

---

## 3. Test Scenarios

### Scenario 1: Browse Products

* Get All Products
* Get All Brands

### Scenario 2: Search Products

* Search product using keyword

### Scenario 3: User Login Flow

* Login with valid credentials
* Fetch user details

### Scenario 4: User Registration Flow

* Register new user
* Login with created user

---

## 4. Workload Model

* Total Virtual Users: 100
* Ramp-up Time: 60 seconds
* Test Duration: 5 minutes
* Think Time: 2 seconds between requests

### Traffic Distribution

* Browse Products: 40%
* Search: 30%
* Login Flow: 20%
* Registration Flow: 10%

---

## 5. Test Types

* Load Testing: Validate system under expected load
* Stress Testing: Identify system breaking point
* Spike Testing: Evaluate behavior under sudden traffic spikes

---

## 6. Test Environment

* Base URL: https://automationexercise.com/api
* Tool: Apache JMeter
* Execution Mode:GUI + Non-GUI (CLI)

---

## 7. Test Data

Test data will be parameterized using CSV files:

* users.csv → login credentials
* search.csv → search keywords

---

## 8. Success Criteria (SLA)

* Average Response Time < 2000 ms
* 90th Percentile Response Time < 3000 ms
* Error Rate < 5%
* System should handle 100 concurrent users without failure

---

## 9. Risks & Assumptions

### Risks

* Public API environment may have unstable performance
* Data persistence may affect repeated test runs

### Assumptions

* APIs are available and stable during testing
* No rate limiting is enforced

---

## 10. Deliverables

* JMeter Test Plan (.jmx)
* Test Execution Results (.jtl)
* HTML or Allure Report
* Performance Analysis Report
* CI/CD Pipeline Integration using Github Actions

---
 