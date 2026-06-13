import re

from core.regex_library import *

class PatternDetector:

    @staticmethod
    def detect(text):

        return {

            "emails": list(
                set(
                    re.findall(
                        EMAIL_PATTERN,
                        text
                    )
                )
            ),

            "phones": list(
                set(
                    re.findall(
                        PHONE_PATTERN,
                        text
                    )
                )
            ),

            "pan_numbers": list(
                set(
                    re.findall(
                        PAN_PATTERN,
                        text
                    )
                )
            ),

            "aadhaar_numbers": list(
                set(
                    re.findall(
                        AADHAAR_PATTERN,
                        text
                    )
                )
            ),

            "gst_numbers": list(
                set(
                    re.findall(
                        GST_PATTERN,
                        text
                    )
                )
            ),

            "invoice_numbers": list(
                set(
                    re.findall(
                        INVOICE_PATTERN,
                        text
                    )
                )
            ),

            "employee_ids": list(
                set(
                    re.findall(
                        EMPLOYEE_PATTERN,
                        text
                    )
                )
            )
        }