import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_bucket(bucket_name, region="us-east-1"):
    try:
        if region is None:
            s3_client = boto3.client('s3')
        else:
            s3_client = boto3.client('s3', region_name=region)
        response = s3_client.create_bucket(Bucket=bucket_name)
        return response
    except NoCredentialsError:
        print("Credenciais da AWS não encontradas.")
        raise
    except PartialCredentialsError:
        print("Credenciais da AWS incompletas.")
        raise

# Exemplo de uso
if __name__ == "__main__":
    bucket_name = "meu-novo-bucket"
    region = "us-east-1"
    try:
        response = create_bucket(bucket_name, region)
        print(f"Bucket {bucket_name} criado com sucesso. Resposta: {response}")
    except Exception as e:
        print(f"Erro ao criar o bucket: {e}")