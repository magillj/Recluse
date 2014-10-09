__author__ = 'Jake Magill'

import cmd
import urllib2
import re

class RecluseConsole(cmd.Cmd):
    """Recluse UI Console"""

    def do_configure(self, filename):
        """Set crawling configuration to a file"""
        print "Not supported at this time"

    def help_configure(self):
        print help_print("configure [filename]", "Set crawling configuration to file at filename")

    def do_run(self, url):
        """Run Recluse on specified URL"""
        tags = extract_tags(get_HTML_data(url))
        for tag in tags:
            print tag

    def help_run(self):
        print help_print("run [url]", "Run Recluse on url")

    def do_exit(self, line):
        """Exit the program"""
        return True

class DOMElement():
    """Data structure to represent DOM elements"""
    def __init__(self, tag, id, classes, innerHTML):
        self.tag = tag
        self.id = id
        self.classes = classes
        self.innerHTML = innerHTML

    def set_children(self, children):
        """Set the children of this DOMElement"""
        self.children = children

    def __str__(self):
        """Prints in regular HTML tag format, without closing tag.
           Throws exception if no valid tag is present"""
        id_text = ""
        if self.id is not None:
            id_text = " id=\"" + self.id + "\""

        class_text = ""
        if self.classes is not None:
            class_text = " class=\"" + self.classes + "\""

        if self.tag is None:
            raise Exception("No tag for element")

        return "<" + self.tag + \
               (self.id if self.id is not None else "") + \
               (self.classes if self.classes is not None else "") + ">"

def help_print(command_syntax, help_text):
    """Prints command help consistently for the console, with the help text at column 30"""
    whitespace_append = 26 - len(command_syntax)
    return command_syntax.rjust(4 + len(command_syntax), ' ') + \
           help_text.rjust(whitespace_append + len(help_text), '.')

def configure(filename):
    """Set crawler configuration to file"""


def construct_DOM_tree(file_data):
    """Returns a DOMElement representing the HTML in file_data"""


def extract_tags(html_data):
    """Helper function that returns a list of DOMElements from the tag info"""
    tags = []
    remainder = ""

    # Find each tag on this level of the DOM
    while html_data is not None and html_data.find("<") != -1:
        # Gather tag information
        tag_start = html_data.find("<")
        tag_close = html_data.find(">")
        tag_info = html_data[tag_start + 1:tag_close]
        tag_type = getTagType(tag_info)
        tag_id = getAttribute(tag_info, "id")
        tag_classes = getAttribute(tag_info, "class")
        # Check if its a closing tag
        if tag_info[0] == "/":
            html_data = html_data[tag_close + 1:]
            break
        # Check if its a self closing tag
        if tag_info[len(tag_info) - 1] == "/":
            tags.append(DOMElement(tag_type, tag_id, tag_classes, ""))
            html_data = html_data[tag_close + 1:]
            continue

        extract_output = extract_tags(html_data[tag_close + 1:])
        inner_html_index = html_data.find(extract_output["remainder"]) - (len(tag_type) + 2)
        if inner_html_index < 0 or inner_html_index >= len(html_data):
            inner_html_index = len(html_data) - (len(tag_type) + 2)

        tag = DOMElement(tag_type, tag_id, tag_classes, html_data[tag_close + 1: inner_html_index - 1])
        if extract_output["tags"] is not None:
            tag.set_children(extract_output["tags"])

        tags.append(tag)
        html_data = extract_output["remainder"]

    return {"tags": tags, "remainder": html_data}

def getAttribute(html_data, attribute):
    """Helper function that accepts a string of HTML data and looks for the first attribute in html_data.
       Returns the attribute's assignment if found, otherwise returns empty string"""
    assignment_index = html_data.find(attribute)
    if assignment_index == -1:
        return ""

    property_index = assignment_index + 2   # Add 2 to account for the leading ="
    assignment_trimmed = html_data[property_index:]
    return assignment_trimmed[:assignment_trimmed.find("\"")]

def getTagType(tag_data):
    stop_index = tag_data.find(" ")
    if stop_index == -1:
        return tag_data
    else:
        return tag_data[:stop_index]

def get_HTML_data(url):
    """Makes an AJAX GET request and returns the unformatted HTML data from that"""
    if "http" not in url:   # Prepend http:// if http or https is not already present
        url = "http://" + url
    print "Attempting to fetch HTML from " + url
    try:
        response = urllib2.urlopen(url)
        return re.sub(">\s*<", "><", response.read())
    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):   # HTML Error, will contain a code property
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code

if __name__ == "__main__":
    default_configuration_file = "config.html"
    print "Attempting to read default configuration file (config.html)"


    RecluseConsole().cmdloop("Welcome to Recluse")