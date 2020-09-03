[![Maintainability](https://api.codeclimate.com/v1/badges/dc3d59db7b47dcdfd224/maintainability)](https://codeclimate.com/github/Dekevich/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/dc3d59db7b47dcdfd224/test_coverage)](https://codeclimate.com/github/Dekevich/python-project-lvl2/test_coverage)

### JSON file diff generator.

A console utility that shows the diff of two JSON files.

#### Installation

To install the package run the following command from the command line:
    
     > pip install --user --extra-index-url https://test.pypi.org/simple/ dekevich-gendiff

On some systems you may need to type pip3 instead of pip, like this:

    > pip3 install --user --extra-index-url https://test.pypi.org/simple/ dekevich-gendiff

#### Usage example
Suppose we have two JSON files with the following content:
    
file1.json:

    {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": false
    }
    
file2.json:

    {
        "timeout": 20,
        "verbose": true,
        "host": "hexlet.io"
    }

The basic program usage would look like this:

    > gendiff file1.json file2.json
    
    > {
        - follow: False
        - proxy: 123.234.53.22
        + verbose: True
        - timeout: 50
        + timeout: 20
          host: hexlet.io
    }

##### Installation and usage asciinema:

[![asciicast](https://asciinema.org/a/xNOfmQ1btyhumDj6bo4LkrzEB.svg)](https://asciinema.org/a/xNOfmQ1btyhumDj6bo4LkrzEB)
