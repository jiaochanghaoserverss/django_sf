from common.views import BaseRequestHandler


# 首页view
class IndexHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>hello word</h1>")

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
