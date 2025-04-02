import unittest
from textnode import TextNode, TextType
from markdown_pipeline import text_to_textnodes  

class TestTextToTextNodes(unittest.TestCase):

    def test_bold_only(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])

    def test_bold_italic_code(self):
        text = "**bold** and *italic* and `code`"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ])

    def test_image(self):
        text = "An image: ![alt](https://img.com/pic.png)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("An image: ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, url="https://img.com/pic.png", alt="alt"),
        ])

    def test_link(self):
        text = "Go to [site](https://site.com)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Go to ", TextType.TEXT),
            TextNode("site", TextType.LINK, url="https://site.com"),
        ])

    def test_all_combined(self):
        text = "**text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg", alt="obi wan image"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, url="https://boot.dev"),
        ])

    def test_no_markdown(self):
        text = "Just normal text"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Just normal text", TextType.TEXT)
        ])

    def test_empty_string(self):
        text = ""
        result = text_to_textnodes(text)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
