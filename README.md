## Description

This repository contains a template and a script to generate an HTML photo gallery using [ggallery](https://github.com/creeston/ggallery) tool.

[![npm](https://img.shields.io/badge/demo-online-008000.svg)](https://creeston.github.io/ggallery-nanogallery2)


## Usage

In your `ggallery` configuration file, specify the template URL:

```yaml
template:
    url: https://github.com/creeston/ggallery-nanogallery2
```


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