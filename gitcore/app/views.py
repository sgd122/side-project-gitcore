from rest_framework.response import Response
from rest_framework.views import APIView
from common.web_api import github_request, github_user_info, github_repo_list, github_pr_create, github_pr_list, \
    github_pr_get, github_orgs_repo_list


class UserInformationView(APIView):
    """
    사용자의 Github 정보를 가져온다.
    """
    def get(self, request, user_id):
        data = github_user_info(user_id=user_id)
        return Response(data)


class UserReposView(APIView):
    """
    사용자의 Repository 목록을 가져온다.
    """
    def get(self, request, user_id):
        data = github_repo_list(user_id=user_id)
        return Response(data)


class OrgsReposView(APIView):
    """
    조직의 Repository 목록을 가져온다.
    """
    def get(self, request, org_id):
        data = github_orgs_repo_list(org_id=org_id)
        return Response(data)


class PullRequestView(APIView):
    """
    Pull Request 에 대한 처리
    """
    def get(self, request, user_id, repo):
        """
        해당 Repo 의 pull requests 전체를 조회한다.
        """
        data = github_pr_list(user_id=user_id, repo=repo)
        return Response(data)

    def post(self, request, user_id, repo):
        """
        해당 Repo 의 pull requests 를 생성한다.
        """
        data = github_pr_create(user_id=user_id, repo=repo, dict_data='{"head":"head","base":"base"}')
        return Response(data)


class GetPullRequestView(APIView):
    """
    특정 Pull Request 를 조회한다.
    """
    def get(self, request, user_id, repo, pull_number):
        """
        특정 Pull Request 를 조회한다.
        """
        data = github_pr_get(user_id=user_id, repo=repo, pull_number=pull_number)
        return Response(data)