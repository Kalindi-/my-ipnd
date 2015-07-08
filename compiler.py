# IPND!!!!!! 
# plenty notes, some playing around, and a little game
# tiny trainings in html, css, python, json, jinja and javascript

#####

#this compiler was written in stage 4, and made better in stage 5 


import os
import webapp2
import jinja2
import random
import time
import json
import database_objects

from google.appengine.ext import ndb

#initializing work environment: the file, and the jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
template_loader = jinja2.FileSystemLoader(template_dir)
template_env = jinja2.Environment(loader = template_loader, autoescape = True)

# uploading data for the game
game_data = json.load(open('json/game.json'))

# page making handler
class Handler(webapp2.RequestHandler):
    """contains the basic methods for rendering the templates into html pages"""
    def write(self, *arguments, **key_word_dictionary):    
        """makes a html page out of the inputs"""
        self.response.out.write(*arguments, **key_word_dictionary)

    def render_str(self, template, **parameters): 
    # why here paramenters, and in the other cases i call it key_word_dicitionary
        """makes a string out of the inputs"""
        t = template_env.get_template(template)
        return t.render(parameters)

    def render(self, template, **key_word_dictionary):
        """takes template to fill it in with the keywords"""
        self.write(self.render_str(template, **key_word_dictionary))


#page making!!
template_dict = json.load(open("json/template_dict.json"))

def get_page(page):
    "inputs the neccesary data into the page making handler"
    class StagePage(Handler):
        "makes my page up, using the templates I provide"
        def get(self):
            self.render(template_dict[page][1])
        def post(self):
            self.redirect(template_dict[page][2])
    return StagePage

def get_term_page(page, game_dict, title):
    "inputs the necessary data for the makes my term pages up"  
    class TermPage(Handler):  
        def get(self):
            self.render(template_dict[page][1], game_dict=pair_and_random(game_data[game_dict]), title = title)
    return TermPage

def get_input_page(page, render=None, redirect=None, error_render=None, database_object=None):
# the pages that are to be made with user input / datastore
    class Page(Handler):
        def get(self):
            """retrieve objects, and create page digestable content"""
            #retrieve all instances of object in date-order
            d_object = template_dict[page][database_object]
            d_object = getattr(database_objects, d_object)
            query = d_object.query().order(d_object.date)

            # create a dictionary of terms and definitions to pass them into the page template
            game_dict = {}
            for idea in query:
                term = idea.term
                definition = idea.definition

                game_dict[term] = definition

            self.render(template_dict[page][render], game_dict=pair_and_random(game_dict), title=" - round of inputs game")

        def post(self):
            """retrieve input data and create instances of object"""
            term = self.request.get('term')
            definition = self.request.get('definition')

            if term and definition and term.isspace() == False and definition.isspace() == False:
                d_object = template_dict[page][database_object]
                d_object = getattr(database_objects, d_object)
                pair = d_object(term=term, definition=definition)
                pair.put()
                little_delay()
                self.redirect(template_dict[page][redirect])
            else:
                self.render(template_dict[page][error_render], error=True, term=term, definition=definition)
    return Page

class HomePage(Handler):
    def get(self):
        """make homepage page up"""
        self.render(template_dict["homepage"][1])

    def post(self):
        """retrieve input data and create instances of object Comment"""

        comment = self.request.get('comment')
        email = self.request.get('email')

        if (comment and comment.isspace() == False) or (email and email.isspace() == False):
            pair = database_objects.Comment(email=email, comment=comment)
            pair.put()
            little_delay()
            self.render(template_dict["homepage"][1], thanks=True)
        else:
            self.render(template_dict["homepage"][1], error=True,  comment=comment, email=email)

#helper funtions
def pair_and_random(dictionary):
    """make sure the pairs are recognizable and randomizes their order - for display"""
    game_dict = dict(dictionary)

    order_nums = range(len(game_dict.keys())*2)
    card_nums = list(order_nums)
    random.shuffle(order_nums)
    
    for key,value in game_dict.items():
        game_dict[key] = [value, order_nums[0], order_nums[1], card_nums[0], card_nums[1]]
        order_nums = order_nums[2:]
        card_nums = card_nums[2:]

    return game_dict

def little_delay():
    """databases need a moment to update, if no delay, the redirection 
       does not show the most recent input"""
    time_to_update = .1
    time.sleep(time_to_update)


#creation of pages
app = webapp2.WSGIApplication([(template_dict["homepage"][0], HomePage),     

                               (template_dict["stage0notes1"][0], get_page("stage0notes1")),
                               (template_dict["stage0notes2"][0], get_page("stage0notes2")),                    
                               (template_dict["stage0notes3"][0], get_page("stage0notes3")),

                               (template_dict["stage1pt1"][0], get_page("stage1pt1")),
                               (template_dict["stage1pt2"][0], get_page("stage1pt2")),

                               (template_dict["stage2pt1"][0], get_page("stage2pt1")),
                               (template_dict["stage2pt2"][0], get_page("stage2pt2")),
                               (template_dict["stage2pt3"][0], get_page("stage2pt3")),

                               (template_dict["stage3"][0], get_page("stage3")),

                               (template_dict["stage4pt1"][0], get_page("stage4pt1")),                    
                               (template_dict["stage4pt2"][0], get_term_page("stage4pt2",2, " - Terms 1 game")),
                               (template_dict["stage4pt3"][0], get_term_page("stage4pt3",1, "- Terms 2 game")),
                               (template_dict["stage4pt4"][0], get_page("stage4pt4")),
                               (template_dict["stage4pt5"][0], get_input_page("stage4pt5",1,2,3,4)),  

                               (template_dict["stage5pt1"][0], get_page("stage5pt1")),                    
                               (template_dict["stage5pt2"][0], get_term_page("stage5pt2",2, " - Terms 1 game")),
                               (template_dict["stage5pt3"][0], get_term_page("stage5pt3",1, " - Terms 2 game")),
                               (template_dict["stage5pt4"][0], get_term_page("stage5pt4",0, " - game about javascript")),
                               (template_dict["stage5pt5"][0], get_page("stage5pt5")),
                               (template_dict["stage5pt6"][0], get_input_page("stage5pt6", 1,2,3,4))
                               ],
                              debug = True)

