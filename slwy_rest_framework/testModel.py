from slwy_rest_framework.fields import ParamField

class ModelCase:
    api = None
    account = None

    def __getattr__(self, item, **kwargs):
        if item == "response":
            self.__request_api()
            return self.response
        # if item == "params":
        #     self.__reset_params(kwargs['data'])
        super(ModelCase, self).__getattr__(item)

    def __request_api(self):
        if self.api is not None:
            response = self.api().as_view()
            setattr(self, "response", response)
            pass

    # def __reset_params(self, data):
    #     if isinstance(data, dict):
    #         api = self.api.params = ParamField(data)
    #         response = api().as_view()
    #         setattr(self, "response", response)
