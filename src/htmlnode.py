class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {name}="{val}"' for name, val in self.props.items())

    def __repr__(self):
        tag_repr = self.tag if self.tag else None
        value_repr = self.value if self.value else None
        children_repr = ''.join(c for c in self.children) if self.children else None
        return f"HTMLNode(tag={tag_repr},value={value_repr}, children={children_repr}, props={self.props_to_html()})"
