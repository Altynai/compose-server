# -*- coding: utf-8 -*-


class TestComposer(object):

    def test_none(self, client, dormouse_html):
        response = client.post("/compose", data=dormouse_html)
        return dormouse_html == response.data

    def test_dummy(self, client, dormouse_html):
        response = client.post("/compose?type=dummpy", data=dormouse_html)
        first = response.data
        assert client.post("/compose?type=dummpy", data=first).data == first
