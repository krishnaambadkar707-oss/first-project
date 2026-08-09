import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a plaintext password with bcrypt directly (no passlib).
    bcrypt only uses the first 72 bytes of input, so longer
    passwords are truncated safely rather than raising an error.
    """

    password_bytes = password.encode("utf-8")[:72]

    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:

    plain_bytes = plain_password.encode("utf-8")[:72]

    try:
        hashed_bytes = hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_bytes, hashed_bytes)
    except ValueError:
        # Malformed/legacy hash stored in the DB.
        return False
