import sqlalchemy

from .base import metadata


# Таблица пользователей
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("username", sqlalchemy.String(64), unique=True),
    sqlalchemy.Column("email", sqlalchemy.String(64), unique=True, index=True),
    sqlalchemy.Column("avatar", sqlalchemy.String(256), nullable=True),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Column("is_validated", sqlalchemy.Boolean)
)


# Таблица refresh токенов пользователей
sessions = sqlalchemy.Table(
    "sessions",
    metadata,
    sqlalchemy.Column("user_id",
                      sqlalchemy.Integer,
                      sqlalchemy.ForeignKey("users.id", ondelete="CASCADE")
                      ),
    sqlalchemy.Column("refresh_token", sqlalchemy.String(128), index=True),
    sqlalchemy.Column("expires_in", sqlalchemy.DateTime)
)


# Таблица прохождений пользователя
walks = sqlalchemy.Table(
    "walks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("user_id",
                      sqlalchemy.Integer,
                      sqlalchemy.ForeignKey("users.id", ondelete="CASCADE")
                      ),
    sqlalchemy.Column("title_id",
                      sqlalchemy.Integer,
                      sqlalchemy.ForeignKey("titles.id", ondelete="CASCADE")
                      ),
    sqlalchemy.Column("status", sqlalchemy.String(16)), # Берется из WALK_STATUSES в настройках
    sqlalchemy.Column("comment", sqlalchemy.String(1024), nullable=True),

    sqlalchemy.Column("rate", sqlalchemy.Boolean, nullable=True)
)


# Таблица тайтлов
titles = sqlalchemy.Table(
    "titles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("cover", sqlalchemy.String(256)),
    sqlalchemy.Column("description", sqlalchemy.String(1024)),

    sqlalchemy.Column("type", sqlalchemy.String(16)),   # Тип берется из TITLE_GENRES в настройках
    sqlalchemy.Column("release_year", sqlalchemy.Integer),

    sqlalchemy.Column("positive_rates_count", sqlalchemy.Integer),
    sqlalchemy.Column("negative_rates_count", sqlalchemy.Integer)
)

