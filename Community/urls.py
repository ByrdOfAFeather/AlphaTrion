from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$', views.CommunityInstView.as_view(), name='community-home'),
	url(r'^communitysurvey/(?P<communityid>\d+)/$', views.review_community_instance, name='community-review'),
	url(r'^communitysurveyresults/(?P<communityid>\d+)/$', views.survey_results, name='community-results-specific'),
	url(r'^communitysurveyresults/$', views.communityinstviewresults, name='community-results'),
	url(r'^communitysurveyoverallresults/$', views.overall_survey_results, name='overall-community-results'),
	url(r'^addcommunity/$', views.add_community, name='add-community'),
	url(r'^addgame/$', views.add_game, name='add-game'),
	url(r'^equationdocumentation/$', views.equation_documentation, name='equation-documentation'),
	url(r'^communitysongsuggestion/$', views.song_suggestion, name='song-suggestion'),
]
