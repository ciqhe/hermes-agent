# 这是 Vercel 专用入口，绕过 hermes 自带的 lazy-install 逻辑
from hermes_cli.web_server import app

# 直接导出 app，让 Vercel 运行
__all__ = ["app"]
