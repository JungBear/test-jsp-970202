from cgi import parse_multipart
from flask import Flask, request
import json
import start


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!!'

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
def recommend():
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
    if len(df) >= 5:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            
                            "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": name[0],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%881.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[0]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                        
                            }
                        
                        ]
                    

                        },

                        {
                        "title": name[1],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%882.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[1]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": name[2],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%883.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[2]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                            }
                       
                        ]
                        },
                        {
                        "title": name[3],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%884.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[3]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": name[4],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%885.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[4]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        }
                    ]
                    }
                }
                ],
                "quickReplies": [
                {
                "messageText": "추가 장학금",
                "action": "message",
                "label": "장학금 더보기"
                }
            
                ]
            }
        }

        return responseBody
    else :
        qwest=False
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            
                            "text": "검색된 장학금은 총 : {}개 입니다".format(len(df))
                        }
                    },
                    
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": name[0],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%881.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[0]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                        
                            }
                        
                        ]
                        

                        },
                            
                        {
                        "title": name[1],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%882.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[1]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": name[2],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%883.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[2]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                            }
                       
                        ]
                        },
                        {
                        "title": name[3],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%884.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[3]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": name[4],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%885.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": URL[4]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        }
                    ]
                    }
                }
                ]
            }
        }

        return responseBody

@app.route('/api/recommen2d', methods=['POST'])
def recommend():
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
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                    "title": name[5],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%881.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":"webLink",
                        "label": "구경하기",
                        "webLinkUrl": URL[5]
                        },
                        {
                        "action": "share",
                         "label": "공유하기"
                        
                        }
                        
                    ]
                    

                    },

                    {
                    "title": name[6],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%882.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": URL[6]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": name[7],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%883.jpg?raw=true"
                    },
                    "buttons": [
                         {
                        "action": "webLink",
                        "label": "구경하기",
                        "webLinkUrl": URL[7]
                        },
                        {
                        "action": "share",
                        "label": "공유하기"
                        }
                       
                    ]
                    },
                    {
                    "title": name[8],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%884.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": URL[8]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": name[9],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%885.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": URL[9]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    }
                ]
                }
             }
            ],
            "quickReplies": [
            {
                "messageText": "추가 장학금1",
                "action": "message",
                "label": "장학금 더보기"
            }
            
            ]
        }
    }

    return responseBody
