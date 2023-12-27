from tortoise import fields
from tortoise.models import Model
from datetime import datetime
from pydantic import BaseModel



class PhishingReport(Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=512)
    reason = fields.TextField(null=True)
    real = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(default=datetime.now)

    class Meta:
        table = "phishing reports"

class mistakePhishingReport(Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=512)
    reason = fields.TextField(null=True)
    real = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(default=datetime.now)

    class Meta:
        table = "Mistake phishing reports"
class PhishingReportSchema(BaseModel):
    url: str
    reason: str

    class Config:
        orm_mode = True

class reviewDetectionSchema(BaseModel):
    review: str

    class Config:
        orm_mode = False
class newsDetectionSchema(BaseModel):
    news: str

    class Config:
        orm_mode = False