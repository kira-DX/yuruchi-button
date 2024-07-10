import json
import os
import re

lang_path = 'static/language'
audio_path = 'static/audios'

def __read_data__(data_type):
    if data_type == 'data':
        with open('data.json','r',encoding='utf-8') as file:
            data = json.load(file)
        return data
    elif data_type == 'lang':
        lang_files = {}
        for lang_file in os.listdir(lang_path):
            with open(os.path.join(lang_path,lang_file),'r',encoding='utf-8') as file:
                lang_files[lang_file]=(json.load(file))
        return lang_files
    else:
        print('data type error.')

def __write_data__(data_type,data,lang_name=None):
    if data_type == 'data': # data:dict
        with open('data.json','w',encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    elif data_type == 'lang' and lang_name != None: # data:list[dict]
        with open(os.path.join(lang_path, lang_name),'w',encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        print('data type error.')

def __calc_filenum__(data:json,category:str,filename:str):
    index = 0
    filename = filename.split('.')[0]
    category_num = list(data.keys()).index(category)+1

    for button_name in data[category]:
        index += 1
        if filename in button_name.keys():
            return {
                'exist':True,
                'num':'{}-{:03d}'.format(category_num,index)
            }
    return {
        'exist':False,
        'num':'{}-{:03d}'.format(category_num,len(data[category])+1)
    }
def __flatten_dict__(d):
    items = []
    for k, v in d.items():
        if isinstance(v, dict):
            items.extend(__flatten_dict__(v).items())
        else:
            items.append((k, v))
    return dict(items)

def __get_keys__(d):
    keys = {}
    for index,category in enumerate(list(d.keys())):
        keys.update({'category_{}'.format(index+1):category})
        for item_index,items in enumerate(d[category]):
            for item in items.keys():
                keys.update({'{}-{:03d}'.format(index+1,item_index+1):item})
    return keys
def add_audio(category:str,filename:str,note:str=None,delete_mp3=False):
    data = __read_data__('data')
    trans = __read_data__('lang')
    button = __calc_filenum__(data,category,filename)
    filename = filename.split('.')[0]

    # add audio.mp3
    if button['exist']:
        print('This button name is already exist.')
        return
    with open('temp_audio/{}.mp3'.format(filename),'rb') as file:
        audio_file = file.read()
    with open('static/audios/{}.mp3'.format(button['num']),'wb') as file:
        file.write(audio_file)

    # update data.json
    data[category].append({filename:note})
    __write_data__('data',data)

    # update language files
    for key,values in trans.items():
        values[button['num']]=filename
        temp = sorted(values.keys(),reverse=True)
        values = {key: values[key] for key in temp}
        __write_data__('lang',values,key)

    # if need to remove orginal audio
    if delete_mp3:
        os.remove('temp_audio/{}.mp3'.format(filename))

def del_audio(category:str,filename:str):
    data = __read_data__('data')
    trans = __read_data__('lang')
    button = __calc_filenum__(data,category,filename)

    if not button['exist']:
        print('This button does not exist.')
        return
    files = [f for f in os.listdir(audio_path) if f.endswith('.mp3')]
    files.sort()
    try:
        # remove audio.mp3
        match = re.match(r"(\d+)-(\d{3})\.mp3", button['num']+'.mp3')
        category_num,number = int(match.group(1)), int(match.group(2))
        os.remove(os.path.join(audio_path, button['num']+'.mp3'))
        for filename in files:
            match = re.match(r"(\d+)-(\d{3})\.mp3", filename)
            f_type, f_number = int(match.group(1)), int(match.group(2)) # "1(f_type)-001(f_number)"
            if f_type == category_num:
                if f_number > number:
                    os.rename(
                        os.path.join(audio_path, filename), 
                        os.path.join(audio_path, '{}-{:03d}.mp3'.format(f_type,f_number-1))
                    )

        # update data.json
        del (data[category][number-1]) 
        __write_data__('data',data)

        # update language files
        for key,values in trans.items():
            try:
                del values[button['num']]
            except:
                pass

            new_lang = values.copy()

            for filename,value in values.items():
                match = re.match(r"(\d+)-(\d{3})", filename)
                try:
                    f_type, f_number = int(match.group(1)), int(match.group(2)) 
                    if f_type == category_num:
                        if f_number > number:
                            new_lang['{}-{:03d}'.format(f_type,f_number-1)]=values['{}-{:03d}'.format(f_type,f_number)]
                            del new_lang['{}-{:03d}'.format(f_type,f_number)]
                except:
                    new_lang[filename]=value
            temp = sorted(values.keys(),reverse=True)
            values = {key: values[key] for key in temp}
            __write_data__('lang',values,key)
    except:
        print('This audio file does not exist.')


def change_audio(category:str,buttonname:str,filename:str,delete_mp3=False):
    data = __read_data__('data')
    button = __calc_filenum__(data,category,buttonname)
    filename = filename.split('.')[0]
    with open('temp_audio/{}.mp3'.format(filename),'rb') as file:
        audio_file = file.read()
    with open('static/audios/{}.mp3'.format(button['num']),'wb') as file:
        file.write(audio_file)
    if delete_mp3:
        os.remove('temp_audio/{}.mp3'.format(filename))

def init_lang_file(language=None,replace=False):
    with open('description.json','r',encoding='utf-8') as file:
        description = json.load(file)
    with open('data.json','r',encoding='utf-8') as file:
        data = json.load(file)

    init_data = {}
    langs = list(description['lang'].keys())
    if language:
        langs = [language]
    
    for lang_name in langs:
        for item_index,item in __get_keys__(data).items():
            if item_index not in init_data:
                init_data[item_index] = item
        for item_index,item in __flatten_dict__(description).items():
                    if item_index not in init_data:
                        if item_index not in ['footer_left'] and isinstance(item, list):
                            init_data[item_index] = item[0]
                        else:
                            init_data[item_index] = item
        temp = sorted(init_data.keys(),reverse=True)
        init_data = {key: init_data[key] for key in temp}
        if not replace:
            original_data = __read_data__('lang')
            init_data.update(original_data[lang_name+'.json'])
            print(init_data)
        __write_data__('lang',init_data,lang_name+'.json')
