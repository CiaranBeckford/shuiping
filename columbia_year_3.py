import codecs
import re
import dragonmapper
from dragonmapper import hanzi
from hanziconv import HanziConv

#example entry format - need for regex and stripping
#["'垮掉", "kuǎdiào to collapse, to break down\\n'"]

def init_dict():
    chinese_dict = dict()
    with codecs.open('year_1.txt', encoding='utf-8') as f:
        for line in f:
            dict_entry = re.split(r'\\t+', (repr(line)))
            if dict_entry is not None:
                chi_chars = None
                translation = None
                if hanzi.is_traditional(dict_entry[0]) is True:
                    chi_chars =  HanziConv.toSimplified(dict_entry[0])
                    translation = dict_entry[1]
                    translation = translation.split()
                    translation[-1] = str((translation)[-1][0:-3])
                    translation = " ".join(translation)
                    translation = re.sub('[^A-Za-z0-9 , () [] . / \']+', '', translation)
                    translation = translation.replace('<br>', ' - ')
                elif hanzi.is_traditional(dict_entry[1]) is True:
                    chi_chars = HanziConv.toSimplified(dict_entry[1])
                    translation = dict_entry[0]
                    translation = re.sub('[^A-Za-z0-9 , () [] . / \']+', '', translation)
                    translation = translation.replace('<br>', ' - ')
                    stripped = chi_chars.split('\\n')
                    chi_chars = stripped[0]
                chinese_dict.update({ chi_chars : (translation)})
    with codecs.open('year_2.txt', encoding='utf-8') as f:
        for line in f:
            dict_entry = re.split(r'\\t+', (repr(line)))
            if dict_entry is not None:
                chi_chars = (dict_entry[0])[1::]
                sim_trad = chi_chars.split('～')
                chi_chars = sim_trad[0]
                line_split = (dict_entry[1]).split()
                translation = line_split
                #strips \\n off end"
                translation[-1] = str((translation)[-1][0:-3])
                translation = " ".join(translation)
                translation = re.sub('[^A-Za-z0-9 , () [] . / \']+', '', translation)
                translation = translation.replace('<br>', ' - ')
                chinese_dict.update({ chi_chars : (translation)})
    with codecs.open('year_3.txt', encoding='utf-8') as f:
        for line in f:
            dict_entry = re.split(r'\\t+', (repr(line)))
            if dict_entry is not None:
                chi_chars = (dict_entry[0])[1::]
                line_split = (dict_entry[1]).split()
                translation = line_split
                #strips \\n off end"
                translation[-1] = str((translation)[-1][0:-3])
                translation = " ".join(translation)
                translation = re.sub('[^A-Za-z0-9 , () [] . / \']+', '', translation)
                chinese_dict.update({ chi_chars : (translation)})
    return chinese_dict

def check_dict(query, chinese_dict):
    if query in chinese_dict:
        return (True, (chinese_dict[query]))
    else:
        return (False, None)
