# Installation
Python3 comes with requests, 
make sure to import

`import requests`

# GET Requests
Basic GET request

`response = requests.get('https://api.github.com/events')`

This also works for DELETE, HEAD, and OPTIONS requests

# POST requests
You can pass a dict for POST data

````python
data = {
    'key': 'value,
}

response = requests.post('https://httpbin.org/post', data=data)
````
This also works for PUT requests

# Request object
Once you get a response, there are some built-in methods and properties

````python
response.url
>>> https://httpbin.org/get?key=value

response.text
response.json()

````