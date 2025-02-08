import re

class Patterns:
    """Common regex patterns for validation."""

    # Email Pattern
    EMAIL_PATTERN = re.compile(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )

    # URL Pattern
    URL_PATTERN = re.compile(
        r"^(https?|ftp):\/\/"  # Protocol (http, https, ftp)
        r"([a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+)"  # Domain
        r"(:\d{2,5})?"  # Optional Port
        r"(\/[^\s]*)?$"  # Path
    )