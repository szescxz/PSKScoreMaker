## PSKScoreMaker

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/PSKScoreMaker/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%203.8-blue.svg)](https://github.com/yp05327/PSKScoreMaker#)

[English](https://github.com/yp05327/PSKScoreMaker/blob/master/README.md)

[日本語](https://github.com/yp05327/PSKScoreMaker/blob/master/README_JP.md)

# 介绍 
这是一个为 Project SeKai 而写的一个工具。如果你有什么好的想法，并且愿意与我分享，你可以在[这里](https://github.com/yp05327/PSKScoreMaker/issues)添加issues.

支持功能：
 ```
自动生成铺面图片（从官方的铺子文件）
```

# 更新记录
[点此查看](https://github.com/yp05327/PSKScoreMaker/blob/master/update_cn.md)

# 如何使用
1、你需要安装运行环境。这个软件是用Python写的，所以你需要先安装Python。你可以在[这里](https://www.python.org/downloads/)下载Python。推荐使用3.7或3.8版本。

在安装完Python之后，打开控制台，安装requirements。

```shell
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

2、下载源代码。

3、把谱子文件放进 “musiccore” 文件夹。

*4、把贴图放进 'images' 文件夹。

这些note文件的列表：

```
notes_normal.png
notes_crtcl.png
notes_long.png
notes_long_among.png
notes_long_among_crtcl.png
note_long_among_unvisible.png
note_long_among_unvisible_crtcl.png
notes_flick.png

notes_flick_arrow_01.png
notes_flick_arrow_01_diagonal.png
notes_flick_arrow_crtcl_01.png
notes_flick_arrow_crtcl_01_diagonal.png

notes_flick_arrow_02.png
notes_flick_arrow_02_diagonal.png
notes_flick_arrow_crtcl_02.png
notes_flick_arrow_crtcl_02_diagonal.png

notes_flick_arrow_03.png
notes_flick_arrow_03_diagonal.png
notes_flick_arrow_crtcl_03.png
notes_flick_arrow_crtcl_03_diagonal.png

notes_flick_arrow_04.png
notes_flick_arrow_04_diagonal.png
notes_flick_arrow_crtcl_04.png
notes_flick_arrow_crtcl_04_diagonal.png

notes_flick_arrow_05.png
notes_flick_arrow_05_diagonal.png
notes_flick_arrow_crtcl_05.png
notes_flick_arrow_crtcl_05_diagonal.png

notes_flick_arrow_06.png
notes_flick_arrow_06_diagonal.png
notes_flick_arrow_crtcl_06.png
notes_flick_arrow_crtcl_06_diagonal.png
```

5、打开控制台，转到源代码所在目录下，运行：

```shell
python main.py (music score file's name)

例：如果铺子文件名是“0003_expert.txt”的话，
那么，
python main.py 0003_expert.txt
```

提示:
1、在第四步，为了避免侵权，我不会上传贴图文件。

2、输出是一个临时文件，我不会添加任何保存的功能。所以如果你想要保存它，请你自己去完成。

# 问题反馈或建议

[点击此处](https://github.com/yp05327/PSKScoreMaker/issues)