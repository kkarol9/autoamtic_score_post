import openai

openai.api_key = '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'
response = openai.Image.create(
    prompt='6-1 6-2',
    n=1,
    size="512x512"
    )
img_url = response.data[0].url

print(img_url)