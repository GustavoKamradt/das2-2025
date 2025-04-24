import boto3

dynamodb = boto3.client("dynamodb", region_name="us-east-1")

try:
    dynamodb.create_table(
        TableName="cliente",
        KeySchema=[
            {
                "AttributeName": "cpf",
                "KeyType": "HASH",  # chave de partição
            },
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "cpf",
                "AttributeType": "S",  # tipo String
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
    )
except Exception as e:
    print(e)