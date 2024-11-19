import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/397546002821/Ada_Fila'

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Aluno Jorge entregou o projeto'
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])