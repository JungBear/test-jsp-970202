from cgi import parse_multipart
from flask import Flask, request
import json
import start


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody

  
# 장학금 추가로 받아오기 
@app.route('/api/recommend', methods=['POST'])
def recommen2d():
    body = request.get_json()
    print(body)
    
    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job']
    print(job)
    print(type(job))
    location=params_df['loc']
    print(location)
    Benefits=params_df['Benefits']
    age=json.loads(params_df['sys_number'])['amount']
    yes_no = params_df['yes_no']

    Benefits1="\'%%" + Benefits + "%%\'"
    job1="\'%%" + job + "%%\'"
    yes_no1 = "\'%%" + yes_no + "%%\'"
    location1 = "\'%%" + location + "%%\'"
    df=start.db_select(Benefits1,job1,age,location1,yes_no1)
    print(df)

