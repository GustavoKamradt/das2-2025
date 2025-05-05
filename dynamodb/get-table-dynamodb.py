import boto3

dynamodb = boto3.client("dynamodb", region_name="us-east-1")

try:
    resposta = dynamodb.get_item(
        TableName="cliente",
        Key={
            "cpf": {
                "S": "1234567891"
            }
        }
    )
    if "Item" in resposta:
        item = resposta["Item"]
        print(f"Item encontrado: {item}")
    else:
        print("Item não encontrado.")
except Exception as e:
    print(e)