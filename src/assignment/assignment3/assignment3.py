from readhtml import readhtml
from htmlvalidator import HtmlValidator

r = readhtml()
# f = r.readfile("city.html")
# print(type(f))
h = HtmlValidator("city.html", r)
h.validate()