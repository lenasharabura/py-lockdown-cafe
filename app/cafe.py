import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated')

        today = datetime.date.today()
        expired_date = visitor["vaccine"]["expiration_date"]

        if expired_date < today:
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask"
            )
        return f"Welcome to {self.name}"