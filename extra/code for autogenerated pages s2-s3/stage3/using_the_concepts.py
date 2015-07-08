import concepts

#this makes the page - head, title and footer

stage3page = concepts.HtmlPage("This is my self generated page, for stage3 for the ipnd", 
								"my jump out boxes, using other people's code, but also mine",
								"THE BIG CLASS PAGE", "/../css/stage3/style.css", "http://goo.gl/RT3tgF",
								"Kalindi", "Stage 3", "June 2015")

#initializing objects

oop = concepts.Concept("OOP",
	"What is object oriented programming?<br> Thinking about objects, their attributes and \
	 behaviours is central to OOP. Classes that define an object are created, they define  \
	 sets of attributes and functions. Many instances of the same object can be easily created, \
	 avoiding repetition because they fit into a category that has the behaviours and characterisics \
	 defined by the class. In case one would like ot make more specific instances of an object, it \
	 can further be defined, inherit all from parent classses, plus have defined the new aspect. \
	 I didnt't like it because it was a media presence class, not a class about OOP.")

why_oop = concepts.Concept("why&nbsp;oop?", 
	"A problem that is to be solved through OOP is dealt with by defining the objects that \
	make it up. The interacting objects create a system, without the need for the system to be created \
	by a programmer step by step. OOP allows for much simpler code that can refer and use previously \
	defined code, (no need to solve the problem again). <br>Another way it prevents repetition, \
	is that when a class is defined, new instances can be easily created, without the need to define \
	each instance again. It allows for a fast creation of many instances of a certain object that can \
	all be accessed through the class predefined functions. Given that classes can have children classes, \
	the functions and attributes can be inherited, thus allowing for the creation of similar, yet more \
	specific objects.")

classes = concepts.Concept("class", 
	"A programmer defines a recipe for an object, with the attributes and behaviours that any \
	object of that class would have. A class is something that defines the structure: it defines \
	how an object should be structured, but doesn't actually fill in the content. A class is \
	like a form: it specifies what content should exist.")

instance = concepts.Concept("instance",
	"An instance is a specific copy of an object and has all the neccesary attributes. \
	It is the filled copy of the form with all the necessary information. \
	It specifies what the content actually is.")

class_object  = concepts.Concept("object", 
	"An object is defined with a class, it has attributes, variables and responds to the \
	class methods.")

method = concepts.Concept("method",
	"The functions of the class. A special kind of function that is defined in a class definition \
	and works with objects of the class.")

module = concepts.Concept("module", 
	"It is where classes with their methods and variables are defined, it has the code for the \
	creation of the different instances of the object and all the methods that apply to them. \
	It is a conceptually connected set of classes/objects, that can be affected by the methods \
	it contains (e.g. math module, or random module). It gets imported, and the code than used.",
	"module.function()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; runs function")

using_modules = concepts.Concept("using&nbsp;modules", 
	"A module is a system of variables, functions and class definitions that can interacts with \
	another system. To make a module one makes a file.py. It is good practice to use the module \
	in another file2.py")

inheritance = concepts.Concept("inheritance", 
	"The transfer of the characteristics of a class to other classes that is derived from it.")

library = concepts.Concept("library", 
	"Is a collection of modules. There is, for example, the standard python library")

class_variables = concepts.Concept("class&nbsp;variables",
	"A variable that is shared by all instances of a class. Class variables are defined \
	within a class but outside any of the class's methods.")

method_overriding = concepts.Concept("method&nbsp;overriding",
	"The assignment of more than one behavior to a particular function. It runs the one most \
	recently defined in code runtime.")

oop_abstraction = concepts.Concept("OOP&nbsp;abstraction",
	"It does a good job at making one think and realize what are the basic parameters of an object \
	or its behaviour. One can define these, and from them even define more specific ones that \
	inherit traits from its parent classes. Thus making one aware of the characteristics, \
	both of what was already coded, as well as giving a way to think about elements that are \
	planned to be prgrammed.<br>I really did not enjoy this stage.")

html_css_vs_oop = concepts.Concept("html/css&nbsp;vs&nbsp;oop",
	"The different tags in html are like classes, they have attributes and behaviours, css can \
	override some of those. There is inheritance, that works based on contained elements, and \
	each time we use a tag, we make a different element instance. I would say oop is interesting \
	because it allows for the person who codes to define all the parameters of behaviour, \
	in html some come given but some can be added with css.")

instance_varibles = concepts.Concept("instance&nbsp;varibles",
	"The variables defined while creating the instance and that generally get called with 'self'.")

examples = concepts.Concept("a&nbsp;few&nbsp;examples",
	"a few prewritten classes and their examples:<br>text.translate(table(?), '0123456789' \
	characters to remove)<br><br>os.listdir('url')<br>os.rename(old,new)<br><br>webbrowser.open()")



# the making of bibilography

list_of_links =["<a href='http://www.tutorialspoint.com/python/python_classes_objects.htm'>1</a>",
				"<a href='http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/'>2</a>",
				"<a href='http://www.tutorialspoint.com/python/python_classes_objects.htm'>3</a>",
				"""<a href="http://en.wikibooks.org/wiki/A_Beginner's_Python_Tutorial/Classes">4</a>""",
				"<a href='http://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/'>5</a>",
				"<a href='http://www.learnpython.org/en/Classes_and_Objects'>6</a>"]

bibliography= concepts.Bibliography(list_of_links)


#making content of the page

list_of_concepts = [why_oop, classes, instance, class_object, method, module, using_modules, 
					library, inheritance, class_variables, method_overriding, instance_varibles, examples, bibliography, 
					html_css_vs_oop, oop_abstraction, oop]

concept_html = ""
for concept in list_of_concepts:
	concept_html += concept.makeBox()

#making the whole page

text = stage3page.makeHead() + concept_html + stage3page.makeFooter() + stage3page.makeEnd()

#writing the html document

output = open('using_classes.html', 'w')
output.write(text)
