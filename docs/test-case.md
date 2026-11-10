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
- **Actual:** Successfully reached the inventory page.
- **Status:** Pass.

### TC-002: Login with invalid credentials
- **Priority:** High
- **Steps:**
  1. Enter an invalid username.
  2. Enter an invalid password.
  3. Click Login.
- **Expected:** Login should be rejected with an appropriate error message.
- **Actual:** login failed and displayed an appropriate error message.
- **Status:** Pass.

### TC-003: Login with empty fields
- **Priority:** Medium
- **Steps:**
  1. Leave username empty.
  2. Leave password empty.
  3. Click Login.
- **Expected:** Application should prevent login and display a validation message.
- **Actual:** Login failed with error message "username is required".
- **Status:** Pass.

### TC-004: Logout functionality
- **Priority:** High
- **Precondition:** User is logged in.
- **Steps:**
  1. Open the navigation menu.
  2. Click Logout.
- **Expected:** User should be redirected to the login page.
- **Actual:** User is redirected to the login page.
- **Status:** Pass.

## Module 2: Inventory and Products

### TC-005: Verify inventory product display
- **Priority:** High
- **Steps:**
  1. Log in.
  2. Open the inventory page.
  3. Inspect product names, prices and images.
- **Expected:** Available products should display correctly with their relevant information.
- **Actual:** Available products are displayed with their images, price and description.
- **Status:** Pass.

### TC-006: Sort products by name
- **Priority:** Medium
- **Steps:**
  1. Open the inventory page.
  2. Select Name (Z to A).
  3. Inspect the product order.
- **Expected:** Products should appear in alphabetical Descending order.
- **Actual:** Product sorting is broken and gives an alert message.
- **Status:** Fail.

### TC-007: Sort products by price
- **Priority:** Medium
- **Steps:**
  1. Open the inventory page.
  2. Select Price (low to high).
  3. Inspect the displayed prices.
- **Expected:** Products should appear in ascending price order.
- **Actual:** Sorting is broken and sends an alert message.
- **Status:** Fail.

## Module 3: Shopping Cart

### TC-008: Add product to cart
- **Priority:** High
- **Steps:**
  1. Log in.
  2. Select any available product.
  3. Click Add to cart.
- **Expected:** Product should be added and the cart badge should update.
- **Actual:** Added items to the cart and the cart badge also is updated..
- **Status:** Pass.

### TC-009: Remove product from cart
- **Priority:** High
- **Precondition:** At least one product is in the cart.
- **Steps:**
  1. Open the shopping cart.
  2. Click Remove on a selected product.
- **Expected:** Selected product should be removed and the cart count should update.
- **Actual:** Cart item is removed and badge count also updated.
- **Status:** Pass.

### TC-010: Verify cart item count
- **Priority:** Medium
- **Steps:**
  1. Add one product to the cart.
  2. Add another product.
  3. Inspect the cart badge.
- **Expected:** Cart badge should reflect the number of selected products.
- **Actual:** Cart badge is reflecting the numbeer of selected products.
- **Status:** Pass.

## Module 4: Checkout

### TC-011: Checkout with valid customer information
- **Priority:** High
- **Precondition:** At least one product is in the cart.
- **Steps:**
  1. Open the cart.
  2. Click Checkout.
  3. Enter first name.
  4. Enter last name.
  5. Enter postal code.
  6. Click Continue.
- **Expected:** All customer information fields should accept input, and the user should proceed to the checkout overview page.
- **Actual:** First Name and Postal Code accept keyboard input. The Last Name field receives focus but does not accept typed or pasted text. The same behavior occurs in an Incognito session.
- **Status:** Blocked – Unable to complete valid checkout due to Last Name field input issue.

### TC-012: Checkout with missing information
- **Priority:** High
- **Precondition:** At least one product is in the cart.
- **Steps:**
  1. Open the cart.
  2. Click Checkout.
  3. Leave one or more required fields empty.
  4. Click Continue.
- **Expected:** Application should prevent progression and display an appropriate validation message.
- **Actual:** Proper error message is displayed and it prevents progression.
- **Status:** Pass.

## Module 5: Order Processing

### TC-013: Verify order overview calculations
- **Priority:** High
- **Precondition:** User has reached the checkout overview page.
- **Steps:**
  1. Inspect selected products.
  2. Calculate the sum of product prices.
  3. Inspect subtotal, tax and total.
- **Expected:** Subtotal should equal the sum of product prices, and total should correctly include applicable tax.
- **Actual:** The total of product is correct with applicable tax and subtotal is also correct.
- **Status:** Pass.

### TC-014: Complete an order successfully
- **Priority:** High
- **Precondition:** User is on the checkout overview page with valid information.
- **Steps:**
  1. Click Finish.
  2. Inspect the confirmation page.
- **Expected:** Order should be completed and a success confirmation should appear.
- **Actual:** While clicking finish no action is performed, no success confirmation appeared.
- **Status:** Fail.

## Module 6: Navigation

### TC-015: Verify checkout navigation
- **Priority:** Medium
- **Precondition:** User has reached the checkout overview page.
- **Steps:**
  1. Click Cancel.
  2. Observe the destination.
  3. Navigate back to the cart if necessary.
- **Expected:** User should be returned to the appropriate previous shopping workflow without an unintended order being placed.
- **Actual:** It redirects to the inventory page and no unintended order has been placed.
- **Status:** Pass.

## Module 7: Checkout - Costumer Information

### TC-016: Verify last name field accepts user inputs

- **Priority:** High
- **Precondition:** User is logged in and has at least one product in the cart.
- **Steps:**
  1. Open the shopping cart.
  2. Click Checkout.
  3. Click inside the Last Name field.
  4. Type "Dahal".
  5. Attemp to Paste Dahal into the field.
  6. Repeat the test in the incognito session.
- **Expected:** The Last Name field should accept both keyboard input and pasted text.
- **Actual:** The field receives focus, but neither typed nor pasted text appears. The behavior persists in Incognito.
- **Status:** Fail – Requires further investigation.


---

## Execution Summary

| Metric | Initial value |
|---|---:|
| Total test cases | 16 |
| Passed | 11 |
| Failed | 4 |
| Blocked | 1 |
| Not Run | 0 |

**Important:** Update actual results and statuses only after executing each test case. Do not treat unexecuted cases as passed.