## Description

This repository contains a template and a script to generate an HTML photo gallery using [ggallery](https://github.com/creeston/ggallery) tool.

[![npm](https://img.shields.io/badge/demo-online-008000.svg)](https://creeston.github.io/ggallery-nanogallery2)


## Usage

In your `ggallery` configuration file, specify the template URL:

```yaml
template:
    url: https://github.com/creeston/ggallery-nanogallery2
    parameters:
        album_routing: true | false # If disabled, website will be rendered as Single Page Application, otherwise each album will have its own route
        viewer_download_button: true | false # Adds a download button to the full-image viewer, to the left of the close button. Default: false
        thumbnail_download_button: true | false # Adds a download button to every photo thumbnail (not album covers). Default: false
```

Both download options use nanogallery2's own `downloadButton`/`DOWNLOAD` toolbar actions — no custom JS was added. Verified (via Playwright, against photos hosted on a different origin — Azure Blob Storage — than the gallery page itself) that this forces a real browser download rather than just opening the image in a new tab, so no CORS configuration or custom fetch-as-blob JS is needed on the storage side.


## References

Template uses the following technologies:

- **[nanogallery2](https://nanogallery2.nanostudio.org/)**
- **[bulma](https://bulma.io/)**
- **[FontAwesome](https://fontawesome.com/)**


## Development

### Prerequisites

```sh
python3 -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the Tests

To run the tests, use the following command:

```sh
python -m unittest discover -p *_tests.py
```