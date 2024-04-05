class BrowserHistory:
    def __init__(self, homepage: str):
        # Use a list to track visited urls. Note that a visit() after back() removes
        # url after back() to url
        pass

    def visit(self, url: str) -> None:
        pass

    def back(self, steps: int) -> str:
        pass

    def forward(self, steps: int) -> str:
        pass


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
