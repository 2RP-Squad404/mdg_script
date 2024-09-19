import json

from config import settings
from datagen import generate_buy
from google.cloud import pubsub_v1

project_id = settings.PROJECT_ID
topic_id = 'mockdata-for-bq'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# event_exemple = {"account":{"account_number":"1234567890123456","account_type":"Checking","bank":{"address":{"city":"New York","state":"NY","street":"123 Main Street","zip_code":"10001"},"branch":"Main Street","name":"Global Bank"},"currency":"USD"},"recipient":{"account_number":"6543210987654321","bank":{"address":{"city":"Los Angeles","state":"CA","street":"456 Broadway","zip_code":"90001"},"branch":"Downtown","name":"World Trust Bank"},"name":"John Doe"},"sender":{"account_number":"1111222233334444","bank":{"address":{"city":"Chicago","state":"IL","street":"789 Business Lane","zip_code":"60601"},"branch":"Corporate Plaza","name":"Enterprise Bank"},"name":"ABC Corp"},"transaction_details":{"amount":1500.75,"description":"Salary for September 2024","fees":{"amount":15,"currency":"USD"},"method":"Wire Transfer","reference_number":"REF987654321","status":"Completed","timestamp":"2024-09-17T10:30:00Z","type":"Credit"},"transaction_id":"TX123456789"}

event_message = json.dumps(generate_buy())

future = publisher.publish(topic_path, event_message.encode('utf-8'))
print(f'mensagem publicada: {future.result()}')
print(f'event: {event_message}')
