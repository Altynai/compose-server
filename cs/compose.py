# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from bs4 import BeautifulSoup


class BaseHTMLComposer(object):

    __metaclass__ = ABCMeta

    def __init__(self, html):
        self.soup = BeautifulSoup(html)

    @abstractmethod
    def compose(self):
        raise NotImplementedError("method compose is not implemented")


class DummyHTMLComposer(BaseHTMLComposer):

    def compose(self):
        return self.soup.prettify()
