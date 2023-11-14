# Note: The openai-python library support for Azure OpenAI is in preview.
import os, json
from openai import AzureOpenAI

client = AzureOpenAI(api_key=os.getenv("AZURE_OPENAI_KEY"),
api_version="2023-07-01-preview",
azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"))
model_name=os.getenv("MODEL_NAME")

def prettify_json(message_json):
    return json.dumps(message_json, ensure_ascii=False, indent=4)


content = "Find beachfront hotels in San Diego for less than $300 a month with free breakfast."

messages= [
    #{"role": "user", "content": "Find beachfront hotels in San Diego for less than $300 a month with free breakfast."}
    {"role": "user", "content": content}
]

functions= [
    {
        "name": "search_hotels",
        "description": "Retrieves hotels from the search index based on the parameters provided",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location of the hotel (i.e. Seattle, WA)"
                },
                "max_price": {
                    "type": "number",
                    "description": "The maximum price for the hotel"
                },
                "features": {
                    "type": "string",
                    "description": "A comma separated list of features (i.e. beachfront, free wifi, etc.)"
                }
            },
            "required": ["location"]
        }
    }
]

#response = client.chat.completions.create(model="gpt-35-turbo-0613",
response = client.chat.completions.create(model=model_name,
messages=messages,
functions=functions,
function_call="auto")

#print(response['choices'][0]['message'])
#print(prettify_json(response.choices[0].message.content))
message = response.choices[0].message
print(message)
content= response.choices[0].message.content
#decoded_content=content.encode('iso-2022-jp').decode('utf-8')
