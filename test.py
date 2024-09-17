import requests

resp = requests.post("http://localhost:5000/predict", files = {'file':open('sample_image.png', 'rb')})

print(resp.text)