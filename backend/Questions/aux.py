##from fastapi import HTTPException
##from openai import AsyncOpenAI
""""
async def get_chatgpt_response(question: str) -> str:
    client = AsyncOpenAI(
        # This is the default and can be omitted
    )
    model_engine = "gpt-3.5-turbo"
    try:
        # Call the OpenAI API to generate a response
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model_engine,
        )
        # Extract and return the generated text from the API response
        return chat_completion.choices[0].text.strip()
    except Exception as e:
        # Handle any other errors raised by the OpenAI API
        raise HTTPException(status_code=500, detail=str(e)) from e
"""