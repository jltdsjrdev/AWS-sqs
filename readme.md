# 📩 AWS SQS Project

## 📝 Descrição

Este projeto demonstra o uso do **Amazon Simple Queue Service (SQS)** para gerenciar filas de mensagens em um sistema distribuído. Inclui exemplos de como criar, enviar, receber e excluir mensagens de uma fila utilizando a biblioteca **Boto3**, o SDK da AWS para Python.

---

## 🚀 Recursos

- Criação de fila SQS (Standard ou FIFO).
- Envio de mensagens para a fila.
- Recebimento de mensagens da fila.
- Exclusão de mensagens após processamento.
- Configuração de permissões IAM.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **AWS SDK (Boto3)**
- **Amazon SQS**

---

## 📋 Pré-requisitos

Antes de iniciar, você precisará de:

1. **Conta na AWS**.
2. **AWS CLI instalado e configurado**.
3. **Python 3 e a biblioteca Boto3**:
  
   pip install boto3
Credenciais IAM com permissões para gerenciar SQS.
⚙️ Instalação
Clone este repositório:

git clone https://github.com/jltdsjrdev/AWS-sqs.git
cd AWS-sqs
Instale as dependências:


pip install -r requirements.txt
Configure suas credenciais AWS:


aws configure
📂 Estrutura do Projeto
plaintext

AWS-sqs/
├── main.py                 # Script principal com operações SQS
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivos ignorados no Git

<br>
▶️ Como Usar
Crie uma fila: No script main.py, utilize a função create_queue() para criar uma fila no SQS.
Envie uma mensagem: Chame a função send_message(queue_url, message_body).
Receba e processe mensagens: Use receive_message(queue_url) para buscar mensagens na fila.
Exclua mensagens: Após o processamento, remova as mensagens com delete_message(queue_url, receipt_handle).

---

💻 Exemplo de Uso
Veja abaixo um exemplo básico de como usar o projeto:

python

import boto3

sqs = boto3.client('sqs')

# Cria uma fila
response = sqs.create_queue(QueueName='MinhaFila')
queue_url = response['QueueUrl']

# Envia uma mensagem
sqs.send_message(QueueUrl=queue_url, MessageBody='Olá, mundo!')

# Recebe a mensagem
messages = sqs.receive_message(QueueUrl=queue_url)
print(messages['Messages'])

# Exclui a mensagem
receipt_handle = messages['Messages'][0]['ReceiptHandle']
sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle) 
<br>
<br>
📜 Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
<br>

🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
Faça um fork do repositório.
<br>
Crie uma branch para sua feature:

git checkout -b minha-feature
Commit suas alterações:

git commit -m "Minha nova feature"
Faça um push:

git push origin minha-feature
Abra um Pull Request.