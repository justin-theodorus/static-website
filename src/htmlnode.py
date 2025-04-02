class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        if self.value is not None:
            # Leaf node
            if self.tag is None:
                return self.value
            else:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>".replace(" >", ">")
        elif self.children:
            # Parent node
            inner_html = "".join([child.to_html() for child in self.children])
            return f"<{self.tag} {self.props_to_html()}>{inner_html}</{self.tag}>".replace(" >", ">")
        else:
            return ""

    def props_to_html(self):
        if self.props:
            ans = ''
            for key,val in self.props.items():
                ans += key + '="' + val +  '" '
            return ans[:-1]
        else:
            return ''
    def __repr__(self):
        return (
            f"HTMLNode("
            f"tag={self.tag!r}, "
            f"value={self.value!r}, "
            f"children={self.children!r}, "
            f"props={self.props!r})"
        )