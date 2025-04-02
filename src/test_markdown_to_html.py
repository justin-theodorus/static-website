import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_single_heading(self):
        md = "# Heading"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(result, "<div><h1>Heading</h1></div>")

    def test_paragraph_with_inline(self):
        md = "This is **bold** and _italic_ text."
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(result, "<div><p>This is <b>bold</b> and <i>italic</i> text.</p></div>")

    def test_code_block(self):
        md = "```\ndef hello():\n  return 'hi'\n```"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(result, "<div><pre><code>def hello():\n  return 'hi'</code></pre></div>")

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(result, "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>")

    def test_ordered_list(self):
        md = "1. First\n2. Second"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(result, "<div><ol><li>First</li><li>Second</li></ol></div>")

    def test_blockquote(self):
        md = "> Line 1\n> Line 2"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(result, "<div><blockquote>Line 1 Line 2</blockquote></div>")

    def test_multiple_blocks(self):
        md = "# Title\n\nThis is a paragraph.\n\n- One\n- Two"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(
            result,
            "<div><h1>Title</h1><p>This is a paragraph.</p><ul><li>One</li><li>Two</li></ul></div>"
        )

    def test_inline_link_and_image(self):
        md = "This is a [link](https://example.com) and ![img](img.png)"
        result = markdown_to_html_node(md).to_html()
        self.assertEqual(
            result,
            '<div><p>This is a <a href="https://example.com">link</a> and <img src="img.png" alt="img"></p></div>'
        )

if __name__ == "__main__":
    unittest.main()
