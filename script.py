import tempfile
import requests
import json
import os

with open("response.json", "r") as arquivo:
    json1 = arquivo.read()

# Converte o objeto JSON em um dicionário Python
data_a = json.loads(json1)

# Acessa a chave "value" do dicionário e imprime seu valor
array_a = data_a['value']

url = "https://management.azure.com/subscriptions/0b84aeb3-3723-42d4-b77a-6d8b2bb3353a/resources?api-version=2021-04-01"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzgxODcwNGZiLThmZjMtNGQyOC05YTA1LWY1NDJjOTFhYmU0Ni8iLCJpYXQiOjE2ODE0MDU3MTAsIm5iZiI6MTY4MTQwNTcxMCwiZXhwIjoxNjgxNDExMzEyLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBTit5MUs0czZkOVhacVRWUmZpcCt4MlA4bzZ5akpBa3BrWDR2bm5RN1A5K0dwYnNpWC9TUTg5TC9WRFFnYzJBZm4zdzExbkVBN0drRmh4bHZKZVV3T1h6WEZmZzFKODBwSEJMVll1SEg4QjA9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiU2FtcGFpbyIsImdpdmVuX25hbWUiOiJSZW5hbiIsImdyb3VwcyI6WyJlZGE4NTM4NC0wNmU0LTRlYjEtYTI1ZC0yOGNhYTYwNTA5YzEiLCI0NjlhZmZkZC1hZTQ4LTRiM2YtYTM4NS0yYmFjMWExYjQ5MzUiXSwiaXBhZGRyIjoiMTg5LjEwNi43OC4zNiIsIm5hbWUiOiJSZW5hbiBTYW1wYWlvIiwib2lkIjoiODllZTMyMWQtOTVhZS00ODdhLTlmZmQtYWUwNmU0MzRkMzY4IiwicHVpZCI6IjEwMDMyMDAxQTI5NTg3RTMiLCJyaCI6IjAuQVVVQS13U0hnZk9QS0UyYUJmVkN5UnEtUmtaSWYza0F1dGRQdWtQYXdmajJNQk5GQU1NLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IjJXak1hTVFnQmlkZTY0LWQ3eFY0Wk1PNjdBOXJjR2I2RkpmRk00VDJSVUEiLCJ0aWQiOiI4MTg3MDRmYi04ZmYzLTRkMjgtOWEwNS1mNTQyYzkxYWJlNDYiLCJ1bmlxdWVfbmFtZSI6InJlbmFuc2FtcGFpb0BhbGV4YW5kZXJjb25jZWljYW9ldmxvczR1Lm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6InJlbmFuc2FtcGFpb0BhbGV4YW5kZXJjb25jZWljYW9ldmxvczR1Lm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6InpYaG0xbkpTUVVpRDhnN01MM1BOQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjRhNWQ4ZjY1LTQxZGEtNGRlNC04OTY4LWUwMzViNjUzMzljZiIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTU3OTU3ODQ5NH0.adfKl0O2V4sw_CFTSLIGxpSJQ7HQx6l9BJSPcNccNNKxX8lX2_GO_5yDHieqRh2AwqCmaTN6gAuXALgVc-zynojdpdlepvvEudUdL-tI86DveDfn0ovDpxfcYOxMDdVlOZeXS2njVw89BAnFaPP_ERGmrHc7ftX1l8-VMVpHRUuU4UI60DXnJVbCA5MOp1Ct7ZM8cSsHgQC2hB_di_ObwD3fW_KHt-LFy2kRHry7pobxFcJbqG0HQhIRvt7HD5FhX6jNEtnLaD4wA7xfBCiESL3LwzhLYWTycvdh9fmpbTwqp4sJ7Xd_57O-f7zNIlyJkkAOUXSTVErng92oWn23zQ"
}

response = requests.get(url, headers=headers)

json2 = response.content

# Converte o objeto JSON em um dicionário Python
data_b = json.loads(json2)

# Acessa a chave "value" do dicionário e imprime seu valor
array_b = data_b['value']

# Cria um arquivo temporário para o array A
with tempfile.TemporaryFile(mode='w+t') as file_a:
    file_a.writelines([f"{item}\n" for item in array_a])
    file_a.seek(0)

    # Cria um arquivo temporário para o array B
    with tempfile.TemporaryFile(mode='w+t') as file_b:
        file_b.writelines([f"{item}\n" for item in array_b])
        file_b.seek(0)

        # Lê o conteúdo dos arquivos temporários e converte em conjuntos
        set_a = set(file_a.readlines())
        set_b = set(file_b.readlines())

        # Calcula a diferença entre os conjuntos
        added = set_b - set_a
        removed = set_a - set_b

        webhook_url = "https://discord.com/api/webhooks/1004817962953347073/OOQNuBYEtv_C-SEfqdoIqzpPnwTGByLh7ZXEAPwNw2n1LR2vxdMABTQ-DnB3tav2Oh6e"

        # Se houve mudanças, faz o commit

        changed = "false"

        if added or removed:
            changed = "false"
            print(f"::set-output name=changed::{changed}")
            print(f"::set-output name=json2::{json2}")

        # Define o conteúdo da mensagem
        if added:
            message_content = f"Adicionado from A to B: {added}"
            print(f"Adicionado from A to B: {added}")
        elif removed:
            message_content = f"Removido from A to B: {removed}"
            print(f"Adicionado from A to B: {removed}")
        else:
            message_content = "Não ocorreu mudanças"

        # Define o payload da mensagem
        payload = {
            "content": message_content
        }

        # Envia a mensagem para o webhook
        response = requests.post(webhook_url, json=payload)

        # Verifica se a mensagem foi enviada com sucesso
        if response.status_code == 204:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem: {response.text}")