# 电影文件名识别工具 movieNameParser

## 为啥做了这个？

我有一堆命名乱七八糟的电影/电视剧需要识别，所以以 divijbindlish/parse-torrent-name 这个为原型适配了下国内常见的命名规则

## 用法

```py
from common import parse
info = parse('[现代启示录].Apocalypse.Now.2001.Remux.BluRay.720p.x264.AC3-CMCT.mkv')
print info
```

## 功能

能识别出的字段有：分辨率-resolution、年份-year、季-season、集-episode、压制来源-source、视频编解码器-codec、音频编解码器-audio、动态范围类型-dynRes、地区-region、发行版本-release、流媒体源-stream、文件大小-size、3D-3d、音频通道数-audioLangNum、音频语言-audioLang、字幕语言subLang、帧率-fps、色彩深度-bit、CD分片-cd、来源网站-website、压制小组-group

未识别出的部分会放在 excess 字段

## 备注

我是非专业人员，随便搞搞不喜勿喷
