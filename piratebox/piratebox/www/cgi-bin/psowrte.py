#!/usr/bin/python

# PyShoutOut by Joey C. (http://www.joeyjwc.x3fusion.com)
# Writes the recieved information to the data file.


import cgi, datetime, os, re
print "Content-type:text/html\r\n\r\n"
datafile = open("chat.html", 'r+')
values = cgi.FieldStorage()
if values.has_key("name"):
  name = values["name"].value
else:
  name = "&nbsp;"
if values.has_key("data"):
  rawdata = values["data"].value
else:
  rawdata = "&nbsp;"
datapass = re.sub("<", "&lt;", rawdata)
data = re.sub(">", "&gt;", datapass)
color = values["color"].value
curdate = datetime.datetime.now()
old = datafile.read()
datafile.truncate(0)
datafile.close()
datafile = open("chat.html", 'r+')
datafile.write("<p><span class='date'>" + curdate.strftime("%H:%M:%S") + "</span><span class='name'>" + name + " : </span><span class='shout " + color + "'>" + data + "</span></p>\n" + old)
datafile.close()
#print """<html><head><meta http-equiv="refresh" content="0;url=/cgi-bin/psoread.py"></head><body>Reading...</body></html>"""
print """<strong>ok</strong>"""
