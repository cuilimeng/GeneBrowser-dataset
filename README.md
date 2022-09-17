# GeneBrowser-dataset
## Introduction
This dataset is collected from [3billion](https://3billion.io/gene/). If you use this dataset or the web scraper, please cite this repository properly:
```
@misc{cui2022genebrowser,
  author = {Cui, Limeng},
  title = {GeneBrowser-dataset},
  url = {https://github.com/cuilimeng/GeneBrowser-dataset},
  year = {2022}
}
```
## Installation
You should run __dir_crawler.py__ to get all the gene URLs and then __content_crawler.py__ to parse the web contents of each URL.

## Requirements
Credits for [3billion](https://3billion.io/).
ChromeDriver installation - https://chromedriver.chromium.org/.