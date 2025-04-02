import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_link, split_nodes_image, split_nodes_delimiter

class TestSplitMarkdownNodes(unittest.TestCase):

    # ----- LINK TESTS -----

    def test_single_link(self):
        node = TextNode("Click [here](https://example.com)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, url="https://example.com")
        ])

    def test_multiple_links(self):
        node = TextNode("[One](url1) and [Two](url2)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [
            TextNode("One", TextType.LINK, url="url1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Two", TextType.LINK, url="url2")
        ])

    def test_text_with_no_links(self):
        node = TextNode("Just plain text.", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_non_text_node_is_ignored_link(self):
        node = TextNode("Don't touch me", TextType.BOLD)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    # ----- IMAGE TESTS -----

    def test_single_image(self):
        node = TextNode("Look at this ![alt](https://image.com)", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [
            TextNode("Look at this ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, url="https://image.com", alt="alt")
        ])

    def test_multiple_images(self):
        node = TextNode("![one](u1) and ![two](u2)", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [
            TextNode("one", TextType.IMAGE, url="u1", alt="one"),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.IMAGE, url="u2", alt="two")
        ])

    def test_text_with_no_images(self):
        node = TextNode("This has no pictures", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_non_text_node_is_ignored_image(self):
        node = TextNode("I'm already bold", TextType.BOLD)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])
    def test_single_delimiter_pair(self):
        input_node = TextNode("This is **bold** text.", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ])

    def test_multiple_delimiter_pairs(self):
        input_node = TextNode("**bold** and **strong**", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("strong", TextType.BOLD)
        ])

    def test_no_delimiter(self):
        input_node = TextNode("This has no markup", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        self.assertEqual(result, [input_node])

    def test_empty_delimited_parts(self):
        input_node = TextNode("A ** ** B", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("A ", TextType.TEXT),
            TextNode(" ", TextType.BOLD),
            TextNode(" B", TextType.TEXT)
        ])

    def test_non_text_type_node(self):
        input_node = TextNode("Already bold", TextType.BOLD)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        self.assertEqual(result, [input_node])  # Should remain unchanged

    def test_odd_number_of_delimiters(self):
        input_node = TextNode("Unclosed **bold phrase", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        # Split will result in ["Unclosed ", "bold phrase"]
        self.assertEqual(result, [
            TextNode("Unclosed ", TextType.TEXT),
            TextNode("bold phrase", TextType.BOLD)
        ])
if __name__ == "__main__":
    unittest.main()
