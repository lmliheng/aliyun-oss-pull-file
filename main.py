# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog, messagebox
import oss2
from tqdm import tqdm
import time
import pyperclip

def upload_file():
    local_file_path = filedialog.askopenfilename()
    oss_object_name = local_file_path.split('/')[-1]

    auth = oss2.Auth('xxxx', 'xxxx')
    bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'heng1')

    with tqdm(total=1, desc="上传进度", ncols=100) as progress_bar:
        bucket.put_object_from_file(oss_object_name, local_file_path, progress_callback=lambda consumed_bytes, total_bytes: progress_bar.update(consumed_bytes / total_bytes))

    print(f'文件 {local_file_path} 已成功上传至OSS，对象名为：{oss_object_name}')
    url = f"https://heng1.oss-cn-beijing.aliyuncs.com/{oss_object_name}"
    messagebox.showinfo("上传成功!", f"文件 {local_file_path} 已成功上传至OSS，使用URL为：{url}，点击确认后会自动复制URL到剪切板并删除页面！")
    pyperclip.copy(url)
    time.sleep(0)
    root.destroy()

root = tk.Tk()
root.title("OSS文件上传")

frame = tk.Frame(root)
frame.pack(padx=50, pady=50)

button_browse = tk.Button(frame, text="浏览文件并上传", command=upload_file)
button_browse.pack(pady=10)

root.mainloop()