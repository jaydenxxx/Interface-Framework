class ParamsModelMixin:
    @staticmethod
    def update_request_data(data):
        if isinstance(data, dict):
            pass
        else:
            raise TypeError("data must be a dict!")

    def reset_request_data(self):
        pass
