from unittest import TestCase
from hashlib  import sha1, sha256, sha512, md5




from reqio.toolkit import NamingFunctions
from testlib.fake      import FakeReadyRequest


request = FakeReadyRequest()
bytes_  = request.response.content





class TestNamingFunctions(TestCase):
    hex = lambda m, arg: m(arg).hexdigest()
    def test_url_hashsum(self) -> None:
        methods = [
            [NamingFunctions.url_md5sum   , md5],
            [NamingFunctions.url_sha1sum  , sha1],
            [NamingFunctions.url_sha256sum, sha256],
            [NamingFunctions.url_sha512sum, sha512],
        ]
        for method, row_method in methods:
            self.assertEqual(method(request), TestNamingFunctions.hex(row_method, request.url.encode()))


