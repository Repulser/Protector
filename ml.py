from typing import Tuple, Optional

from google.cloud import automl_v1beta1
from google.oauth2 import service_account

import utils

config = utils.load_config()
credentials = service_account.Credentials.from_service_account_file('automl_credentials.json')  # GCP Credentials
prediction_client = automl_v1beta1.PredictionServiceClient(credentials=credentials)  # Prediction client


def get_prediction(content: str, project_id: str, model_id: str):
    """
    Requests prediction from google AutoML.
    :param content: Content of message
    :param project_id: Project
    :param model_id:
    :return: PredictionResponse object from google
    """
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned


def predict(content: str) -> Optional[Tuple[str, float]]:
    """
    Prediction wrapper.
    :param content: Content of message
    :return:
    """
    prediction = get_prediction(content, config['project_id'], config['model_id'])
    if not prediction:
        return None
    return prediction.payload[0].display_name, prediction.payload[0].classification.score
