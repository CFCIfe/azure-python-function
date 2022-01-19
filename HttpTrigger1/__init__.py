import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    users_json = []

    for FamilyContainer in doc:
        user_json = {
           "id": FamilyContainer['id'],
           "name": FamilyContainer['lastName']
        }
    users_json.append(user_json)





    return func.HttpResponse(
            json.dumps(users_json),
            status_code=200,
            mimetype="application/json"            
    )