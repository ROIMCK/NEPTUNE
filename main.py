# Project Neptune Starter Code
# Assumes a dataset called neptune exists
# Assumes a table call rawmessages
# rawmessages schema - single column:  message:string
# Deploy as a Cloud Function using Python3.7 Runtime
# When deploying the cloud function - be sure to change enty point to the function name - pubsub_to_bigquery

import base64
from google.cloud import bigquery
table_id = "neptune.rawmessages"


def pubsub_to_bigquery(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print("Row To Insert: " + pubsub_message)
    client = bigquery.Client()
    table = client.get_table(table_id)
    row_to_insert = [(pubsub_message,)]     # NOTE - the trailing comma is required for this case - it expects a tuple
    errors = client.insert_rows(table, row_to_insert)
    if errors == []:
        print("Row Inserted: " + pubsub_message)
