from cgi import parse_multipart
from flask import Flask, request
import json
import start


app = Flask(__name__)

@app.route('/')
def hello_world():
    start.db_create()
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



    

# 카카오톡 장학금 받아오기
@app.route('/api/recommend', methods=['POST'])
def recommend():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job']
    print(job)
    print(type(job))

    location=params_df['location']
    print(location)

    advantage=params_df['advantage']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number'])['amount']
    print(age)

    special = params_df['special']
    print(special)
    advantage1="\'%%" + advantage + "%%\'"
    job1="\'%%" + job + "%%\'"
    special1 = "\'%%" + special + "%%\'"
    location1 = "\'%%" + location + "%%\'"
    list1=start.db_select(advantage1,job1,age,location1,special1)
    len1=len(list1)
    print(len1)
    print(list1)
    list2=list1[0]
    print(list2)
    print(type(list2))
    
    if len1 >= 5:
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
                        "title": list1[0][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%881.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-58:-2]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                        
                            }
                        
                        ]
                    

                        },

                        {
                        "title": list1[1][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%882.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[1][-58:-2]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": list1[2][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%883.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[2][-58:-2]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                            }
                       
                        ]
                        },
                        {
                        "title": list1[3][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%884.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[3][-58:-2]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": list1[4][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%885.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[4][-58:-2]
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
                            
                            "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": list1[0][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%881.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-58:-2]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                        
                            }
                        
                        ]
                        

                        },
                            
                        {
                        "title": list1[1][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%882.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[1][-58:-2]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": list1[2][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%883.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[2][-58:-2]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                            }
                       
                        ]
                        },
                        {
                        "title": list1[3][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%884.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[3][-58:-2]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": list1[4][2:-62],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%885.jpg?raw=true"
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[4][-58:-2]
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
        
        
        

    
        

  
# 장학금 추가로 받아오기 
@app.route('/api/recommen2d', methods=['POST'])
def recommen2d():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job1']
    print(job)
    print(type(job))

    location=params_df['location1']
    print(location)

    advantage=params_df['advantage1']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number1'])['amount']
    print(age)

    special=params_df['special1']
    [print(special)]

    
    advantage1="\'%%" + advantage + "%%\'"
    job1="\'%%" + job + "%%\'"
    special1 = "\'%%" + special + "%%\'"
    location1 = "\'%%" + location + "%%\'"

    list1=start.db_select(advantage1,job1,age,location1,special1)
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                    "title": list1[5][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%881.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":"webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[5][-58:-2]
                        },
                        {
                        "action": "share",
                         "label": "공유하기"
                        
                        }
                        
                    ]
                    

                    },

                    {
                    "title": list1[6][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%882.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[6][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": list1[7][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%883.jpg?raw=true"
                    },
                    "buttons": [
                         {
                        "action": "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[7][-58:-2]
                        },
                        {
                        "action": "share",
                        "label": "공유하기"
                        }
                       
                    ]
                    },
                    {
                    "title": list1[8][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%884.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[8][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": list1[9][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/flower75982/blob/main/image/%EC%9E%A5%ED%95%99%EA%B8%885.jpg?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[9][-58:-2]
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
