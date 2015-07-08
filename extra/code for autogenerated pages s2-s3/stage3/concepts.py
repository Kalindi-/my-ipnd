import random


class Concept():
   """for stage 3 I'd like to practice building classess, and understand a bit what they are about"""

   RUBRIK_CONCEPTS = ["instance", "class", "method", "object", "module", "library"]

   def __init__(self, concept_name, description, example=None):
      self.concept_name = concept_name
      self.description = description
      self.example = example

   def showImportance(self):
      if self.concept_name in  Concept.RUBRIK_CONCEPTS:
         return "importance very"
      else:
         return random.choice(["importance middle", "importance not-very"])

   def makeBox(self):
      #having buttons inside <a> gives me errors in the validator. 
      #What would be your proposal to solve this? I looked around a bit, 
      #and most of the suggestions I found were to style the <a> to look like a button.
      # I am not entirely happy with this solution so i looked forwatd, and then stumbled upon this:
      #http://www.thesitewizard.com/wizards/css-menu-buttons.shtml (search for "how many buttons" and 
      #under this section there is a "button" saying "Next >> Go to Step 2"). How are they making 
      #this button. I looked into inspect element, as well as the source code. 
      #I wasn't able to find anything about it in the css. What are they doing, can i do this too. Help! : )
      code ="""        
      <a href='#openModal"""+self.concept_name+"""' class ='boxes'>
         <button type="button">"""+self.concept_name+"""</button>
      </a>
      <div id='openModal"""+self.concept_name+"""' class="modalDialog">
         <div>
            <p class='"""+self.showImportance()+"""'>!</p>
            <a href="using_classes" title="Close" class="close">X</a>
            <h2>"""+self.concept_name+"""</h2>
            <p>"""+self.description+"""</p>"""
      if self.example:
            code += """
         <marquee><p>"""+ self.example+"""</p></marquee>"""  
         #Validator threw errors. I see marquee is not accepted as a html element. 
         #It is however presented as an option in stage 4. It feels a bit lame to be 
         #presented easy fun options, that are than a bit of a problem to be implemented?
      code +="""
         </div>
      </div>"""
      return code


class Bibliography():
   """pages i found my stuff on"""
   def __init__(self, list_of_links):
      self.list_of_links = list_of_links

   def makeBox(self):
      code ="""        
      <a href='#openModallinks' class ='boxes'>
         <button type="button">Bibliography</button>
      </a>
      <div id='openModallinks' class="modalDialog">
         <div>
            <a href="using_classes" title="Close" class="close">X</a>
            <h2>Some links</h2>
            <p>|"""
      for link in self.list_of_links: 
         code += link + "|"
      code += """
         </div>
      </div>"""
      return code 


class HtmlPage():
   """making the pieces of the html to put them all  together"""
   def __init__(self, description, title_page, main_heading, css, favicon, name, stage, month):
      self.description = description
      self.title_page = title_page
      self.main_heading = main_heading
      self.css = css
      self.favicon = favicon
      self.name = name
      self.stage = stage
      self.month = month


   def makeHead(self):
      #why does it indicate the meta="description" as an error in the validator?
      code ="""<!DOCTYPE html>
<!--This is an auto-generated page - concept.py being the module, using_the_concepts.py
being the place where I define my instances. I put my comments and questions in those files.
The whole IPND project can be found here: https://github.com/Kalindi-/my-ipnd-page -->
<html>
   <head>
      <meta charset="UTF-8">
      <title>"""+self.title_page+"""</title>
      <meta description='"""+self.description+"""'>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href='"""+self.css+"""'>
      <link rel="shortcut icon" href='"""+ self.favicon+"""' type="image/x-icon"/> 
   </head>
   <body>
      <a href='../../' class='home'>Home</a>
      <header>
         <h1>"""+self.main_heading+"""</h1>
      </header>
      <div class="concepts">"""
      return code

   def makeFooter(self):
      code="""
      </div>
      <footer class="row">
         <p>"""+self.name+"""</p>
         <p>"""+self.stage+"""</p>
         <p>"""+self.month+"""</p>
      </footer>"""
      return code

   def makeEnd(self):
      code="""
   </body>
</html>"""
      return code




