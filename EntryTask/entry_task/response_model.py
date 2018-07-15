class ResponseBody:

    def __init__(self,success,message):
        self.success = success
        self.message = message

    def as_json(self):
        return dict(
            success=self.success,
            message=self.message,
        )