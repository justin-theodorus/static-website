import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_one_child(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, "Normal"),
            LeafNode("i", "Italic")
        ]
        parent = ParentNode("p", children)
        self.assertEqual(parent.to_html(), "<p><b>Bold</b>Normal<i>Italic</i></p>")

    def test_to_html_with_nested_children(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_raises_without_tag(self):
        child = LeafNode("b", "text")
        with self.assertRaises(ValueError):
            ParentNode(None, [child])


    def test_to_html_raises_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

if __name__ == "__main__":
    unittest.main()
