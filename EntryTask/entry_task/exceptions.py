class AuthenticationFailed(Exception):
    status_code = 401
    message = 'Incorrect authentication credentials'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message


class WrongInputType(Exception):
    status_code = 400
    message = 'Wrong input type'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message


class InsertError(Exception):
    status_code = 400
    message = 'Cannot insert into database'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message


class NotFoundError(Exception):
    status_code = 404
    message = 'Cannot find'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message




