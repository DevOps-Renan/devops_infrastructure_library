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
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzgxODcwNGZiLThmZjMtNGQyOC05YTA1LWY1NDJjOTFhYmU0Ni8iLCJpYXQiOjE2ODE0MTM3NzksIm5iZiI6MTY4MTQxMzc3OSwiZXhwIjoxNjgxNDE4MDQ5LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBdm5IY0ppV3FWUnowemNHT3ZQZ09TNmdQVFlIVE04Mnp5N2Q1bitleDlEWHB4T1BjenlKVU53RFo2ZjAzcW9Cd2hBdUpKU0xZQU9FcWE0alZxRFpsL2IwMG4zWUVUMTRJYWxlUCt6Tnh1YW89IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiU2FtcGFpbyIsImdpdmVuX25hbWUiOiJSZW5hbiIsImdyb3VwcyI6WyJlZGE4NTM4NC0wNmU0LTRlYjEtYTI1ZC0yOGNhYTYwNTA5YzEiLCI0NjlhZmZkZC1hZTQ4LTRiM2YtYTM4NS0yYmFjMWExYjQ5MzUiXSwiaXBhZGRyIjoiMTg5LjEwNi43OC4zNiIsIm5hbWUiOiJSZW5hbiBTYW1wYWlvIiwib2lkIjoiODllZTMyMWQtOTVhZS00ODdhLTlmZmQtYWUwNmU0MzRkMzY4IiwicHVpZCI6IjEwMDMyMDAxQTI5NTg3RTMiLCJyaCI6IjAuQVVVQS13U0hnZk9QS0UyYUJmVkN5UnEtUmtaSWYza0F1dGRQdWtQYXdmajJNQk5GQU1NLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IjJXak1hTVFnQmlkZTY0LWQ3eFY0Wk1PNjdBOXJjR2I2RkpmRk00VDJSVUEiLCJ0aWQiOiI4MTg3MDRmYi04ZmYzLTRkMjgtOWEwNS1mNTQyYzkxYWJlNDYiLCJ1bmlxdWVfbmFtZSI6InJlbmFuc2FtcGFpb0BhbGV4YW5kZXJjb25jZWljYW9ldmxvczR1Lm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6InJlbmFuc2FtcGFpb0BhbGV4YW5kZXJjb25jZWljYW9ldmxvczR1Lm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6ImJLQTFkQlpMTFVDb0lxQ2g4ZjlzQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjRhNWQ4ZjY1LTQxZGEtNGRlNC04OTY4LWUwMzViNjUzMzljZiIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTU3OTU3ODQ5NH0.hKXECi3uHKX5cS0GzUec9UYcflbHJoiaS4fLZ1rQXm0kmsKGpC9rqc5xnoxsunT6L2fm1gAIxetmS_pCj98fSn6cqHDM283lwrrTXq5o8-WM0EyyLwuxPY7SzhU5_jnHq-DTvZ4XPMyAdb09ygYS3aY-cYNhq4XNI5cnynF85GZjkWtlxtWV5xX_KJDvJhRVxUd93_kJJW8dayW8WSwWiqZiIaUqgJSz7z7nADl-8p0lj3N11pp3TyOlXXEz-DVYqf5pAcvqirKv0_OTh0IFLg3L7qCEHOsXQ3p3AZevyxQVic_8nwJ8YhYcQ8Sa2CI25cC5NpS53aGgVaYYHNwTBQ"
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

        message_content = ""

        if added or removed:
            changed = "false"
            with open("response.json", "w") as arquivo:
                arquivo.write(json.dumps(data_b))
                arquivo.write("\n")

        # Define o conteúdo da mensagem
        if added:
            message_content = f"Adicionado from A to B: {added}"
            print(f"Adicionado from A to B: {added}")

        if removed:
            message_content = f"Removido from A to B: {removed}"
            print(f"Adicionado from A to B: {removed}")
        
        if not removed and not added:
            message_content = "Nada modificado"
            print("Nada modificado")

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

