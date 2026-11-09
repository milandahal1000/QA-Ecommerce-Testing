# Manual Test Cases – SauceDemo E-Commerce Application

**Project:** SauceDemo QA Testing  
**Application:** https://www.saucedemo.com/  
**Execution Status:** Not Started  
**Tester:** QA Portfolio Project

## Test Data

Use the demo credentials displayed on the SauceDemo login page.

- Valid user: `standard_user`
- Invalid user: `invalid_user`
- Password: Use the currently displayed demo password.
- First name: Milan
- Last name: Dahal
- Postal code: 44600

## Module 1: Authentication

### TC-001: Login with valid credentials
- **Priority:** High
- **Precondition:** Login page is accessible.
- **Steps:**
  1. Enter valid username.
  2. Enter valid password.
  3. Click Login.
- **Expected:** User should successfully reach the inventory page.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-002: Login with invalid credentials
- **Priority:** High
- **Steps:**
  1. Enter an invalid username.
  2. Enter an invalid password.
  3. Click Login.
- **Expected:** Login should be rejected with an appropriate error message.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-003: Login with empty fields
- **Priority:** Medium
- **Steps:**
  1. Leave username empty.
  2. Leave password empty.
  3. Click Login.
- **Expected:** Application should prevent login and display a validation message.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-004: Logout functionality
- **Priority:** High
- **Precondition:** User is logged in.
- **Steps:**
  1. Open the navigation menu.
  2. Click Logout.
- **Expected:** User should be redirected to the login page.
- **Actual:** Not executed.
- **Status:** Not Run.

## Module 2: Inventory and Products

### TC-005: Verify inventory product display
- **Priority:** High
- **Steps:**
  1. Log in.
  2. Open the inventory page.
  3. Inspect product names, prices and images.
- **Expected:** Available products should display correctly with their relevant information.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-006: Sort products by name
- **Priority:** Medium
- **Steps:**
  1. Open the inventory page.
  2. Select Name (A to Z).
  3. Inspect the product order.
- **Expected:** Products should appear in alphabetical ascending order.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-007: Sort products by price
- **Priority:** Medium
- **Steps:**
  1. Open the inventory page.
  2. Select Price (low to high).
  3. Inspect the displayed prices.
- **Expected:** Products should appear in ascending price order.
- **Actual:** Not executed.
- **Status:** Not Run.

## Module 3: Shopping Cart

### TC-008: Add product to cart
- **Priority:** High
- **Steps:**
  1. Log in.
  2. Select any available product.
  3. Click Add to cart.
- **Expected:** Product should be added and the cart badge should update.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-009: Remove product from cart
- **Priority:** High
- **Precondition:** At least one product is in the cart.
- **Steps:**
  1. Open the shopping cart.
  2. Click Remove on a selected product.
- **Expected:** Selected product should be removed and the cart count should update.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-010: Verify cart item count
- **Priority:** Medium
- **Steps:**
  1. Add one product to the cart.
  2. Add another product.
  3. Inspect the cart badge.
- **Expected:** Cart badge should reflect the number of selected products.
- **Actual:** Not executed.
- **Status:** Not Run.

## Module 4: Checkout

### TC-011: Checkout with valid customer information
- **Priority:** High
- **Precondition:** At least one product is in the cart.
- **Steps:**
  1. Open the cart.
  2. Click Checkout.
  3. Enter first name, last name and postal code.
  4. Click Continue.
- **Expected:** User should proceed to the checkout overview page.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-012: Checkout with missing information
- **Priority:** High
- **Precondition:** At least one product is in the cart.
- **Steps:**
  1. Open the cart.
  2. Click Checkout.
  3. Leave one or more required fields empty.
  4. Click Continue.
- **Expected:** Application should prevent progression and display an appropriate validation message.
- **Actual:** Not executed.
- **Status:** Not Run.

## Module 5: Order Processing

### TC-013: Verify order overview calculations
- **Priority:** High
- **Precondition:** User has reached the checkout overview page.
- **Steps:**
  1. Inspect selected products.
  2. Calculate the sum of product prices.
  3. Inspect subtotal, tax and total.
- **Expected:** Subtotal should equal the sum of product prices, and total should correctly include applicable tax.
- **Actual:** Not executed.
- **Status:** Not Run.

### TC-014: Complete an order successfully
- **Priority:** High
- **Precondition:** User is on the checkout overview page with valid information.
- **Steps:**
  1. Click Finish.
  2. Inspect the confirmation page.
- **Expected:** Order should be completed and a success confirmation should appear.
- **Actual:** Not executed.
- **Status:** Not Run.

## Module 6: Navigation

### TC-015: Verify checkout navigation
- **Priority:** Medium
- **Precondition:** User has reached the checkout overview page.
- **Steps:**
  1. Click Cancel.
  2. Observe the destination.
  3. Navigate back to the cart if necessary.
- **Expected:** User should be returned to the appropriate previous shopping workflow without an unintended order being placed.
- **Actual:** Not executed.
- **Status:** Not Run.

---

## Execution Summary

| Metric | Initial value |
|---|---:|
| Total test cases | 15 |
| Passed | 0 |
| Failed | 0 |
| Blocked | 0 |
| Not Run | 15 |

**Important:** Update actual results and statuses only after executing each test case. Do not treat unexecuted cases as passed.