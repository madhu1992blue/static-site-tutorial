from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag not specified")
        if not self.children:
            raise ValueError("children not specified")
        children_html = "".join(c.to_html() for c in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
