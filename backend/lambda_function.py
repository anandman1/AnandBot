# Import required AWS SDK and JSON handling libraries
import boto3
import json

# Initialize AWS Bedrock client
# This creates a connection to AWS Bedrock service in the us-east-1 region
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

# Specify the AI model to use
# Using Cohere's Command model version 14 available through AWS Bedrock
modelId = 'cohere.command-text-v14'

def lambda_handler(event, context):
    # Log the incoming event for debugging purposes
    print('Event:', json.dumps(event))

    # Define CORS headers to allow cross-origin requests
    # These headers are necessary when calling the API from a web browser
    cors_headers = {
        'Access-Control-Allow-Origin': '*',  # Allow requests from any origin
        'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',  # Allow necessary AWS headers
        'Access-Control-Allow-Methods': 'OPTIONS,POST'  # Allow OPTIONS (preflight) and POST requests
    }

    # Handle OPTIONS request (preflight)
    # This is required for CORS - browsers send this before actual POST requests
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': ''
        }

    try:
        # Parse the incoming request body
        # API Gateway wraps the request in an 'event' object with a 'body' field
        # Direct Lambda invocation might not have the 'body' wrapper
        if 'body' in event:
            requestBody = json.loads(event['body'])
        else:
            requestBody = event

        # Validate that the request contains a prompt
        # This ensures we don't send empty requests to the model
        if 'prompt' not in requestBody:
            raise ValueError("Missing 'prompt' in request")

        prompt = requestBody['prompt']

        # Configure the request parameters for the AI model
        # These parameters control the model's response behavior
        body = {
            'prompt': prompt,             # The user's input text
            'max_tokens': 400,         # Maximum length of response
            'temperature': 0.75,       # Controls randomness (0=deterministic, 1=random)
            'p': 0.01,                # Nucleus sampling parameter
            'k': 0,                   # Top-k sampling parameter
            'stop_sequences': [],      # Sequences where model should stop generating
            'return_likelihoods': 'NONE'  # Don't return token probabilities
        }

        # Call the Bedrock API with our prompt and parameters
        # This sends the request to the AI model and gets the response
        bedrockResponse = bedrock.invoke_model(
            modelId=modelId,
            body=json.dumps(body),
            accept='*/*',
            contentType='application/json'
        )
        
        # Extract the generated text from the model's response
        # Navigate through the response structure to get the actual text
        response = json.loads(bedrockResponse['body'].read())['generations'][0]['text']
        
        # Return successful response with CORS headers
        # Include both the original prompt and the model's response
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps({
                'prompt': prompt,
                'response': response
            })
        }

    except Exception as e:
        # Log and return any errors that occur
        # This ensures errors are properly communicated to the client
        print('Error:', str(e))
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'error': str(e)})
        }
