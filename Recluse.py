__author__ = 'Jake Magill'

import cmd

class Recluse_Console(cmd.Cmd):
    """Recluse UI Console"""

    def do_configure(self, filename):
        """Set crawling configuration to a text file"""
        print "Not supported at this time"

    def help_configure(self):
        print help_print("configure [filename]", "Set crawling configuration to text file at filename")

    def do_run(self, url):
        """Run Recluse on specified URL"""
        print "Not supported at this time"

    def help_run(self):
        print help_print("run [url]", "Run Recluse on url")

    def do_exit(self):
        """Exit the program"""
        return True

def help_print(command_syntax, help_text):
    """Prints command help consistently for the console, with the help text at column 30"""
    whitespace_append = 26 - len(command_syntax)
    return command_syntax.rjust(4 + len(command_syntax), ' ') + \
           help_text.rjust(whitespace_append + len(help_text), '.')



if __name__ == "__main__":
    Recluse_Console().cmdloop("Welcome to Recluse")