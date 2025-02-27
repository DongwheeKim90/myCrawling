# Library import > Using alias
import requests as req

# requests methods
# - Retrieve information: requests.get()
# - Create or perform an action: requests.post()
# - Update or overwrite: requests.put()
# - Delete: requests.delete()

# -- Retrieve information using GET > Can send values in headers as a dictionary
res = req.get("https://api.ipify.org/", headers={"name": "Lucas"})

# -- Check the request details sent to the server, such as method and headers
print(res.request.method)
print(res.request.headers)

# -- Check the status code after retrieving information using GET
print(res.status_code)

# -- Check the response content received from the URL
print(res.text)

# -- Check how long it took to receive the response from the URL
print(res.elapsed)