import re

EMAIL_PATTERN = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

PHONE_PATTERN = r'(?:\+91)?[6-9]\d{9}'

PAN_PATTERN = r'[A-Z]{5}[0-9]{4}[A-Z]'

AADHAAR_PATTERN = r'\d{4}\s?\d{4}\s?\d{4}'

GST_PATTERN = r'\d{2}[A-Z]{5}[0-9]{4}[A-Z][A-Z0-9]Z[A-Z0-9]'

INVOICE_PATTERN = r'INV[-/]?\d+'

EMPLOYEE_PATTERN = r'EMP[-_]?\d+'