from flask import Flask
from flask import render_template
from flask import abort
from flask import request
from datetime import datetime

app = Flask(__name__)


# NOTE: IDs are used by the Disqus plug-in to distinguish betwixt pages.
# NOTE: When updating with a new blog post:
# 1. Create a new host method for it. Iterate the id.
# 2. Update the Blog link in frame.html to point to the most recent post.
# 3. Update the previously most recent Blog post to point to the new post as the new most recent one.
# These URLs are generated within Jinja2 using eg. href='{{request.url_root}}2015/10/31/this-website.html'.

# Note: Titles are assigned globally but may also be overwritten in the Jinja2 template using a {% posttitle %}
# wrapper.
# Note: The id parameter is used by the Disqus plugin to verify uniqueness.
post_list = [
    {
        'title': 'About this website',
        'route': '2015/10/31/this-website.html',
        'date': datetime(2015, 10, 31),
        'template': 'this-website.html'
    },
    {
        'title': 'An exercise in probability',
        'route': '2015/11/06/an-exercise-in-probability.html',
        'date': datetime(2015, 11, 6),
        'template': 'an-exercise-in-probability.html'
    },
    {
        'title': 'Openness versus quality',
        'route': '2015/12/12/openness-versus-quality.html',
        'date': datetime(2015, 12, 11),
        'template': 'openness-versus-quality.html'
    },
    {
        'title': 'IBM Watson, Cultural Insight, and WatsonGraph',
        'route': '2015/12/26/watson.html',
        'date': datetime(2015, 12, 26),
        'template': 'watson.html'
    },
    {
        'title': 'Measuring Wikipedia Signpost popularity',
        'route': '2016/01/17/signpost-views.html',
        'date': datetime(2016, 1, 17),
        'template': 'signpost-views.html'
    },
    {
        'title': 'The decision to launch the Space Shuttle Challenger',
        'route': '2016/02/07/space-shuttle-challenger.html',
        'date': datetime(2016, 2, 7),
        'template': 'space-shuttle-challenger.html'
    },
    {
        'title': 'Is Starbucks really always two blocks away?',
        'route': '2016/02/09/average-chain-distance.html',
        'date': datetime(2016, 2, 9),
        'template': 'average-chain-distance.html'
    },
    {
        'title': 'Exploring the IBM Watson Concept Insights service using watsongraph',
        'route': '2016/02/11/watsongraph-visualization.html',
        'date': datetime(2016, 2, 11),
        'template': 'watsongraph-visualization.html'
    },
    {
        'title': 'Analyzing WikiProjects',
        'route': '2016/02/15/wikiprojects.html',
        'date': datetime(2016, 2, 15),
        'template': 'wikiprojects.html'
    },
    {
        'title': 'The executive crisis at the Wikimedia Foundation',
        'route': '2016/02/20/wikimedia-foundation-turnover.html',
        'date': datetime(2016, 2, 20),
        'template': 'wikimedia-foundation-turnover.html'
    }
]

raws_list = [
    'challenger-compact-visualization.html',
    'challenger-extended-visualization.html',
    'gregorys-map-visualization.html',
    'dunkin-donuts-map-visualization.html',
    'starbucks-map-visualization.html',
    'manhattan-point-cloud-visualization.html',
    'average-chain-distance-visualization.html',
    'contributions-force-graph-visualization.html',
    'fortune-force-graph-visualization.html',
    'planets-force-graph-visualization.html'
    ]

post_paths = [post['route'] for post in post_list]


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path == '':
        return render_template('about.html', most_recent=request.url_root + post_list[len(post_list) - 1]['route'])
    if path in post_paths:
        index = post_paths.index(path)
        post = post_list[index]
        return render_template(post['template'],
                               id=index,
                               date="{0:02d}/{1:02d}/{2}".format(post['date'].month, post['date'].day,
                                                                 post['date'].year),
                               title=post['title'],
                               most_recent=request.url_root + post_list[len(post_list) - 1]['route']
                               )
    elif path in raws_list:
        return render_template(path)
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
