import unittest
from htmlnode import HtmlNode  

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html_with_attributes(self):
        node = HtmlNode(props={"href": "https://example.com", "target": "_blank"})
        expected = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_no_attributes(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HtmlNode(tag="a", value="Click me", props={"href": "https://example.com"})
        repr_str = repr(node)
        self.assertIn("HTMLNode(tag='a'", repr_str)
        self.assertIn("value='Click me'", repr_str)
        self.assertIn("'href': 'https://example.com'", repr_str)

if __name__ == "__main__":
    unittest.main()
