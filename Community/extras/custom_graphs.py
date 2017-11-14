from bokeh.core.properties import Instance, String 
from bokeh.embed import components
from bokeh.models import ColumnDataSource, LayoutDOM
from bokeh.plotting import figure, output_file

JS_CODE = """

import * as p from "core/properties"
import {LayoutDOM, LayoutDOMView} from "models/layouts/layout_dom"

OPTIONS =
	width:  '600px'
	height: '600px'
	style: 'dot'
	showPerspective: true
	showGrid: true
	keepAspectRatio: true
	verticalRatio: 1.0
	legendLabel: 'stuff'
	cameraPosition:
		horizontal: -0.35
		vertical: 0.22
		distance: 1.8


export class Surface3dView extends LayoutDOMView

	initialize: (options) ->
		super(options)

		url = "https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.min.js"

		script = document.createElement('script')
		script.src = url
		script.async = false
		script.onreadystatechange = script.onload = () => @_init()
		document.querySelector("head").appendChild(script)

	_init: () ->

		@_graph = new vis.Graph3d(@el, @get_data(), OPTIONS)


		@connect(@model.data_source.change, () =>
				@_graph.setData(@get_data())
		)


	get_data: () ->
		data = new vis.DataSet()
		source = @model.data_source
		for i in [0...source.get_length()]
			data.add({
				x:     source.get_column(@model.x)[i]
				y:     source.get_column(@model.y)[i]
				z:     source.get_column(@model.z)[i]
				style: source.get_column(@model.color)[i]
			})
		return data


export class Surface3d extends LayoutDOM

	default_view: Surface3dView


	type: "Surface3d"

	@define {
		x:           [ p.String           ]
		y:           [ p.String           ]
		z:           [ p.String           ]
		color:       [ p.String           ]
		data_source: [ p.Instance         ]
	}
"""


class Surface3d(LayoutDOM):
	__implementation__ = JS_CODE
	data_source = Instance(ColumnDataSource)
	x = String
	y = String
	z = String
	color = String

def average(values_list):
	if len(values_list) == 0: 
		return 0
	else:
		return sum(values_list)/len(values_list)

def build_surface(x, y, value):
	source = ColumnDataSource(data=dict(x=x, y=y, z=value, color=value))
	surface = Surface3d(x='x', y='y', z='z', color='color', data_source=source)
	script, div = components(surface)
	return script, div


def bar_graph(game_name, game_ratings):
	grade_9 = []
	grade_10 = []
	grade_11 = []
	grade_12 = []
	for ratings in game_ratings:
		if ratings[0] == 12:
			grade_12.append(ratings[1])
		elif ratings[0] == 11:
			grade_11.append(ratings[1])
		elif ratings[0] == 10: 
			grade_10.append(ratings[1])
		elif ratings[0] == 9:
			grade_9.append(ratings[1])
	averages_list = [average(grade_9), average(grade_10), average(grade_11), average(grade_12)]
	grade_rating = figure(tools='save', title=game_name, plot_width=300, plot_height=300)
	grade_rating.hbar(y=(9, 10, 11, 12), right=averages_list, height=.5)
	grade_rating.yaxis.axis_label = 'Grade'
	grade_rating.xaxis.axis_label = 'Average Rating'
	grade_rating.toolbar.logo = None
	grade_script, grade_div = components(grade_rating)
	return (grade_script, grade_div)

