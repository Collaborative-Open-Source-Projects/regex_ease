from .patterns import Patterns

class Validators:
    """Validation for regex patterns."""

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Checks if an email is valid."""

        return bool(Patterns.EMAIL_PATTERN.fullmatch(email))

    @staticmethod
    def get_email_domain(email: str) -> bool:
        """Extracts the domain from an email address."""

        if Validators.is_valid_email(email):
            return email.split('@')[1]
        return None

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Checks if the given URL is valid."""

        return bool(Patterns.URL_PATTERN.fullmatch(url))
