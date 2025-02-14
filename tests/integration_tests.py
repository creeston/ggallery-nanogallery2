import unittest
from renderer import NanoGalleryTemplateRenderer
from ggallery.renderers.base_renderer import RendererParameters
from ggallery.model import AlbumConfig, PhotoConfig


class TestNanoGalleryTemplateRenderer(unittest.TestCase):
    def setUp(self):
        self.renderer = NanoGalleryTemplateRenderer()
        self.parameters = RendererParameters(
            base_url="https://images.pexels.com/photos/",
            title="Test Gallery",
            subtitle="A collection of test images from Pexels",
            favicon=None,
            albums=[
                AlbumConfig(
                    title="Italy",
                    subtitle="A collection of images from Italy",
                    photos=[
                        PhotoConfig(
                            filename="4046386/pexels-photo-4046386.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                            thumbnail="4046386/pexels-photo-4046386.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                            title="Statue",
                        ),
                        PhotoConfig(
                            filename="208701/pexels-photo-208701.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2v",
                            thumbnail="208701/pexels-photo-208701.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2v",
                            title="Venice Canal",
                        ),
                        PhotoConfig(
                            filename="629142/pexels-photo-629142.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            thumbnail="629142/pexels-photo-629142.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            title="Pisa Tower",
                        ),
                    ],
                    cover=None,
                ),
                AlbumConfig(
                    title="Japan",
                    photos=[
                        PhotoConfig(
                            filename="402028/pexels-photo-402028.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            thumbnail="402028/pexels-photo-402028.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                        ),
                        PhotoConfig(
                            filename="590478/pexels-photo-590478.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            thumbnail="590478/pexels-photo-590478.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            title="Tokyo street",
                        ),
                    ],
                    cover="590478/pexels-photo-590478.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                ),
            ],
            thumbnail_height=800,
        )

    def test_render(self):
        result = self.renderer.render(self.parameters)
        with open("docs/index.html", "w") as f:
            f.write(result)


if __name__ == "__main__":
    unittest.main()
