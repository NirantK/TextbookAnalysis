import logging
from functools import lru_cache
from pathlib import Path
from typing import Optional, Union

from fastapi import FastAPI
from fastapi.logger import logger
import boto3
from botocore.exceptions import ClientError

logger.setLevel(logging.DEBUG)

PathLike = Union[Path, str]
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Textbook Analysis API"}

def update_count(current_count, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('names')
    response = table.put_item(
       Item={
            "id" : "1",
            "item" : "count",
            'count': current_count
        }
    )
    return response

def get_count(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    table = dynamodb.Table('names')

    try:
        response = table.query( KeyConditionExpression=Key("item").eq("count"))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return int(response["Item"]["count"])

@app.get("/count")
def count():
    count = get_count(dynamodb)
    if not count:
        count = 0
    update_count(count+1, dynamodb)
    return {"Current Count": count}