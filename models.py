from pydantic import BaseModel

class RecordCall(BaseModel):
    call_duration: int

class Billing(BaseModel):
    call_count: int = 0
    block_count: int = 0