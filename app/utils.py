from datetime import datetime, date
from fastapi import HTTPException


def parse_date(date_str: str) -> date:
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use DD-MM-YYYY.")
