from fastapi import FastAPI, Request
from openai import OpenAI
import json

api_key = ''


# Initialize the FastAPI app
app = FastAPI()
client = OpenAI(api_key=api_key)

# Replace 'your-api-key' with your actual OpenAI API key

# Replace 'your-assistant-id' with the ID of your existing assistant
assistant_id = 'asst_RX3HBaq2yKgmnsFspNGnUKFg'
thread = client.beta.threads.create()

@app.post("/process-text")
async def process_text(request: Request):
# Get the JSON data from the request
    data = await request.json()
    input_text = data.get("text")
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content = input_text
    )
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id
    )
    
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print(messages)
    else:
        print(run.status)
    
    # Call the OpenAI Assistants API using the existing assistant ID
    

    # Return the response in JSON format
    # return {"response": response.choices[0].message["content"]}

# Run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)