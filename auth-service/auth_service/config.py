import decouple as dc


class Config:
    app = "auth_service.app:app"
    host = dc.config("HOST", default="localhost")
    port = dc.config("PORT", default=3000, cast=int)
    debug = dc.config("ENV", default="development") == "development"

    # db configuration
    db_host = dc.config("DB_HOST", default="localhost")
    db_port = dc.config("DB_PORT", default=5432, cast=int)
    db_user = dc.config("DB_USER", default="")
    db_password = dc.config("DB_PASSWORD", default="")
    db_name = dc.config("DB_NAME")

    # auth configuration
    jwt_secret = dc.config("JWT_SECRET")
    jwt_algorithm = dc.config("JWT_ALGORITHM")
    salt = dc.config("SALT")
