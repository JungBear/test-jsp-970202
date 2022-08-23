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
    name=df['name']
    URL=df['url']
    if len(df) > 0:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": "공고 내역입니다."
                            },
                            "items": [
                                {
                                    "title": name[0],
                                    "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                    "link": {
                                        "web": URL[0]
                                    }
                                },
                                {
                                    "title": name[1],
                                    "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                                    "link": {
                                        "web": URL[1]
                                    }
                                },
                                {
                                    "title": name[2],
                                    "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                                    "link": {
                                        "web": URL[2]
                                    }
                                }
                            ],
                            "buttons": [
                                {
                                    "label": "더보기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do#"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": "공고 내역입니다."
                            },
                            "items": [
                                {
                                    "title": '현재 모집중인 공고가 없습니다.',
                                },
                            ],
                            "buttons": [
                                {
                                    "label": "다른공고더보기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do#"
                                }
                            ]
                        }
                    }
                ]
            }
        }


    
    return responseBody