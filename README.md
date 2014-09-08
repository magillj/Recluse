Recluse
=======

A basic and original web crawler

Still under development, and currently unfunctional. Here's the plan though:

Version 1 - Basic data collection. The location of the information on the page is determined by an 
            HTML configuration file. Data is read from there and then searched for across the page. 
            Output is printed to a text file.
            
Version 2 - Support for multiple definitions of where to find text, ability to ignore ids, classes,
            etc or vice versa, and the option to discard output that contains HTML in it.
            
Version 3 - Ability to follow links (configurable as to which ones)

---------------------------------------------------------------------------------------------------
So, how do I get crawling?

1. Create an HTML file with exactly the elements that you expect your desired text to be in. 

   For example, if I wanted the text between all paragraph tags with a class of "paragraph", I 
   would put the following in the configuration file: <p class="paragraph"></p>. Recluse will
   then output all text in any paragraphs with a class "paragraph"
   
2. Run Recluse from command line or terminal

3. Set the configuration file with the following command: configure [filename]

4. (Optional) Set the output file location with the command: output [directory]

   Note: if you do not set the output file manually, it will be generated in the same folder as 
   Recluse.py

5. Run on the site of your choice with the command: run [url]


That's it! Go check your output file for the results! Enjoy
