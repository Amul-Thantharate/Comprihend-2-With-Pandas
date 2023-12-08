import boto3
import json

client = boto3.client('comprehendmedical')

def lambda_handler(event, context):
    
    data = event["body"]
    data = json.loads(data)
    
    option = data["choice"]
    text = data["body"]

    if option == 'Detect Entities':
        result = client.detect_entities_v2(Text=text)
        entities = result['Entities']
        return entities

    elif option == 'RXNorm':
        result = client.infer_rx_norm(Text=text)
        entities = result['Entities']
        return entities

    elif option == 'ICD-10-CM':
        result = client.infer_icd10_cm(Text=text)
        entities = result['Entities']
        return entities

    elif option == 'SNOMED CT':
        result = client.infer_snomedct(Text=text)
        entities = result['Entities']
        return entities
        
    elif option == 'Detect PHI':
        result = client.detect_phi(Text=text)
        entities = result['Entities']
        return entities