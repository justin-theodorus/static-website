from src.htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        props_str = self.props_to_html()

        if self.tag == "img":
            return f"<img{(' ' + props_str) if props_str else ''}>"


        return f"<{self.tag}{(' ' + props_str) if props_str else ''}>{self.value}</{self.tag}>"


