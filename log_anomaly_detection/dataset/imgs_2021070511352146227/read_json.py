import json

f = open('sysmonitor_train.json',)
x = json.load(f)

list_of_logs = []
# print(len(x.keys()))
count =0

for i in x.keys():
    list_of_logs.append(x[i])
    count +=1
    # print(x[i][0])
    # if count == 1:
    #     break
# print(list_of_logs[0][0])
# print(len(list_of_logs))



# from gensim import utils
# import gensim.parsing.preprocessing as gsp

# filters = [
#            gsp.strip_tags, 
#            gsp.strip_punctuation,
#            gsp.strip_multiple_whitespaces,
#            gsp.strip_numeric,
#            gsp.remove_stopwords, 
#            gsp.strip_short, 
#            gsp.stem_text
#           ]

# def clean_text(s):
#     s = s.lower()
#     s = utils.to_unicode(s)
#     for f in filters:
#         s = f(s)
#     return s

f.close()