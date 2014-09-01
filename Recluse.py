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
        print get_HTML_data(url)

    def help_run(self):
        print help_print("run [url]", "Run Recluse on url")

    def do_exit(self, line):
        """Exit the program"""
        return True

class DOMElement():
    """Data structure to represent DOM elements"""
    def __init__(self, tag, id, classes, children):
        self.tag = tag
        self.id = id
        self.classes = classes
        self.children = children

def help_print(command_syntax, help_text):
    """Prints command help consistently for the console, with the help text at column 30"""
    whitespace_append = 26 - len(command_syntax)
    return command_syntax.rjust(4 + len(command_syntax), ' ') + \
           help_text.rjust(whitespace_append + len(help_text), '.')

def configure(filename):
    """Set crawler configuration to file"""


def construct_DOM_tree(file_data):
    """Returns a DOMElement representing the HTML in file_data"""


def get_HTML_data(url):
    """Makes an AJAX GET request and returns the whitespace removed HTML data from that"""
    if "http" not in url:   # Prepend http:// if http or https is not already present
        url = "http://" + url
    print "Attempting to fetch HTML from " + url
    try:
        response = urllib2.urlopen(url)
        return re.sub('\s+', '', response.read())
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