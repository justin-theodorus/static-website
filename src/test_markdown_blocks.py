import unittest
from markdown_to_block import markdown_to_blocks  # adjust path if needed

class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_heading_block(self):
        md = "# Heading"
        self.assertEqual(markdown_to_blocks(md), ["# Heading"])

    def test_multiple_blocks(self):
        md = (
            "# Heading\n\n"
            "Paragraph text.\n\n"
            "- Item 1\n- Item 2"
        )
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "# Heading",
                "Paragraph text.",
                "- Item 1\n- Item 2"
            ]
        )

    def test_strip_whitespace(self):
        md = "  # Heading  \n\n  Text with space   "
        self.assertEqual(
            markdown_to_blocks(md),
            ["# Heading", "Text with space"]
        )

    def test_empty_string(self):
        md = ""
        self.assertEqual(markdown_to_blocks(md), [])

    def test_excessive_newlines(self):
        md = "\n\n\n# Heading\n\n\n\nParagraph\n\n\n"
        self.assertEqual(
            markdown_to_blocks(md),
            ["# Heading", "Paragraph"]
        )

if __name__ == "__main__":
    unittest.main()
