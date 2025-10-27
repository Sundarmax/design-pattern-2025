class HttpRequest:

    def __init__(self,builder):
        self.url = builder.url
        self.method = builder.method
        self.headers = builder.headers
        self.query_param = builder.query_param
        self.body = builder.body
        self.timeout = builder.timeout

    def __str__(self):
        return (
            f"HttpRequest= {self.url} , method = {self.method}, headers  {self.headers}"
        )

    class Builder:

        def __init__(self,url):
            self.url = url
            self.method = "GET"
            self.headers = {}
            self.query_param = {}
            self.body = None
            self.timeout = 30000

        def method(self,method):
            self.method = method
            return  self

        def add_header(self,k,v):
            self.headers.update(
                {k:v}
            )
            return self

        def add_query_param(self, k, v):
            self.query_param[k] = v
            return self

        def body(self, body):
            self.body = body
            return  self

        def timeout(self, timeout):
            self.timeout = timeout
            return  self

        def build(self):
            return  HttpRequest(self)

if __name__ == "__main__":
    request1 = HttpRequest.Builder("https:\\sundarmax.com").build()
    print(request1)

    request2 = HttpRequest.Builder("https:\\sundarmax01.com").add_query_param(id,90).add_header("is_admin",True).build()
    print(request2)
