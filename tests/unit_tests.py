from typing import cast
import unittest
from src.renderer import NanoGalleryTemplateRenderer
from ggallery.renderers.base_renderer import RendererParameters
from ggallery.model import AlbumConfig, PhotoConfig, RenderedFile


class TestNanoGalleryTemplateRenderer(unittest.TestCase):
    def setUp(self):
        self.renderer = NanoGalleryTemplateRenderer()
        self.parameters = RendererParameters(
            base_url="http://example.com/",
            title="Test Gallery",
            subtitle="A collection of test images",
            favicon="http://example.com/favicon.ico",
            albums=[
                AlbumConfig(
                    title="Album 1",
                    photos=[
                        PhotoConfig(filename="photo1.jpg", thumbnail="thumb1.jpg", title="Photo 1"),
                        PhotoConfig(filename="photo2.jpg", thumbnail="thumb2.jpg", title="Photo 2"),
                    ],
                    cover=None,
                ),
                AlbumConfig(
                    title="Album 2",
                    photos=[
                        PhotoConfig(filename="photo3.jpg", thumbnail="thumb3.jpg", title="Photo 3"),
                    ],
                    cover="cover2.jpg",
                ),
            ],
            thumbnail_height=200,
        )

    def test_render(self):
        result = self.renderer.render(self.parameters)
        self.assertIsInstance(result, RenderedFile)
        result = cast(RenderedFile, result)
        content = result.content
        self.assertIsInstance(content, str)
        content = cast(str, result.content)
        self.assertIn("<title>Test Gallery</title>", content)
        self.assertIn("src: 'cover2.jpg'", content)
        self.assertIn("src: 'photo1.jpg'", content)
        self.assertIn("srct: 'thumb1.jpg'", content)
        self.assertIn("title: 'Album 1'", content)
        self.assertIn("title: 'Photo 1'", content)


if __name__ == "__main__":
    unittest.main()
