import openai

# Skeleton Code for the model.
openai.api_key = 'your_api_key_here'

def generate_content(topic, max_length=100, model="text-davinci-003"):
    """
    Generates marketing content based on the provided topic using OpenAI's API.
    
    Parameters:
    - topic: The topic or prompt to generate content for.
    - max_length: The maximum length of the generated content.
    - model: The model to use for generating content.
    
    Returns:
    - A string containing the generated content.
    """
    try:
        # Generate text using the OpenAI API
        response = openai.Completion.create(
            engine=model,
            prompt=topic,
            max_tokens=max_length,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=1
        )
        content = response.choices[0].text.strip()
        return content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    topic = "The future of digital marketing"
    generated_content = generate_content(topic)
    print("Generated Content:\n", generated_content)
