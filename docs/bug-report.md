# Bug Report – SauceDemo

# Bug Information

- **Bug ID:** BUG-001
- **Title:** When i use the filter button to sort the items in the inventory in descending order it sends me an alert message.
- **Related Test Case:** TC-006
- **Module:** Inventory
- **Severity:** Medium
- **Priority:** Medium
- **Status:** Open

## Environment

- Operating System: CachyOS Linux
- Browser: Brave
- Application: https://www.saucedemo.com/

## Steps to Reproduce

1. Open the inventory page.
2. Select Name (Z to A).
3. Inspect the product order.

## Expected Result

Products should appear in alphabetical Descending order.

## Actual Result

Product sorting is broken and gives an alert message.

## Evidence

SauceDemo E-Commerce QA Testing/Evidence/Z-A_sorting_Failure.png

## Additional Notes

After a while when i finished checking checkouts at the last is was sorting the items as per the filter selected.

# Bug Information

- **Bug ID:** BUG-002
- **Title:** When i use the filter button to sor the items in the inventory in ascebding price order it sends me an alert message.
- **Related Test Case:** TC-007
- **Module:** Inventory
- **Severity:** Medium
- **Priority:** Medium
- **Status:** Open

## Environment

- Operating System: CachyOS Linux
- Browser: Brave
- Application: https://www.saucedemo.com/

## Steps to Reproduce

1. Open the inventory page.
2. Select Price (Low to High).
3. Inspect the displayed price.

## Expected Result

Products should appear in ascending price order.

## Actual Result

Product sorting is broken and gives an alert message.

## Evidence

SauceDemo E-Commerce QA Testing/Evidence/Price-Sorting_Failure.png

## Additional Notes

After a while when i finished checking checkouts at the last is was sorting the items as per the filter selected.

# Bug Information

- **Bug ID:** BUG-003
- **Title:** it didnt let me enter the last name for the checkout but it proceed to the next step without the last name.
- **Related Test Case:** TC-016
- **Module:** Checkout
- **Severity:** High
- **Priority:** High
- **Status:** Open

## Environment

- Operating System: CachyOS Linux
- Browser: Brave
- Application: https://www.saucedemo.com/

## Steps to Reproduce

1. Open the shopping cart.
2. Click Checkout.
3. Click inside the Last Name field.
4. Type "Dahal".
5. Attemp to Paste Dahal into the field.
6. Repeat the test in the incognito session.

## Expected Result

All customer information fields should accept input, and the user should proceed to the checkout overview page.

## Actual Result

First Name and Postal Code accept keyboard input. The Last Name field receives focus but does not accept typed or pasted text. The same behavior occurs in an Incognito session.

## Evidence

SauceDemo E-Commerce QA Testing/Evidence/Last-Name-notEntered.png

## Additional Notes



# Bug Information

- **Bug ID:** BUG-004
- **Title:** No Successful Payment Confirmation Page was shown after clocking the finish button.
- **Related Test Case:** TC-014
- **Module:** Order Processing
- **Severity:** High
- **Priority:** High
- **Status:** Open

## Environment

- Operating System: CachyOS Linux
- Browser: Brave
- Application: https://www.saucedemo.com/

## Steps to Reproduce

1. Click Finish.
2. Inspect the Confirmation Page.

## Expected Result

Order should be completed and a success confirmation should appear.

## Actual Result

While clicking finish no action is performed, no success confirmation appeared.

## Evidence

SauceDemo E-Commerce QA Testing/Evidence/NoConfirmationPage.png

## Additional Notes

