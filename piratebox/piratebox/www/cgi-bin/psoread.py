#!/usr/bin/python

# PyShoutOut by Joey C. (http://www.joeyjwc.x3fusion.com)
# Read the data from a shout-out file.


# Changed by Matthias Strubel / 2011-02-27 for piratebox-path

#css = open("style.css", 'r')
data = open("data.pso", 'r')
#stl = css.read()
dat = data.read()
#css.close()
data.close()
print "Content-type:text/html\r\n\r\n"
print "<div class=\"shout\">"
print dat
print "</div>"
