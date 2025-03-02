import requests
import json

cookies = {
    'SESSION': 'NzNlMTk5NGYtNTA5OC00ZmNiLTliMmYtZWY5YTUxMGIwNzlj',
}
response = requests.get(
    'https://www.eduplus.net/api/course/teach/courses/web/joined_courses?type=3',
    cookies=cookies,
)
print(response.text)
data = json.loads(response.text)
print(data)
print(type(data))
for lesson in data['data']:
    print(lesson['name'],lesson['term'])

