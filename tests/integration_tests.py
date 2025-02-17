import os
import unittest
from src.renderer import NanoGalleryTemplateRenderer
from ggallery.renderers.base_renderer import RendererParameters
from ggallery.model import AlbumConfig, PhotoConfig, RenderedFile


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

    def test_render_single_page(self):
        result = self.renderer.render(self.parameters)
        self.__export_results("docs-spa", result)

    def test_render_multiple_pages(self):
        self.parameters.template_parameters = {"album_routing": True}
        result = self.renderer.render(self.parameters)
        self.__export_results("docs", result)

    def __export_results(self, folder, result: RenderedFile | list[RenderedFile]):
        if not isinstance(result, list):
            result = [result]
        for file in result:
            path = f"{folder}/{file.name}"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if isinstance(file.content, bytes):
                with open(path, "wb") as f:
                    f.write(file.content)
            elif isinstance(file.content, str):
                with open(path, "w") as f:
                    f.write(file.content)


if __name__ == "__main__":
    unittest.main()
