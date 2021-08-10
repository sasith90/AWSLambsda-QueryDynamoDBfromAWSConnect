import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    print (event)
    center_name = event['Details']['Parameters']['icename']
    client = boto3.resource("dynamodb")
    table = client.Table("cent_info")
    all = table.query(
         KeyConditionExpression=Key('icename').eq(center_name)
         )
    item_all = all['Items']
    tp1 = item_all[0]["tp1"]
    tp2 = item_all[0]["tp2"]
    resposne = {"tp1": tp1,"tp2":tp2}
    print (resposne)
    return (resposne)
