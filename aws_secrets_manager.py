import boto3
from botocore.exceptions import ClientError
import json

class SecretsManager:
    def __init__(self, secret_name, region_name):
        self.secret_name = secret_name
        self.region_name = region_name

    def get_secret(self):
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=self.secret_name
            )
        except ClientError as e:
            raise e

        secret_string = get_secret_value_response['SecretString']
        return json.loads(secret_string)

    def get_secret_value(self, key):
        secrets = self.get_secret()
        return secrets.get(key, None)
