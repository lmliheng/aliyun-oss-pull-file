### OSS文件上传工具
这是一个使用Python和Tkinter库创建的简单OSS文件上传工具。它可以帮助你轻松地将文件上传到阿里云OSS（对象存储服务）。

### 功能
选择本地文件并上传至OSS
显示上传进度
上传完成后，自动复制文件URL到剪切板
上传完成后，自动关闭窗口
使用方法
安装依赖库：
```bash
pip install -r requirements.txt
```
将你的阿里云OSS访问密钥（AccessKey ID和AccessKey Secret）替换到代码中的auth = oss2.Auth('xxxx', 'xxxx')。
运行代码：
```bash
python main.py
```
在弹出的窗口中，点击"浏览文件并上传"按钮，选择要上传的文件。文件将自动上传至OSS，并显示上传进度。
上传完成后，文件URL将自动复制到剪切板，同时窗口会自动关闭。
注意事项
请确保你已经安装了Python和pip。
请确保你的阿里云OSS访问密钥具有足够的权限。
在使用过程中，请注意保护你的阿里云OSS访问密钥。不要将密钥泄露给他人。
### 许可证

MIT License


### 联系方式
如有任何问题或建议，请随时与我联系。

邮箱：liheng2137@qq.com

GitHub：https://github.com/lmliheng

感谢你的使用！希望这个工具对你有所帮助！