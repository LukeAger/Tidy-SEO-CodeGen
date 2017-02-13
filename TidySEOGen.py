import time

banner = """\n

               ____  _
              | __ )| | ___   __ _
              |  _ \| |/ _ \ / _` |
              | |_) | | (_) | (_| |
              |____/|_|\___/ \__, |
               ____          |___/
              / ___|___   __| | ___
             | |   / _ \ / _` |/ _ |
             | |__| (_) | (_| |  __/
   ____       \____\___/ \__,_|\___|
  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
 | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_| |  __/ | | |  __/ | | (_| | || (_) | |
  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|

       Charlotte Ager - Lifeofwife.com

"""

print banner
time.sleep(1)
print "Easily Create Your Wordpress SEO Tags"
time.sleep(1)


part1 = "<DIVSTYLE=\"DISPLAY:NONE;\">"
part2 = "<IMGCLASS=\"ALIGNCENTERSIZE-LARGEWP-IMAGE-281\"SRC=\""
print "Enter Image Address such as http://www.sample.com/image.jpg"
url = raw_input("Web Address::")
part4 = "\"ALT=\""
print "Enter Your Blogs Top Keywords"
keywords = raw_input("Keywords::")
part5 = "\"WIDTH=\"595\"HEIGHT=\"1010\"/>"
part6= "</DIV>"
time.sleep(1)
print "Generating Code..."
time.sleep(1)
end = """Here is your code, if it doesn't work it's your fault...

"""
part7 = """

"""
print end + part1 + part2 + url + part4 +keywords + part5 + part6 + part7



