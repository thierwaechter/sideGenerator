class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_htlm(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        props_html = ""
        if self.props:
            for prop in self.props:
                props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
