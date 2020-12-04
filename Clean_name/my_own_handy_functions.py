f# some handy functions

import pickle # pickle 包用于实现序列化和反序列化（把对象转化或翻译为文件）
import time
import sys
import json #字典模块

def pickle_dump(dict2dump, dict_name): #序列化对象
    pickle_name = dict_name + '.pickle'
    with open(pickle_name, 'wb') as handle: # with 语句是一种处理异常的方式，方便改bug，可以当作 handle=open(xxx)
        pickle.dump(dict2dump, handle, protocol = pickle.HIGHEST_PROTOCOL) 
    return pickle_name

def pickle_load(dict_name): #反序列化对象
    pickle_name = dict_name + '.pickle'
    with open(pickle_name, 'rb') as handle:
        return pickle.load(handle)
    
def show_tables(con): #连接数据库
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall()

def log_time_used(t1, task, log, mode = 'a'): #显示时长
    t2 = time.time()
    t = round(t2-t1,2)
    message = f"{task} takes {t}s."
    if log == '':
        print(message, file = sys.stdout)
    else:
        with open(log, mode) as f:
            print(message, file = f)
    return time.time()

def simple_bing_search(search_word): #bing搜索单词，记得先填好密码
    web_data_raw = client.web.search(query=search_word, raw = True, count = 50)
    raw_text = web_data_raw.response.text
    raw_dict = json.loads(raw_text)
    return raw_dict

def print_log(message, logfile = '', mode = 'a'): #打印日志
    if logfile != '':
        with open(logfile, mode) as f:
            print(message, file = f)
    else:
        print(message, file = sys.stdout)
    return None
