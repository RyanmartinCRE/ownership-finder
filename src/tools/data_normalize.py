from pydantic import BaseModel, EmailStr
from phonenumbers import parse, format_number, PhoneNumberFormat as F

class OwnerRow(BaseModel):
    Address: str
    Owner_Entity: str
    Principal_Names: str
    Email: EmailStr | None
    Phone: str | None
    LinkedIn_URL: str | None
    Status: str = "New"

def run(raw_data: list[dict], address: str, entity: str) -> dict:
    rows = []
    for d in raw_data:
        phone = d.get("phone")
        if phone:
            phone = format_number(parse(phone, "US"), F.E164)
        row = OwnerRow(
            Address=address,
            Owner_Entity=entity,
            Principal_Names=f'{d["name"]} ({d["title"]})',
            Email=d.get("email"),
            Phone=phone,
            LinkedIn_URL=d.get("linkedin"),
        )
        rows.append(row.dict())
    return {"rows": rows}
