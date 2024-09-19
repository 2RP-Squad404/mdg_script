from google.cloud import pubsub_v1

project_id = 'big-maxim-430019-g7'
topic_id = 'mockdata-for-bq'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id,topic_id)

message = "new message to pubsub"

future = publisher.publish(topic_path, message.encode('utf-8'))
print(f'mensagem publicada: {future.result()}')

