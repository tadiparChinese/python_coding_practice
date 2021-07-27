import requests
import json
URL = "http://127.0.0.0:8000/stucreate"
data = {
    'name':'Django',
    'roll' : 101,
    'City': 'Pune'
}
json_data = json.dumps(data) #serialize the data
r = requests.post(url=URL, data = json_data) #sending post request, url, data
data = r.json() #converting it into json format
print(data)


def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream) #changing data into python data
        serializer = StudentSerializer(data=pythondata) #changing python data into complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'} #checking response
            json_data = JSONRenderer().render(res)
            return HTTPResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')