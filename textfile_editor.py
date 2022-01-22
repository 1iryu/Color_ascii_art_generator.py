
#write

#if txt file is not exist , this function would make it. and then write text.
def write(path: str, text):
    f = open(path, 'a')
    f.writelines(text)
    f.close()


def clear_old_text_and_write_text(path: str, text):
    f = open(path, 'x')
    f.writelines(text)
    f.close()


def write_to_unwritten_txt_file(path: str, text):
    if(is_unwritten_txt_file_or_not_exist):
        write(path, text)


def is_unwritten_txt_file_or_not_exist(path: str):
    import os.path
    if(os.path.isfile(path)):
        data = open(path, 'r').read()
        if(data == ""):
            return True
    if(os.path.isfile(path) == False):
        return True
    return False


#read
def read_txt_file(path: str):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data