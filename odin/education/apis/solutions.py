from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from odin.apis.mixins import ServiceExceptionHandlerMixin

from odin.education.models import Solution

from odin.education.apis.permissions import CourseAuthenticationMixin

from odin.education.services import create_gradable_solution

from odin.education.apis.serializers import SolutionSubmitSerializer

from odin.grading.services import start_grader_communication


class SolutionSubmitApi(
    ServiceExceptionHandlerMixin,
    CourseAuthenticationMixin,
    APIView
):

    def get(self, request, *args, **kwargs):
        solution = get_object_or_404(Solution, id=self.kwargs.get('solution_id'))
        data = {
            'solution_id': solution.id,
            'solution_status': solution.verbose_status,
            'code': solution.code,
            'test_result': solution.test_output
        }
        return Response(data)

    def post(self, request):
        serializer = SolutionSubmitSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        solution = create_gradable_solution(
            user=self.request.user,
            task=data['task'],
            code=data['code']
        )
        start_grader_communication(
            solution_id=solution.id,
            solution_model='education.Solution'
        )

        data = {
                'solution_id': solution.id,
                'solution_status': solution.verbose_status,
                'code': solution.code,
                'test_result': solution.test_output
            }

        return Response(data)
