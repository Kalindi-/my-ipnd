from google.appengine.ext import ndb


#my two object
class Box(ndb.Model):
    """object made of user inputs for stage 4 """
    term = ndb.StringProperty()
    definition = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Card(ndb.Model):
    """object made of user inputs for stage 5"""
    term = ndb.StringProperty()
    definition = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Comment(ndb.Model):
    """object made of user inputs for stage 5"""
    comment = ndb.StringProperty()
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)