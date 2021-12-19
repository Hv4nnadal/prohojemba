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
    sqlalchemy.Column("password_hash", sqlalchemy.String(128)),
    sqlalchemy.Column("is_validated", sqlalchemy.Boolean),
    sqlalchemy.Column("is_banned", sqlalchemy.Boolean)
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
    # 1 - В процессе, 2 - Заброшено, 3 - Пройдено, 4 - 100%
    sqlalchemy.Column("status",
                      sqlalchemy.Integer,
                      ),
    sqlalchemy.Column("review_text", sqlalchemy.String(1024), nullable=True),

    sqlalchemy.Column("rate", sqlalchemy.Boolean, nullable=True)
)


titles = sqlalchemy.Table(
    "titles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("cover", sqlalchemy.String(256)),
    # 1 - Игра, 2 - Фильм, 3 - Сериал, 4 - Аниме
    sqlalchemy.Column("type", sqlalchemy.Integer),
    sqlalchemy.Column("description", sqlalchemy.String(1024)),

    sqlalchemy.Column("rates_count", sqlalchemy.Integer),
    sqlalchemy.Column("positive_rates_count", sqlalchemy.Integer)
)
