# Cleaning Report – Dataset B

## Dataset Information

- **Original File:** `dataset_B_company_ledger_RAW.csv`
- **Cleaned File:** `company_ledger_MARCH_PERFECT.csv`

---

## Dataset Statistics

| Item | Count |
|------|------:|
| Rows before cleaning | 50 |
| Rows after cleaning | 39 |
| Rows removed | 11 |

---

## Cleaning Operations Performed

The following cleaning steps were applied to the dataset:

- Removed exact duplicate records.
- Removed near-duplicate transactions while preserving the most complete and accurate record.
- Removed invalid records containing `TBD`, `#REF!`, and missing amount values.
- Standardized all dates to ISO 8601 format (`YYYY-MM-DD`).
- Standardized currency codes (`EGP` and `USD`).
- Created a unified `Amount_EGP` column by converting USD transactions to EGP using a fixed exchange rate.
- Standardized transaction types (`Income` and `Expense`).
- Standardized transaction category names.
- Standardized transaction descriptions where applicable.
- Removed unnecessary whitespace.
- Standardized text capitalization.
- Corrected malformed numeric values.
- Removed thousand separators from numeric fields.
- Converted refund amounts written in parentheses into negative numeric values.
- Produced a clean and consistent dataset suitable for financial analysis.

---

## Dataset Restructuring

The original dataset contained several data quality issues including duplicate transactions, inconsistent date formats, mixed currencies, invalid values, inconsistent category names, malformed numeric values, and inconsistent transaction formatting.

During the cleaning process, the dataset was **restructured** by:

- Standardizing all date formats.
- Standardizing transaction categories and transaction types.
- Cleaning malformed numeric fields.
- Creating a unified `Amount_EGP` column for consistent financial analysis.
- Removing duplicate and invalid records.
- Producing a structured dataset that can be loaded directly using Pandas or other spreadsheet software.

This restructuring improved data consistency while preserving the original financial information.

---

## Assumptions

The following assumptions were applied during the cleaning process:

- A fixed exchange rate of **1 USD = 50 EGP** was used to convert all USD transactions into Egyptian Pounds.
- Refund transactions were treated as **Contra-Revenue (negative revenue)** because they reduce previously recognized revenue rather than representing operating expenses.
- Owner drawing transactions were classified as **Equity Withdrawal (Non-Operating)**.
- Equipment purchases were classified as **Capital Expenditure (CapEx)** because they represent long-term business assets.
- Ambiguous numeric values were interpreted according to the surrounding accounting records before standardization.
- Exact and near-duplicate transactions were removed before performing any financial calculations or analysis.

---

## Comparison

### Before Cleaning

- Exact duplicate transactions.
- Near-duplicate transactions.
- Mixed date formats.
- Mixed currencies (EGP and USD).
- Invalid values (`TBD`, `#REF!`, and blank amount fields).
- Inconsistent transaction categories.
- Inconsistent transaction types.
- Malformed numeric values.
- Thousand separators inside numeric fields.
- Refund values represented using parentheses.
- Inconsistent capitalization and text formatting.

### After Cleaning

- Duplicate transactions removed.
- Invalid records removed.
- Dates standardized to ISO 8601 format.
- Currency values standardized.
- USD transactions converted to EGP.
- Unified `Amount_EGP` column created.
- Numeric values standardized.
- Refund values converted into negative numbers.
- Transaction categories standardized.
- Transaction types standardized.
- Consistent capitalization and formatting.
- Dataset ready for analysis using Pandas or spreadsheet software.

---

## Conclusion

The dataset has been successfully cleaned and standardized. Duplicate transactions, invalid records, inconsistent dates, mixed currencies, malformed numeric values, and inconsistent category names were corrected. A unified `Amount_EGP` column was created to normalize financial values across different currencies. Business assumptions were documented and applied consistently throughout the cleaning process. The final dataset is clean, consistent, and suitable for financial analysis and further processing.