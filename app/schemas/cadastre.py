from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator


class CadastreBase(BaseModel):
    cadastre_number: Optional[str] = Field(
        pattern=r'^\d{2}:\d{2}:\d{6,7}:\d+$'
    )
    latitude: Optional[str] = Field(pattern=r'^[+-]?\d{1,2}.\d+$')
    longitude: Optional[str] = Field(pattern=r'^[+-]?1?\d{1,2}.\d+$')

    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            'example': {
                'cadastre_number': '12:34:1234567:12',
                'latitude': '+23.456',
                'longitude': '-123.456',
            }
        }
    )

    @field_validator('latitude')
    @classmethod
    def check_latitude(cls, value: str):
        if value is None:
            error = 'Значение широты не может быть пустым!'
            raise ValueError(error)
        if value[0] in ('+-'):
            float_value = float(value[1:])
        else:
            float_value = float(value)
        if float_value > 90:
            error = 'Значение широты должно быть между -90 и 90'
            raise ValueError(error)
        return value

    @field_validator('longitude')
    @classmethod
    def check_longitude(cls, value: str):
        if value is None:
            error = 'Значение долготы не может быть пустым!'
            raise ValueError(error)
        if value[0] in ('+-'):
            float_value = float(value[1:])
        else:
            float_value = float(value)
        if float_value > 180:
            error = 'Значение долготы должно быть между -180 и 180'
            raise ValueError(error)
        return value
