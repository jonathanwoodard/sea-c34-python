#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):
    """An HTML element."""
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None, **kwargs):
        self.children = [content] if content else []
        self.attributes = kwargs

    def append(self, content):
        """Append content."""
        self.children.append(content)

    def render(self, file_out, ind=""):
        """Render content, including tags, indentation."""

        file_out.write(
            u"{indent}<{tag}".format(indent=ind, tag=self.tag))
        if self.attributes:
            for key, value in self.attributes.items():
                file_out.write(' {}="{}"'.format(key, value))
        file_out.write(u">\n")
        for child in self.children:
            try:
                child.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(
                    u"{indent}{child}\n"
                    .format(indent=self.indent + ind, child=unicode(child))
                    )
        file_out.write(
            u"{indent}</{tag}>\n"
            .format(indent=ind, tag=self.tag))


class Html(Element):
    header = u"<!DOCTYPE html>\n"
    tag = u"html"

    def render(self, file_out, ind=u""):
        file_out.write(self.header)
        Element.render(self, file_out, ind)


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"


class Head(Element):
    tag = u"head"


class OneLineTag(Element):
    indent = u""

    def render(self, file_out, ind=u""):
        file_out.write(
            u"{indent}<{tag}".format(indent=ind, tag=self.tag))
        if self.attributes:
            for key, value in self.attributes.items():
                file_out.write(' {}="{}"'.format(key, value))
        file_out.write(u">")
        for child in self.children:
            try:
                child.render(file_out)
            except AttributeError:
                file_out.write(
                    u"{child}"
                    .format(child=unicode(child))
                    )
        file_out.write(
            u"</{tag}>\n".format(tag=self.tag))


class Title(OneLineTag):
    tag = u"title"


class SelfClosingTag(Element):

    def render(self, file_out, ind=u""):
        file_out.write(
            u"{indent}<{tag} />\n".format(indent=ind, tag=self.tag))


class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = u"br"


class Meta(SelfClosingTag):
    tag = "meta"

    def __init__(self, content=None, **kwargs):
        SelfClosingTag.__init__(self, content, **kwargs)

    def render(self, file_out, ind=u""):
        file_out.write(
            u"{indent}<{tag}".format(indent=ind, tag=self.tag))
        if self.attributes:
            for key, value in self.attributes.items():
                file_out.write(' {}="{}"'.format(key, value))
        for child in self.children:
            try:
                child.render(file_out)
            except AttributeError:
                file_out.write(
                    u"{child}"
                    .format(child=unicode(child))
                    )
        file_out.write(u" />\n")


class A(OneLineTag):
    tag = u"a"

    def __init__(self, link, content, **kwargs):
        self.link = link
        OneLineTag.__init__(self, content, href=link, **kwargs)


class Ul(Element):
    tag = u"ul"


class Li(Element):
    tag = u"li"


class H(OneLineTag):
    tag = u"h"

    def __init__(self, number, content, **kwargs):
        self.number = number
        self.tag = u"h{}".format(number)
        OneLineTag.__init__(self, content, tag=self.tag, **kwargs)
