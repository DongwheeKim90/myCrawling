import requests as req  # requests 라이브러리 호출
# Import the requests library for making HTTP requests

# GET 요청 방식 (쿼리 파라미터 사용)
# GET request method (using query parameters)
# Sends a GET request to the URL with a query parameter "name=hi"
# Sets a custom User-Agent header to "Avengers"
res_get = req.get("https://webhook.site/05b7b82b-41a0-450b-814d-0046b53bf389?name=hi",
                  headers={"User-Agent": "Avengers"})  # User-Agent 헤더 설정

print(res_get.text)  # 서버의 응답을 출력
# Prints the response received from the server

# POST 요청 방식 (데이터를 본문에 포함하여 전송)
# POST request method (sending data in the request body)
# 본문(body)에 데이터를 포함하여 요청 전송
# Sends a POST request to the URL, passing the data {"name": "Hi"} in the request body
res_post = req.post("https://webhook.site/05b7b82b-41a0-450b-814d-0046b53bf389",
                    data={"name": "Hi"})

# 서버의 응답을 출력
# Prints the response received from the server
print(res_post.text)
