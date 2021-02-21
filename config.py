import os

### DATABASE
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "pupoculo")
DB_HOST = os.environ.get("DB_HOST", "balbol_db")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "balbol")
DB_CONFIG = {
    "USER": DB_USER,
    "PASSWORD": DB_PASSWORD,
    "HOST": DB_HOST,
    "PORT": DB_PORT,
    "NAME": DB_NAME,
}

SQLALCHEMY_DATABASE_URI = (
    f"postgres://{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['NAME']}"
)
