import boto3

dynamodb = boto3.client("dynamodb", region_name="us-east-1")

items = [
    {
        'cpf': {'S': "1234567891"},
        'nome': {'S': "Jose paulo"},
        'clienteativo': {'BOOL': True},
    },
    {
        'cpf': {'S': "4213342415"},
        'nome': {'S': "Douglas sola"},
        'clienteativo': {'BOOL': True},
    },
    {
        'cpf': {'S': "1242352346"},
        'nome': {'S': "Gustavo vieira"},
        'clienteativo': {'BOOL': True},
    },
    {
        'cpf': {'S': "1238323434"},
        'nome': {'S': "Armando pinto"},
        'clienteativo': {'BOOL': True},
    }
]

for item in items:
    try:
        dynamodb.put_item(
            TableName="cliente",
            Item=item
        )
        print(f"Item {item['cpf']['S']} inserido com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir item {item['cpf']['S']}: {e}")