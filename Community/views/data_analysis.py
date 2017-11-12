from Community.forms import CommunityGameRatingsForm, CommunityExtraRatingsForm
from Community.models import CommunityInst, CommunityGameRatings, CommunityGames, CommunityExtraRatings, Game
from Community.extras.math_models import host_score, game_likeability
from Community.extras.custom_graphs import build_surface, bar_graph
from UserProfile.models import Student
from bokeh.core.properties import Instance, String 
from bokeh.embed import components
from bokeh.models import ColumnDataSource, LayoutDOM, Range1d
from bokeh.plotting import figure, output_file, show
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.mail import send_mail

import time

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Senators").exists(), login_url='/accounts/login')
def communityinstviewresults(request):
	"""
	Displays a list of all communities. 

	**Context**
	''communityinst''
		All Community objects

	**Template:**
	:template:'data_analysis/survey_result_list.html'
	"""

	communities = CommunityInst.objects.all()
	return render(request, 'data_analysis/survey_result_list.html', {'communityinst_list': communities})


@login_required
@user_passes_test(lambda u: u.groups.filter(name="Senators").exists(), login_url='/accounts/login')
def survey_results(request, communityid):
	"""
	Builds data structures to display for a individual community 

	**Context**
	''community''
		Communityinst object
	
	''game_mean''
		Mean of all game ratings for all games in Community object 
	
	''game_ratings_dict'' 
		a list of all games formated {index, GameRatingObject} 

	''hs''
		Host score

	''extras_ratings''
		Contains all the extras ratings objects for this community (overall rating, etc)

	''overall_mean''
		The mean for the overall rating of a community. 
	

	**Template:**
	:template:'data_analysis/survey_specific_result.html'

	"""
	start = time.time()

	community = get_object_or_404(CommunityInst, pk=communityid)	
	game_rating_by_grade_level = dict()
	game_rating_dict = dict()
	game_rating_list = []
	index = 0 
	for games in CommunityGames.objects.filter(communityinst=community):
		for instances in CommunityGameRatings.objects.filter(games=games):
			game_rating_list.append(instances)
			game_rating_dict[index] = instances 
			try:
				game_rating_by_grade_level[instances.games.game.name].append(
						(
						Student.objects.filter(user=instances.user)[0].grade_level, 
						instances.game_rating
						)
					)
			except KeyError:
				game_rating_by_grade_level[instances.games.game.name] = [
					(
					Student.objects.filter(user=instances.user)[0].grade_level, 
					instances.game_rating
					)
				]
			index += 1 

	game_mean = round(sum(r.game_rating for r in list(game_rating_dict.values()))/ ( len(game_rating_dict) ), 2)  	
	

	extras_list = [r
	 for r in CommunityExtraRatings.objects.filter(community=community)]
	
	pacing_rating_text = [p.pacing_rating 
	 for p in CommunityExtraRatings.objects.filter(community=community)]	

	overall_values = [r.overall_rating for r in extras_list]
	overall_mean = round(sum(overall_values)/len(overall_values), 2)


	# PRIMITIVE ENCODER, TO BE REPLACED WITH SKLEARN AFTER MINICONDA EXPIERMENTATION
	pacing_rating_numeric = []
	for values in pacing_rating_text:
		if values == 'v': pacing_rating_numeric.append(0)
		elif values == 'g': pacing_rating_numeric.append(1)
		elif values == 'd': pacing_rating_numeric.append(2)
		elif values == 'b': pacing_rating_numeric.append(3)
		elif values == 'h': pacing_rating_numeric.append(4)

	hs = round(host_score(overall_values, pacing_rating_numeric), 2)

	plot_list = []
	for games, rating_lists in game_rating_by_grade_level.items():
		plot_list.append(bar_graph(games, rating_lists))


	return render(request, 'data_analysis/survey_specific_result.html', 
		{'community': community, 'game_mean': game_mean, 'game_ratings_dict': game_rating_dict, 
		'host_score': hs, 'extras_ratings': extras_list, 'overall_mean': overall_mean, 
		'test': game_rating_by_grade_level, 'plot_list': plot_list})


@login_required
@user_passes_test(lambda u: u.groups.filter(name="Senators").exists(), login_url='/accounts/login')
def overall_survey_results(request):
	"""
	Builds data structures to display for all communities  

	**Context**
	''div''
		div of 3D Bokeh/Vis.js graph
	
	''script''
		Script of 3D Bokeh/Vis.js graph

	**Template:**
	:template:'data_analysis/survey_overall_results.html'
	"""

	z = [] 
	x = [] 
	y = [] 

	for games in CommunityGameRatings.objects.all():
		z.append(games.game_rating)
	for games in CommunityGameRatings.objects.all():
		x.append(games.games.game.number_of_participants)
	for games in CommunityGameRatings.objects.all():
		y.append(games.games.game.estimated_length)
	value = z 
	script, div = build_surface(x, y, z)

	return render(request, 'data_analysis/survey_overall_results.html', {'div': div, 'script': script})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Senators").exists(), login_url='/accounts/login')
def equation_documentation(request):
	return render(request, 'data_analysis/equation_documentation.html')
