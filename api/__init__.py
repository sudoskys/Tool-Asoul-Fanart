# -*- coding: utf-8 -*-


class App(object):
    def __init__(self, config):
        self.config = config
        pass

    def start(self, token, ids):
        from .config import Runner
        Runner(token, ids).Push(self.config)
