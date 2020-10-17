## PSKScoreMaker

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/PSKScoreMaker/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%203.8-blue.svg)](https://github.com/yp05327/PSKScoreMaker#)

[中文](https://github.com/yp05327/PSKScoreMaker/blob/master/README_CN.md)

[日本語](https://github.com/yp05327/PSKScoreMaker/blob/master/README_JP.md)

# Introduction 
This is a tool for Project SeKai. If you have some good ideas, and want to share to me, you can add issues at [here](https://github.com/yp05327/BangScoreMaker/issues).

Support Features:
 ```
auto make score pictures(from official score files)
```

# Update Record
[Click here](https://github.com/yp05327/PSKScoreMaker/blob/master/update.md)

# How to use
1、You need to install the running environment.This program is written by Python, so you need to install Python first.You can get Python [here](https://www.python.org/downloads/). Version 3.7 or 3.8 is recommended.

And after installed Python, open the console, install requirements.

```shell
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

2、Download source code. 

3、Put the official music score file into 'musiccore' folder.

*4、Put textures into 'images' folder.

The list of these textures:

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

5、Open the console and turn to the folder of the source code, run:

```shell
python main.py (music score file's name)

for example: if the music score file's name is '0003_expert.txt',
then
python main.py 0003_expert.txt
```

Notes:
1、In step 4, to avoid copyright infringement, I won't upload the textures.

2、Output is a temp file, i won't add any save features. So if you want to save it, please do that by yourself.

# Bug report or advise

[Click here](https://github.com/yp05327/PSKScoreMaker/issues)