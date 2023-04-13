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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzgxODcwNGZiLThmZjMtNGQyOC05YTA1LWY1NDJjOTFhYmU0Ni8iLCJpYXQiOjE2ODE0MDgyMjYsIm5iZiI6MTY4MTQwODIyNiwiZXhwIjoxNjgxNDEzODY2LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBdnY3RzFXWWdrTXBCTEJIV014OHlIVE5DYXZRYUlpSXJkSXhTV2xVbTZRTDVBdGh2TU8yOUowajVkaGowbFZSTlJUTTdaU2lDUndpOXBPeTZNK1JOUzQ2THVDemhGQjJCeFBNb0kvN2pBUHM9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiU2FtcGFpbyIsImdpdmVuX25hbWUiOiJSZW5hbiIsImdyb3VwcyI6WyJlZGE4NTM4NC0wNmU0LTRlYjEtYTI1ZC0yOGNhYTYwNTA5YzEiLCI0NjlhZmZkZC1hZTQ4LTRiM2YtYTM4NS0yYmFjMWExYjQ5MzUiXSwiaXBhZGRyIjoiMTg5LjEwNi43OC4zNiIsIm5hbWUiOiJSZW5hbiBTYW1wYWlvIiwib2lkIjoiODllZTMyMWQtOTVhZS00ODdhLTlmZmQtYWUwNmU0MzRkMzY4IiwicHVpZCI6IjEwMDMyMDAxQTI5NTg3RTMiLCJyaCI6IjAuQVVVQS13U0hnZk9QS0UyYUJmVkN5UnEtUmtaSWYza0F1dGRQdWtQYXdmajJNQk5GQU1NLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IjJXak1hTVFnQmlkZTY0LWQ3eFY0Wk1PNjdBOXJjR2I2RkpmRk00VDJSVUEiLCJ0aWQiOiI4MTg3MDRmYi04ZmYzLTRkMjgtOWEwNS1mNTQyYzkxYWJlNDYiLCJ1bmlxdWVfbmFtZSI6InJlbmFuc2FtcGFpb0BhbGV4YW5kZXJjb25jZWljYW9ldmxvczR1Lm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6InJlbmFuc2FtcGFpb0BhbGV4YW5kZXJjb25jZWljYW9ldmxvczR1Lm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6IlY0d2FaekRhR0UySm42NUx1TjhrQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjRhNWQ4ZjY1LTQxZGEtNGRlNC04OTY4LWUwMzViNjUzMzljZiIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTU3OTU3ODQ5NH0.OkCXuFAU9c6IVJDtZazLeuAoGMidCPe1UQ6AMs3NjTEdMtXUEHGCEYhfXoFyFq927z4SfFgQNZ7P4qfvF8WQmDtgJQ-IOR6_TMXDonyiYHjpizo_dTO8e67b2l8lZkt7mKvapv0pxUh3TFWpU7nRDRWsu2XlADvptTwxAy_DUawaknjmL4Ss_dhAOkj1mZNMHN3c3e2_7LpnTO4cvnsfsPrBNtLNeJK5Q4sC7bgnXnz_g0cFC_HCs57LtQfAB-Y83MfwahIX_CHHbLpnRpQ08Y_tY005QKK6ARHfLf4e81-9CufuPHLbm6NUm7MACdNqE2Oofx5_lPsgtUI-rb4bWg"
}

response = requests.get(url, headers=headers)

json2 = response.content

json_str2 = json2.decode("utf-8")

print(json_str2)

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
            with open("response.json", "a") as arquivo:
                arquivo.write(json.dumps(json_str2))
                arquivo.write("\n")

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