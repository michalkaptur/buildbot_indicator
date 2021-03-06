import requests
import bs4


class StatChecker:
    def __init__(self, server_address, builders, branch):
        self.server_address = server_address
        self.builders = builders
        self.branch = branch
        self.request_address = self.server_address+"/grid?width=1&branch="+self.branch
        self.builders_status = {}

    def get_html(self):
        response = requests.get(self.request_address)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        return soup.select('table.Grid tr')

    def update_builders_status(self):
        self.builders_status = {}
        builders_html = self.get_html()
        for builder in builders_html:
            if builder.a.get_text() in self.builders:
                result = builder.find(class_="build").a.get_text()
                self.builders_status[builder.a.get_text()] = result

    def get_nok_builds(self):
        nok_builds = []
        for builder,status in self.builders_status.items():
            if status != "OK":
                nok_builds.append(builder)
        return nok_builds

    def all_builds_succedded(self):
        for builder,status in self.builders_status.items():
            if status != "OK":
                return False
        return True