from flask import Flask, render_template, request
import stories

app = Flask(__name__)

story_call = getattr(stories, 'story')

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/madlibs')
def madlibs_form():
    return render_template('madlibs_form.html')

@app.route('/story')
def create_story():
    place = request.args['get_place']
    noun = request.args['get_noun']
    verb = request.args['get_verb']
    adjective = request.args['get_adjective']
    plural_noun = request.args['get_plural_noun']
    answ = {'place': place, 'noun': noun, 'verb': verb, 'adjective': adjective, 'plural_noun': plural_noun}
    story_txt = story_call.generate(answ)
    return render_template('story.html', story_txt=story_txt)