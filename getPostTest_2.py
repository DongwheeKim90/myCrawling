# 이미지 업로드 : https://imgur.com/
# Image Upload to Imgur: https://imgur.com/
import requests as req  # requests 라이브러리 호출
# Import the requests library for making HTTP requests

# Imgur API 엔드포인트 (클라이언트 ID 포함)
# Imgur API endpoint with client ID
imgUrl = "https://api.imgur.com/3/upload?client_id=546c25a59c58ad7"

# 업로드할 이미지 파일을 바이너리 모드로 열기
# Open the image file in binary mode for upload
with open("D:/myCrawling/sampleImg.jpg", "rb") as f:
    img = f.read()  # 파일 내용을 읽어 변수 img에 저장
    # Read the file content and store it in the img variable

# 이미지 파일의 크기 출력
# Print the binary file size of the image
print(f"File binary size : {len(img)}")

# Imgur API에 이미지 업로드 요청 (POST 요청)
# Send a POST request to Imgur API to upload the image
res = req.post(imgUrl,
        files={  # 파일 데이터를 딕셔너리 형태로 전송
            "image": img,  # 이미지 파일 데이터
            "type": "file",  # 파일 타입 지정
            "name": "sampleImg.jpg"  # 파일 이름 지정
    })

# 서버 응답 상태 코드 출력 (200이면 성공)
# Print the response status code (200 means success)
print(res.status_code)

# 서버에서 받은 응답 데이터 출력
# Print the response text from the server
print(res.text)

# JSON 응답에서 업로드된 이미지 링크 추출
# Extract the uploaded image link from the JSON response
link = res.json()["data"]["link"]
print(link)

# 업로드된 이미지를 표시할 HTML 코드 생성
# Generate an HTML file to display the uploaded image
html = f'''
<html>
<head>
    <title> Uploaded my Image </title>
</head>
<body>
    <img src = "{link}">
</body>
</html>
'''

# HTML 파일을 생성하여 브라우저에서 업로드된 이미지 확인 가능
# Create an HTML file to display the uploaded image in a browser
with open("image.html", "w") as f:
    f.write(html)  # HTML 코드를 파일에 저장
    # Write the generated HTML code into the file