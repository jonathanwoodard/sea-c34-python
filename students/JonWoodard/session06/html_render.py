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

    def __init__(self, content=None):
        self.children = [content] if content else []
        # self.content = self.indent + str(self.content) if content else ""

    def append(self, content):
        """Append string to content."""
        self.children.append(content)
        # self.content += (
        #    u"{indent}{str}\n".format(indent=self.indent, str=str(string))
        #    )

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        # output = (
        #    u"{indent}<{tag}>\n"
        #    "{indent}{content}"
        #    "{indent}<{tag}>"
        #    ).format(indent=ind, tag=self.tag, content=self.content)

        file_out.write(u"{indent}<{tag}>\n".format(indent=ind, tag=self.tag))
        for child in self.children:
            try:
                child.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(
                    u"{indent}{child}\n".format(
                        indent=self.indent, child=unicode(child))
                    )
        file_out.write(u"{indent}</{tag}>\n".format(indent=ind, tag=self.tag))


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
