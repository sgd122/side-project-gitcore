from rest_framework.response import Response
from rest_framework.views import APIView
from common.web_api import github_request


class UserInfomationView(APIView):
    def get(self, request, user_id):
        url = '/users/%s' % (user_id)
        data = github_request(method_name="GET", url=url)
        return Response(data)


class UserRepoView(APIView):
    def get(self, request, user_id):
        url = '/users/%s/repos' % (user_id)
        data = github_request(method_name="GET", url=url)
        return Response(data)
