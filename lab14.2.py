import requests

image = requests.get("https://cataas.com/cat")

if image.status_code == 200:
    with open("cat.jpg", "wb") as f:
        f.write(image.content)
    print("Фото завантажено успішно.")
else:
    print("Виникла помилка.")