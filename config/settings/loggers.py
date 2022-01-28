import logging
import sqlparse  # type: ignore


class SqlFormatter(logging.Formatter):
    """Formats SQL queries made by Django."""

    def format(self, record: logging.LogRecord) -> str:
        """Format the record.

        Mypy gets confused with logging, so types are ignored.
        """

        sql = record.sql.strip()  # type: ignore
        formatted_sql = sqlparse.format(sql, reindent=True)
        record.statement = formatted_sql  # type: ignore

        return super(SqlFormatter, self).format(record)
