import logging
import uuid
import time
import json
import azure.functions as func


def main(request: func.HttpRequest, translation: func.Out[str]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    start = time.time()
    

    req_body = request.get_json()
    subtitle = req_body.get("subtitle")

    rowKey = str(uuid.uuid4())

    data = {
        "Name": subtitle,
        "PartitionKey": "message",
        "RowKey": rowKey
    }

    #time.sleep(5) #Simultatin 5 seconds of cpu-intensive processing
    
    translation.set(json.dumps(data))
    end = time.time()
    processingTime = end - start

    return func.HttpResponse(
        f"Processing took {str(processingTime)} seconds. Translations is : {subtitle}",
        status_code=200
    )