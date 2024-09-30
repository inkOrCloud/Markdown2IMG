from pkg.plugin.context import APIHost, register, handler, BasePlugin, EventContext
from pkg.plugin.events import *
from plugins.Markdown2IMG.config import *
from markdown import *
from plugins.Markdown2IMG.config import *
import imgkit
import base64
import os
from mirai import Image

img_path = './plugins/Markdown2IMG/output.'+ img_config['format']

@register(name="Markdown2IMG", description="将markdown文本转为图片输出", version="0.1", author="inkorcloud")
class Markdown2IMG(BasePlugin):
    def __init__(self, host: APIHost):
        super().__init__(host)
        pass
        
    @handler(NormalMessageResponded)
    async def process(self, ctx: EventContext, **kwargs):
        html = (
        html_front 
        + markdown(
            text=ctx.event.response_text, 
            extensions=["mdx_math","fenced_code"], 
            extension_configs=markdown_config
            )
        + html_end)
        imgkit.from_string(html, img_path, options=img_config)
        img_base64 = base64.b64encode(open(img_path, 'rb').read()).decode()
        ctx.add_return('reply', [Image(base64=img_base64)])
        ctx.prevent_postorder()
        if os.path.exists(img_path):
            os.remove(img_path)
            pass
        pass
    
    def __del__(self):
        pass