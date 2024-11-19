import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/397546002821/Ada_Fila'

sqs = boto3.client('sqs', region_name='us-east-1')

sqs.delete_queue(QueueUrl=queue_url)
print("Fila excluída com sucesso.")