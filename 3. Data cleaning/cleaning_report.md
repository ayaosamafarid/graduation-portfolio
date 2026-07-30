# Cleaning Report – Dataset A

## Dataset Information

- **Original File:** `dataset_A_legal_termbase_RAW.csv`
- **Cleaned File:** `dataset_A_legal_termbase_ABSOLUTE_CLEAN.csv`

---

## Dataset Statistics

| Item | Count |
|------|------:|
| Rows before cleaning | 104 |
| Rows after cleaning | 86 |
| Rows removed | 18 |

---

## Cleaning Operations Performed

The following cleaning steps were applied to the dataset:

- Removed duplicate and near-duplicate records.
- Fixed character encoding (Mojibake) issues.
- Removed HTML tags.
- Removed HTML entities such as `&nbsp;`.
- Removed extra spaces and unnecessary special characters.
- Cleaned malformed and corrupted text.
- Standardized the CSV structure and delimiters.
- Removed invalid and corrupted records.
- Standardized text formatting where applicable.
- Produced a consistent dataset suitable for further processing and analysis.

---

## Dataset Restructuring

The original dataset contained formatting problems that prevented it from being parsed correctly as a structured CSV file. During the cleaning process, the dataset was **restructured** by:

- Restoring the correct CSV format.
- Organizing records into consistent columns.
- Correcting malformed rows.
- Producing a valid tabular dataset that can be loaded directly using Pandas or other data analysis tools.

This restructuring was necessary to make the dataset usable while preserving the valid information contained in the original file.

---

## Comparison

### Before Cleaning

- Duplicate records.
- Character encoding (Mojibake) errors.
- HTML tags and HTML entities.
- Extra whitespace.
- Corrupted rows.
- Inconsistent CSV formatting.
- Dataset could not be reliably parsed into structured columns.

### After Cleaning

- Duplicate records removed.
- Character encoding corrected.
- HTML content removed.
- Whitespace normalized.
- Corrupted rows removed.
- Consistent CSV formatting.
- Dataset successfully reconstructed into a structured table.
- Ready for analysis using Pandas or spreadsheet software.

---

## Conclusion

The dataset has been successfully cleaned and restructured. All major formatting, encoding, duplication, and structural issues found in the original dataset were addressed, resulting in a clean and consistent dataset suitable for analysis and further processing.