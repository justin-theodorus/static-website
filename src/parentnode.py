from src.htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)
    def to_html(self):
        

        # Recursive step: render each child's HTML
        children_html = ''.join(child.to_html() for child in self.children)

        props_str = self.props_to_html()
        return f"<{self.tag}{(' ' + props_str) if props_str else ''}>{children_html}</{self.tag}>"
