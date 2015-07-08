# This is a html generator. 
#Stage 2 - IPND

# its input is a list, containing strings, dictionaries (that in turn also contain dictionaries and lists)

# how to format the input:
# On spot 0 and 1 of the list the title and the main heading get written respectively as strings,
# on the next spots the different sections, (in dictionary format)

# the dictionaries of the different sections go like this: tag: ... , element_class : ..., and the keys for the subsections

# the subsections in turn hold heading type, heading content, and a list of contents to appear in order of appearance

# EXAMPLE_CONTENT = ["Title of page", "Main heading" {dictionaries of sections}, {one after the other}]
# {section dictionaries} include {"tag" : "name", "element_class": "name", "class_heading":"heading of class", 
# "subsections+order of appearance":{dictionaries of contents}}

# {dictionries of contents} include {"heading: "type_heading", "heading content" : "heading for section", 
#"content" :[a list of contents], "img": [a list of image attributes in this order: "src", "alt", "title"],
# "link": [link attributes:"href", "title", "Text"]}

import json

def make_page(content_list): 
    """makes the whole html page"""
    code = make_head(content_list)
    content_list = content_list[2:]    
    while len(content_list) > 0:
        for element in content_list:
            code += make_tag(content_list[0])                   
            code += make_content(content_list[0])    
            content_list = content_list[1:]
            if element.get("tag"):
                code += """
    </""" + element.get("tag") + """>"""
    code += make_end()
    return code

def make_head(content_list):
    """ makes the head of the html"""
    title = content_list[0]
    main_heading = content_list[1]
    head = """<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title> """ + title + """</title>
    <link rel='stylesheet' href='../css/stage2/pt2_html_generate/style.css'>
    <link rel="shortcut icon" href="http://goo.gl/RT3tgF" type="image/x-icon"/> 
  </head>
  <body>
    <h1>""" + main_heading + """</h1>"""
    return head

def make_tag(section):
    """makes the container tags"""
    tag = ""
    if section.get("class_heading"):
        tag += """
    <h2>""" + section.get("class_heading") + """</h2>"""
    if section.get("tag"):
	    tag += """
    <""" + section.get("tag")
    if section.get("element_class"):
        tag += " class='" + section.get("element_class") +"'"
    if section.get("tag"):
        tag += ">"
    return tag

def make_content(section):
    """makes each of the contents of the page"""
    container = ""
    number_of_content = 1
    while section.get("contained"+str(number_of_content)):
    	key = "contained"+str(number_of_content)
        if section.get(key):
            container += """
      <div>"""
        if section.get(key).get("heading"):
            container +="""
        <""" + section.get(key).get("heading") + """>
          """ + section.get(key).get("h_content") + """
        </""" + section.get(key).get("heading") + ">"
        if section.get(key).get("link"):
            num_link = 0
            for element in section.get(key).get("link"):
                container += """
        <a href='"""+str(section.get(key).get("link")[num_link][0]) +"""' title='"""+str(section.get(key).get("link")[num_link][1]) +"""'>"""+ str(section.get(key).get("link")[num_link][2]) +"""</a>"""
                num_link += 1
        if section.get(key).get("content"):
            for element in section.get(key).get("content"):
                container += """
        <p>""" + element + """</p>"""
        if section.get(key).get("img"):
            container += """
        <img src='"""+section.get(key).get("img")[0] +"""' alt='"""+section.get(key).get("img")[1] +"""' title='"""+section.get(key).get("img")[2] +"""'>"""
        if section.get(key):
            container +=	"""
      </div>"""        
        number_of_content += 1
    return container

def make_end():
    """makes the end tags of the html"""
    return """
  </body>
</html> """


python_text = json.load(open('content.json'))
output = open('python.html', 'w')
output.write(make_page(python_text))


programming_text = json.load(open('programming.json'))
output = open('programming.html', 'w')
output.write(make_page(programming_text))

print "Your pages have been generated"
print ": )"