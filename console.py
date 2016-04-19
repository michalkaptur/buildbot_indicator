import requests
import bs4

SERVER_ADDRESS = "http://buildbot.buildbot.net"
BUILDERS = ["py26-tw0900", "py26-tw1020", "py26-tw1110"]
BRANCH = "master"

response = requests.get(SERVER_ADDRESS+"/grid?width=1&branch="+BRANCH)
soup = bs4.BeautifulSoup(response.text, "html.parser")
builders_html = soup.select('table.Grid tr')
regression_stat = {}
for builder in builders_html:
    if builder.a.get_text() in BUILDERS:
        result = builder.find(class_="build").a.get_text()
        regression_stat[builder.a.get_text()] = result

failed = []
for builder,status in regression_stat.items():
    if status != "OK":
        failed.append(builder)

if len(failed) > 0:
    print("Failed builds:")
    print(failed)
else:
    print("OK")