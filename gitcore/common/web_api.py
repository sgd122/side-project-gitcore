import requests
import json

def github_request(method_name, url, dict_data=None, is_urlencoded=True):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    root_url = "https://api.github.com"
    url = root_url + url
    method_name = method_name.upper()  # 메소드이름을 대문자로 바꾼다
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application / vnd.github.v3 + json'}
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')

    if method_name == 'GET':  # GET방식인 경우
        response = requests.get(url=url, params=dict_data, headers=headers)
    elif method_name == 'POST':  # POST방식인 경우
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application / vnd.github.v3 + json'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers={'Content-Type': 'application/json', 'Accept': 'application / vnd.github.v3 + json'})

    dict_meta = {'status_code' : response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                 'Content-Type': response.headers['Content-Type']}

    return {**dict_meta, **{'data': json.loads(response.text)}}
    # if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
    #     return {**dict_meta, **response.json()}
    # else:  # 문자열 형태인 경우
    #     return {**dict_meta, **{'text': response.text}}