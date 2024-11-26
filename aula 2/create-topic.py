import boto3


# Cria um cliente SNS

sns = boto3.client('sns', region_name='us-east-1')


# Cria o tópico SNS

response = sns.create_topic(

    Name='AdaTopicoBoto3',  # Nome do tópico sem caracteres especiais

    Attributes={

    'DisplayName': 'AdaTopicoBoto3'

}

)


# Obtém o ARN do tópico criado

topicoCriado = response['TopicArn']


# Cria uma assinatura para o tópico

assinatura = sns.subscribe(

    TopicArn=topicoCriado,

    Protocol='email',

    Endpoint='jltdsjrdevjr@hotmail.com',

)


sms = sns.subscribe(

    TopicArn=topicoCriado,

    Protocol='sms',

    Endpoint='+5521991036659',


)


mensagem = sns.publish(

    TopicArn=topicoCriado,

    Message='Esta é uma mensagem de teste enviada pelo Amazon SNS.',

    Subject='Teste de Mensagem SNS'

)


print("Tópico criado com sucesso. ARN do Tópico:", topicoCriado)

print("Assinatura criada com sucesso. ARN da Assinatura:", assinatura)

print("Assinatura criada com sucesso. ARN da Assinatura:", sms)

print("Mensagem enviada com sucesso. ID da Mensagem:", mensagem)
