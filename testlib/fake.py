from os import urandom

class FakeReadyRequest:
    url = "https://"
    def __init__(self, son=False) -> None:
        if son:
            self.content =  urandom(512)
        else:
            self.response = FakeReadyRequest(True)
            self.order    = 7 # 7 heavens :)


