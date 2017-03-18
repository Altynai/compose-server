# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os

from bs4 import BeautifulSoup
from bs4.element import NavigableString
from pynliner import Pynliner


class BaseHTMLComposer(object):

    __metaclass__ = ABCMeta

    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    @abstractmethod
    def compose(self):
        raise NotImplementedError("method compose is not implemented")


class DummyHTMLComposer(BaseHTMLComposer):

    def __init__(self, html):
        super(DummyHTMLComposer, self).__init__(html)
        where = os.path.dirname(__file__)
        path = os.path.join(where, "..", "resource", "style.css")
        with open(path, "r") as fd:
            self.css = fd.read()

    def compose(self):
        children = self.soup.body.children
        tags = [str(_) for _ in children if not isinstance(_, NavigableString)]
        prettify = "".join(tags)
        pynliner = Pynliner()
        return pynliner.from_string(prettify).with_cssString(self.css).run()
