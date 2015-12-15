#!/usr/bin/python

import re
import requests

def store_completed_courses(sign_on_html):
    completed_courses = []
    match = re.search(r"> ([A-Z]{4}\d{4}) - \w+ <", sign_on_html)
    print match.group

def check_uoc(program_code):

    """Given a program code e.g 3852,
    returns the UOC required for completion"""

    html = requests.get("http://www.handbook.unsw.edu.au/undergraduate/programs/2016/" + program_code + ".html")
    match = re.search(r"<p><strong>Min UOC For Award:</strong>&nbsp;(\d+)</p>", str(html.content))
    uoc = match.group(1)
    return uoc


def main():
    html = requests.get("https://my.unsw.edu.au/portal/faces/oracle/webcenter/portalapp/pages/studentProfile.jspx?_adf.ctrl-state=88nrwxvxk_77&_afrLoop=22347719481187226")
    store_completed_courses(str(html.content))

if __name__ == "__main__":
    main()
