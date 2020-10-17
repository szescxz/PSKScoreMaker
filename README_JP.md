## PSKScoreMaker

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/PSKScoreMaker/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%203.8-blue.svg)](https://github.com/yp05327/PSKScoreMaker#)

[English](https://github.com/yp05327/PSKScoreMaker/blob/master/README.md)

[中文](https://github.com/yp05327/PSKScoreMaker/blob/master/README_CN.md)

# 紹介
これは Project SeKai のため、作ったツールです。いいアイデアがあれば、[ここ](https://github.com/yp05327/PSKScoreMaker/issues)でissuesを追加してください。

完成した機能：
 ```
 自動的に譜面写真を導出する（公式譜面ファイルから）
```

# 更新履歴
[こちら](https://github.com/yp05327/PSKScoreMaker/blob/master/update_cn.md)

# 使い方
1、実行環境を導入する。このツールはPythonで作ったものから、Pythonをインストールしてください。[ここ](https://www.python.org/downloads/)でPythonをダウンロードできる。バージョン3.7あるいは3.8は推薦。

Pythonをインストールした後、コンソールでrequirementsをインストールする。

```shell
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

2、ソースコードをダウンロードする。

3、譜面ファイルを「musiccore」フォルダに置く。

*4、テクスチャファイルを「images」フォルダに置く。

テクスチャファイルのリスト：

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

5、コンソールでソースコードのフォルダで実行する：

```shell
python main.py (music score file's name)

例: 譜面ファイルの名前は「0003_expert.txt」だとしたら、
python main.py 0003_expert.txt
```

注意事項:
1、ステップ4のところで、著作権のため、テクスチャファイルをアップロードしないようにする

2、導出されたのは一時フォルダー、保存機能を追加予定がないので、使用者は自分で保存する。

# 不具合レポートあるいはご意見

[こちら](https://github.com/yp05327/PSKScoreMaker/issues)