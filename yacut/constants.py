from string import ascii_lowercase, ascii_uppercase, digits

GENERATED_SHORT_ID_LENGTH = 6
LEGAL_CHARS = ascii_uppercase + ascii_lowercase + digits
RE_LEGAL_CAHRS = """^[a-zA-z0-9]{0,16}$"""

MAIN_URL = 'http://localhost/'
