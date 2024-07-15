# Markdown2IMG
将markdown文本渲染为图片输出
## 依赖
需要额外安装wkhtmltopdf

### Ubuntu/Debian
```shell
sudo apt-get install wkhtmltopdf
```
### MacOSX
```shell
brew install --cask wkhtmltopdf
```

## 配置
配置位于`plugins/Markdown2IMG/config.py`

img_config: imgkit参数，详见[wkhtmltoimage参数](https://wkhtmltopdf.org/usage/wkhtmltopdf.txt)

markdown_config: markdown参数，详见[python markdown](https://python-markdown.github.io/reference/)

