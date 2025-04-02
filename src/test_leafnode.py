import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_html_with_tag(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_html_with_no_tag(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_html_with_props(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = LeafNode("a", "Click me!", props)
        expected = '<a href="https://google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_missing_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_children_is_none(self):
        node = LeafNode("p", "No children")
        self.assertIsNone(node.children)

if __name__ == '__main__':
    unittest.main()
