import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links  # Adjust path if needed

class TestMarkdownExtraction(unittest.TestCase):

    # ------------------------
    # Image extraction tests
    # ------------------------

    def test_single_image(self):
        text = "Check this image ![alt text](https://example.com/image.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "https://example.com/image.png")])

    def test_multiple_images(self):
        text = "![img1](url1) and ![img2](url2)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("img1", "url1"), ("img2", "url2")])

    def test_no_images(self):
        text = "Just some text, no images."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_image_with_special_chars(self):
        text = "![image: funny!](https://site.com/img.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("image: funny!", "https://site.com/img.png")])

    # ------------------------
    # Link extraction tests
    # ------------------------

    def test_single_link(self):
        text = "This is a [link](https://example.com)."
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://example.com")])

    def test_multiple_links(self):
        text = "[one](url1) then [two](url2)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("one", "url1"), ("two", "url2")])

    def test_link_and_image(self):
        text = "![img](imgurl) and [link](linkurl)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "linkurl")])  # ✅ should NOT include the image

    def test_no_links(self):
        text = "No links here!"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_link_with_special_chars(self):
        text = "[click here!](https://example.com/@page)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("click here!", "https://example.com/@page")])

if __name__ == '__main__':
    unittest.main()
