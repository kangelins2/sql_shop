"""Модуль входа в программу."""

from database import Database, DatabaseSettings


def main() -> None:
    """Главная функция."""
    pas = "postgres"
    settings = DatabaseSettings(
        host="localhost",
        port=54321,
        db="postgres",
        user="postgres",
        password=pas,
    )


if name == "main":
    main()