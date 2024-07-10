# Nuino Button

Nuino Button [https://nuino-button.vercel.app](https://nuino-button.vercel.app/)

Related Links:
* [Kohaku Nuino's Youtube channel](https://www.youtube.com/channel/UCF4KiwafRPMgvnfipsk1JZg)
* [Kohaku Nuino's Twitter](https://twitter.com/Kohaku_Nuino)

# Requirements
Flask>=3.0.2  
dominate>=2.9.1

## Installation

`pip install flask`  
`pip install dominate`

# Usage
Clone all the documents to local.
This document is built using Python Flask. You can deploy the code to any supported platform, such as Vercel.  
If you're using Vercel to build the website, you only need to deploy the entire document to Vercel.

download this source code:[Nuino-button](https://github.com/Ymkznn/Nuino-button/archive/refs/heads/main.zip)  

1.Modify all the data in [description.json](https://github.com/Ymkznn/Nuino-button/blob/main/description.json).  
Here is the example:  
```
{
    "description":"ぬいのボタン; 心羽白ぬいの; nuino kohaku; vtuber button",
    "site-title":"ぬいのボタン",
    "title":"ぬいのボタン NUINO_BUTTON",
    "offcanvas-title":"ぬいのボタン",
    "default-lang":"日本語",
    "lang":{
        "ja":"日本語",
        "zh_TW":"繁體中文"
    },
    "allow-volume-setting":true,
    "volume-setting":"音量",
    "voice_pause":"前の音声再生を停止",
    "links":{
        "Youtube":["Youtube","https://www.youtube.com/channel/UCF4KiwafRPMgvnfipsk1JZg"],
        "Twitter":["Twitter","https://twitter.com/Kohaku_Nuino"],
        "UNiVIRTUAL":["UNiVIRTUAL","https://univirtual.jp/"],
        "Unofficial_wiki":["非公式wiki","https://seesaawiki.jp/univirtual_fan/d/%bf%b4%b1%a9%c7%f2%a4%cc%a4%a4%a4%ce"]
    },
    "footer_left":"サイト制作：やまかぜ\n音声編集/協力のぬいぐる民さん（敬称略）：ARI、MIHARU、しょー、ただの通りすがり、ひらきょん、ふっく～、ヤナギ、梅",
    "source":{
        "google_form":["音声投稿","https://forms.gle/xYhMXtFcwTdLw8hJ7"],
        "github":["github","https://github.com/Ymkznn/Nuino-button"]
    },
    "declaration":"このサイトはファン作品であり、公式とは関係ありません"
}
```  
"lang" can be added/remove like: "en":"english", so as "links","source".
also can be empty.


2.Modify the categories in [data.json](https://github.com/Ymkznn/Nuino-button/blob/main/data.json).  
Here is the example:  
```
{
    "かわいい": [],
    "うまい": [],
    "病み": [],
    "奇声": [],
    "名言": [],
    "モノマネ": [],
    "その他": []
}
```

3.run main.py

4.use [develope.py](https://github.com/Ymkznn/Nuino-button/blob/main/develope.py) to set/delete button or change button's voice.  
Here is the example:  
put your audio file into [](https://github.com/Ymkznn/Nuino-button/blob/main/develope.py)
create `example.py`  
```
import develope

develope.add_audio('category','button_name.mp3')                    # create button, mp3 file name will be used on button (delete_mp3=True to delete mp3 file after create button).
develope.del_audio('category','button_name')                        # delete button.
develope.change_audio('category','button_name','new_audio.mp3')     # change button's audio file, it will not change button name (delete_mp3=True to delete mp3 file after create button).
init_lang_file()                                                    # initial translate files (language=None,replace=False) language=None for init all language.json, replace true to renew all content.

# example
develope.add_audio('category','button_name.mp3',delete_mp3=True) 
```  

5.just F5 and see the change

You can freely change the website's color scheme or form in [static/css/style.css.](https://github.com/Ymkznn/Nuino-button/blob/main/static/css/style.css)
