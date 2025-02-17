import os
from jinja2 import Environment, FileSystemLoader
from ggallery.renderers.base_renderer import (
    BaseRenderer,
    RendererParameters,
    RenderedFile,
)


class NanoGalleryTemplateRenderer(BaseRenderer):
    # We set the start ID for the albums to 1000000 to avoid conflicts with the photo IDs
    # Looks like a bug in the NanoGallery library
    GALLERY_START_ID = 1000000

    def render(
        self,
        parameters: RendererParameters,
    ) -> list[RenderedFile] | RenderedFile:
        template_parameters = parameters.template_parameters or {}

        if "album_routing" in template_parameters and template_parameters["album_routing"]:
            return self.__render_album_pages(parameters)
        return self.__render_single_page(parameters)

    def __render_single_page(
        self,
        parameters: RendererParameters,
    ) -> list[RenderedFile] | RenderedFile:
        module_folder = os.path.dirname(__file__)
        env = Environment(loader=FileSystemLoader(module_folder))
        template = env.get_template("nano-gallery.html.j2")

        items = []
        album_id = self.GALLERY_START_ID
        for album in parameters.albums:
            album.id = album_id
            photos = album.photos
            if not photos:
                continue

            album_cover = photos[0].thumbnail if album.cover is None else album.cover
            items.append(
                {
                    "src": album_cover,
                    "srct": None,
                    "album_id": None,
                    "kind": "album",
                    "title": album.title,
                    "id": album_id,
                }
            )

            for photo in photos:
                items.append(
                    {
                        "src": photo.filename,
                        "srct": photo.thumbnail,
                        "album_id": album_id,
                        "kind": None,
                        "title": photo.title,
                        "id": None,
                    }
                )
            album_id += 1

        html_index_content = template.render(
            items=items,
            items_base_url=parameters.base_url,
            title=parameters.title,
            subtitle=parameters.subtitle,
            favicon=parameters.favicon,
            albums=parameters.albums,
            thumbnail_height=parameters.thumbnail_height,
            is_album_page=False,
            is_album_routing=False,
        )

        return RenderedFile(name="index.html", content=html_index_content)

    def __render_album_pages(
        self,
        parameters: RendererParameters,
    ) -> list[RenderedFile] | RenderedFile:
        module_folder = os.path.dirname(__file__)
        env = Environment(loader=FileSystemLoader(module_folder))
        template = env.get_template("nano-gallery.html.j2")

        rendered_files = []
        items = []
        album_id = self.GALLERY_START_ID
        for album in parameters.albums:
            album.id = album_id
            photos = album.photos
            if not photos:
                continue

            album_cover = photos[0].thumbnail if album.cover is None else album.cover
            items.append(
                {
                    "src": album_cover,
                    "srct": None,
                    "album_id": None,
                    "kind": "album",
                    "title": album.title,
                    "id": album_id,
                }
            )

            album_route = album.source if album.source else album.title.lower().replace(" ", "-")
            album.route = album_route
            album_id += 1

        html_index_content = template.render(
            items=items,
            items_base_url=parameters.base_url,
            title=parameters.title,
            subtitle=parameters.subtitle,
            favicon=parameters.favicon,
            albums=parameters.albums,
            thumbnail_height=parameters.thumbnail_height,
            is_album_page=False,
            is_album_routing=True,
        )

        rendered_files.append(RenderedFile(name="index.html", content=html_index_content))

        item_id = 0
        for album in parameters.albums:
            items = []
            if not album.photos:
                continue

            for photo in album.photos:
                items.append(
                    {
                        "src": photo.filename,
                        "srct": photo.thumbnail,
                        "album_id": None,
                        "kind": None,
                        "title": photo.title,
                        "id": item_id,
                    }
                )
                item_id += 1

            gallery_favicon = f"../{parameters.favicon}" if parameters.favicon else None
            html_album_content = template.render(
                items=items,
                items_base_url=parameters.base_url,
                title=album.title,
                subtitle=album.subtitle,
                favicon=gallery_favicon,
                thumbnail_height=parameters.thumbnail_height,
                is_album_page=True,
                is_album_routing=True,
            )

            rendered_files.append(RenderedFile(name=f"{album.route}/index.html", content=html_album_content))

        return rendered_files
