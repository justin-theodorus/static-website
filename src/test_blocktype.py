import unittest
from blocktype import BlockType
from block_to_block import block_to_block_type  # adjust path

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Subheading"), BlockType.HEADING)

    def test_code_block(self):
        code = "```\ndef hello():\n    return 'hi'\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote_block(self):
        quote = "> This is a quote\n> Another quote line"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- Item one\n- Item two\n- Item three"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        para = "This is just a normal paragraph of text."
        self.assertEqual(block_to_block_type(para), BlockType.PARAGRAPH)

    def test_mixed_list_fail(self):
        bad_list = "1. First\n3. Third"
        self.assertEqual(block_to_block_type(bad_list), BlockType.PARAGRAPH)

    def test_mixed_unordered(self):
        bad_ul = "- Item one\nAnother line"
        self.assertEqual(block_to_block_type(bad_ul), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
