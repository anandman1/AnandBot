```markdown
# Bedrock Chat Interface

A simple web interface that connects to AWS Bedrock's Cohere Command model through API Gateway and Lambda, enabling real-time AI chat interactions.

## Architecture

```ascii
+-------------+     +--------------+     +------------------+     +------------------+
|   Frontend  | --> | API Gateway  | --> | Lambda Function | --> | Amazon Bedrock   |
| (HTML/JS)   |     | (REST API)   |     | (Python)        |     | (Cohere Command) |
+-------------+     +--------------+     +------------------+     +------------------+
```

## Components

### Frontend
- Single HTML file with embedded JavaScript and CSS
- Simple, responsive chat interface
- Handles API interactions and response display

### Backend
- **API Gateway**: REST API endpoint
- **Lambda Function**: Python-based serverless function
- **Bedrock**: Using Cohere Command v14 model

## Setup Instructions

### AWS Resources Required
1. API Gateway
2. Lambda Function
3. Bedrock access
4. IAM Role with appropriate permissions

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (ES6+)
- Backend:
  - Python 3.x
  - boto3 SDK

## Cost Considerations

- API Gateway requests
- Lambda invocations
- Bedrock model usage
- CloudWatch logs storage

## Cleanup Instructions

To avoid incurring future charges, delete these resources when not in use:

1. Delete API Gateway API
2. Delete Lambda Function
3. Remove CloudWatch log groups
4. Revoke Bedrock access if no longer needed

## Author [Anand Verma]

## Acknowledgments

- AWS Documentation: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
- Felix Yu: YouTube video on the backend development: https://www.youtube.com/watch?v=aMAmD-1SFYQ
- Amber Israelsen (@TinyTechnicalTutorials)'s YouTube video on frontend app development & deployment: https://www.youtube.com/watch?v=7m_q1ldzw0U&t=1327s
```
