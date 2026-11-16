"""Data/hora, tudo é gravado em UTC"""

from datetime import datetime, timezone


def agora() -> datetime:
    return datetime.now(timezone.utc)


def como_utc(valor: datetime | None) -> datetime | None:
    if valor is None:
        return None
    if valor.tzinfo is None:
        return valor.replace(tzinfo=timezone.utc)
    return valor.astimezone(timezone.utc)
