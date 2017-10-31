from django.conf.urls import url

from .views import (
    UserCompetitionsView,
    CreateCompetitionView,
    EditCompetitionView,
    CreateCompetitionMaterialFromExistingView,
    CreateNewCompetitionMaterialView,
    EditCompetitionMaterialView,
    CompetitionDetailView,
    CreateNewCompetitionTaskView,
    CreateCompetitionTaskFromExistingView,
    EditCompetitionTaskView,
    ParticipantSolutionsView,
    AllParticipantsSolutionsView,
    CompetitionSignUpView,
    CompetitionSetPasswordView,
    CompetitionLoginView,
    ParticipantSolutionDetailView,
)
from .apis import (
    CreateGradableSolutionApiView,
    CreateNonGradableSolutionApiView,
    SolutionDetailApiView
)

competition_registration_urlpatterns = [
    url(
        regex='(?P<competition_slug>[-\w]+)/signup/$',
        view=CompetitionSignUpView.as_view(),
        name='signup'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/set-password/(?P<registration_token>[-\w]+)/$',
        view=CompetitionSetPasswordView.as_view(),
        name='set-password'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/login/(?P<registration_token>[-\w]+)/$',
        view=CompetitionLoginView.as_view(),
        name='login'
    )
]

urlpatterns = [
    url(
        regex='^user-competitions/$',
        view=UserCompetitionsView.as_view(),
        name='user-competitions',
    ),
    url(
        regex='create-competition/$',
        view=CreateCompetitionView.as_view(),
        name='create-competition'
    ),
    url(
        regex='^(?P<competition_slug>[-\w]+)/$',
        view=CompetitionDetailView.as_view(),
        name='competition-detail'
    ),
    url(
        regex='^edit-competition/(?P<competition_slug>[-\w]+)/$',
        view=EditCompetitionView.as_view(),
        name='edit-competition'
    ),
    url(
        regex='^(?P<competition_slug>[-\w]+)/create-material/from-existing/$',
        view=CreateCompetitionMaterialFromExistingView.as_view(),
        name='create-competition-material-from-existing'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/create-material/new/$',
        view=CreateNewCompetitionMaterialView.as_view(),
        name='create-new-competition-material'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/edit-material/(?P<material_id>[0-9]+)/$',
        view=EditCompetitionMaterialView.as_view(),
        name='edit-competition-material'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/create-task/new/$',
        view=CreateNewCompetitionTaskView.as_view(),
        name='create-new-competition-task'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/create-task/from-existing/$',
        view=CreateCompetitionTaskFromExistingView.as_view(),
        name='create-competition-task-from-existing'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/edit-task/(?P<task_id>[0-9]+)/$',
        view=EditCompetitionTaskView.as_view(),
        name='edit-competition-task'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/tasks/(?P<task_id>[0-9]+)/solutions/submit-gradable/$',
        view=CreateGradableSolutionApiView.as_view(),
        name='submit-gradable-solution'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/tasks/(?P<task_id>[0-9]+)/solutions/submit-non-gradable/$',
        view=CreateNonGradableSolutionApiView.as_view(),
        name='submit-non-gradable-solution'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/tasks/(?P<task_id>[0-9]+)/personal-solutions/$',
        view=ParticipantSolutionsView.as_view(),
        name='participant-task-solutions'
    ),
    url(
        regex='(?P<competition_slug>[-\w]+)/tasks/(?P<task_id>[0-9]+)/all-solutions/$',
        view=AllParticipantsSolutionsView.as_view(),
        name='all-participants-solutions'
    ),
    url(
        regex='^solutions/(?P<solution_id>[0-9]+)/$',
        view=SolutionDetailApiView.as_view(),
        name='participant-solution-detail-api'
    ),
    url(
        regex='^(?P<competition_slug>[-\w]+)/tasks/(?P<task_id>[0-9]+)/solutions/(?P<solution_id>[0-9]+)/$',
        view=ParticipantSolutionDetailView.as_view(),
        name='participant-solution-detail'
    ),
] + competition_registration_urlpatterns
