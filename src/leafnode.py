from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")  
        if self.tag is None:
            return self.value
        else:
            props_str = self.props_to_html()
            return f"<{self.tag}{(' ' + props_str) if props_str else ''}>{self.value}</{self.tag}>"
