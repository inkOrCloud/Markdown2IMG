
img_config = {
    'width': 400,
    'format': 'png', #jpg/png
    'zoom': 2,
    'quiet': '',
    'no-stop-slow-scripts': None,
    'enable-local-file-access': None
}
    
markdown_config = {
    'enable_dollar_delimiter': True,  # 是否启用单美元符号（默认只启用双美元）
    'add_preview': True  # 在公式加载成功前是否启用预览（默认不启用)
}

html_front = '''
<html>
<head>
<script type="text/javascript" src="https://cdn.bootcdn.net/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-MML-AM_CHTML"></script>
</head>
<style>
    #MathJax_Message {
        display: none!important;
    }
</style>
<body>
'''

html_end = '''
</body>
</html>
'''
    
    