class CaseViewSet:
    api = None
    account = None

    def __getattr__(self, item):
        if item == "response":
            self.__request_api()
            return self.response
        if item == "params":
            pass
        super(CaseViewSet, self).__getattr__(item)


    def __request_api(self):
        if self.api is not None:
            response = self.api().as_view()
            setattr(self, "response", response)
            pass
