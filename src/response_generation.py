```python
import openai
from error_handling import handle_error

def generate_response(prompt, model):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        handle_error(e)

def emulate_creator_style(user_data, model):
    try:
        prompt = f"{user_data['creator_name']}: {user_data['last_message']}"
        response = generate_response(prompt, model)
        return response
    except Exception as e:
        handle_error(e)
```