import base64
from datetime import datetime

import requests, json
from django.utils.dateformat import DateFormat


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
                                     headers={'Content-Type': 'application/x-www-form-urlencoded',
                                              'Accept'      : 'application / vnd.github.v3 + json'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers=headers)

    dict_meta = {'status_code' : response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                 'Content-Type': response.headers['Content-Type']}

    return {**dict_meta, **{'data': json.loads(response.text)}}


def github_user_info(user_id: str):
    """
    사용자의 Github 정보를 가져온다.
    """
    url = '/users/%s' % (user_id)
    data = github_request(method_name="GET", url=url)
    return data


def github_user_events(user_id: str):
    """
    사용자의 Github event 정보를 가져온다.
    """
    url = '/users/%s/events' % (user_id)
    data = github_request(method_name="GET", url=url)
    return data


def github_repo_list(user_id: str):
    """
    사용자의 Repository 목록을 가져온다.
    """
    url = '/users/%s/repos' % (user_id)
    data = github_request(method_name="GET", url=url)
    return data


def github_orgs_repo_list(org_id: str):
    """
    조직의 Repository 목록을 가져온다.
    """
    url = '/orgs/%s/repos' % (org_id)
    data = github_request(method_name="GET", url=url)
    return data


def github_pr_list(user_id: str, repo: str):
    """
    해당 Repo 의 pull requests 를 조회한다.
    """
    url = '/repos/%s/%s/pulls' % (user_id, repo)
    data = github_request(method_name="GET", url=url)
    return data


def github_pr_create(user_id: str, repo: str, dict_data):
    """
    해당 Repo 의 pull requests 를 생성한다.
    """
    url = '/repos/%s/%s/pulls' % (user_id, repo)
    data = github_request(method_name="POST", url=url, dict_data=dict_data)
    return data


def github_pr_get(user_id: str, repo: str, pull_number: str):
    """
    해당 Repo 의 pull requests 를 조회한다.
    """
    url = '/repos/%s/%s/pulls/%s' % (user_id, repo, pull_number)
    data = github_request(method_name="GET", url=url)
    return data


def github_push_to_github(filename, repo, branch, token):
    """
    github commit을 만든다.
    """
    # TODO: download_url을 통해서 파일을 가져와서 commit을 하는 방향??
    # TODO: github accesskey를 발급받아야 하는지 여부 파악??
    url="https://api.github.com/repos/"+repo+"/contents/"+filename
    base64content=base64.b64encode(open(filename, "rb").read())

    data = requests.get(url+'?ref='+branch, headers = {"Authorization": "token "+token}).json()
    sha = data['sha']

    if base64content.decode('utf-8')+"\n" != data['content']:
        message = json.dumps({"message":"update",
                            "branch": branch,
                            "content": base64content.decode("utf-8") ,
                            "sha": sha
                            })

        resp=requests.put(url, data = message, headers = {"Content-Type": "application/json", "Authorization": "token "+token})

        print(resp)
    else:
        print("nothing to update")


def github_today_commit(user_id: str):
    """
    사용자의 오늘 Github Event 목록을 확인합니다.
    """
    repo_list = github_user_events(user_id=user_id)
    today = DateFormat(datetime.now()).format('Ymd')
    type_list = ["WatchEvent", "IssuesEvent"]
    data = []
    for repo in repo_list.get("data"):
        v_type = repo.get("type")
        v_created_at = DateFormat(datetime.strptime(repo.get("created_at"), "%Y-%m-%dT%H:%M:%SZ").date()).format('Ymd')
        if v_type not in type_list:
            if v_created_at == today:
                data.append(repo)

    dict_meta = {'status_code' : repo_list.get("status_code"), 'ok': repo_list.get("ok"), 'encoding': repo_list.get("encoding"),
                 'Content-Type': repo_list.get('Content-Type')}

    return {**dict_meta, **{'data': data}}