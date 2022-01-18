import logging
import azure.functions as func


def main(req: func.HttpRequest, FamilyContainer: func.DocumentList) -> str:
    if not FamilyContainer:
        logging.warning("Family not found")
    else:
        logging.info("Found Family, Description=%s",
                     FamilyContainer[0]['description'])
    return 'OK'