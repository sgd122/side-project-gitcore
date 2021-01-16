import requests, json


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
