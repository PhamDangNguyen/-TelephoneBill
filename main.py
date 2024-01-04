from fastapi import FastAPI, HTTPException
from models import  RecordCall, Billing
from typing import List, Union
import math

app = FastAPI()

call_logs = {} #Dictionary to save calls information 


#API record the calling
@app.put("/mobile/{user_name}/call", response_model = Union[RecordCall,str])
async def put_call(user_name:str, time_call:RecordCall):
    # Check if the username is not in call_logs
    if user_name not in call_logs:
        call_logs[user_name] = []
        call_logs[user_name].append(time_call.call_duration)
        return f"add {user_name} on the list with {time_call.call_duration} millisecond phone call"
    # Check if the username is longer than 32 characters
    if len(user_name) > 32:
        raise HTTPException(status_code = 400, detail = "Username must be shorter than 32 characters")
    # Add call information to call_logs
    call_logs[user_name].append(time_call.call_duration)
    return f"Customer {user_name} just made a {time_call.call_duration} millisecond call"


@app.get("/mobile/{user_name}/billing", response_model = Union[str, RecordCall])
async def get_billing(user_name: str, data_bill: Billing):
    #check custumer name
    if user_name not in call_logs:
        raise HTTPException(status_code = 404, detail = "The username is not on the list")
    #calculate the block parameters and total call duration
    time_call_all = 0
    for i in call_logs[user_name]:
        time_call_all += i
    data_bill.call_count = len(call_logs[user_name])
    if time_call_all % 3000 == 0:
        data_bill.block_count = time_call_all / 3000
    else:
        data_bill.block_count = math.floor(time_call_all / 3000) + 1
    print(f'The call duration for customer Đăng Nguyên is {time_call_all} seconds')
    print(f'The number of blocks for customer Đăng Nguyên is {data_bill.block_count} block')
    return f"Customer named {user_name} has to pay for {int(data_bill.block_count)} block."