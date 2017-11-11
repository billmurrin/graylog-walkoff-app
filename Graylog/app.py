from apps import App, action
from pygraylog.graylogapi import GraylogAPI


class Graylog(App):
    def __init__(self, name=None, device=None):
        device = "Graylog"
        App.__init__(self, name, device)
        self.api = GraylogAPI(self.device_fields['serveruri'], api_key=self.device_fields['apikey'])
        self.query_params = {}

    @action
    def param(self, key, value):
        self.query_params[key] = value

    @action
    def relative_search(self, query):

        if 'query' not in self.query_params:
            self.query_params['query'] = query

        result = self.api.api.search.universal.relative.get(**self.query_params)

        return result

    def shutdown(self):
        return
