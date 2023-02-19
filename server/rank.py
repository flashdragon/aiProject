import numpy as np
import pandas as pd
import os
import random
import statistics
from sklearn.preprocessing import MinMaxScaler

def recommend(s, animal_input_path):
    path = animal_input_path
    
    file_list = os.listdir(path)
    class_list = []
    for i in range(len(file_list)):
        if file_list[i][-3:]=='jpg':
            class_list.append(file_list[i].split('_')[0])
    class_set = sorted(list(set(class_list)))

    class_cnt = pd.DataFrame(columns=['class_name','count'])
    class_name_lst = []
    class_cnt_lst = []
    for c in class_set:
        class_name_lst.append(c)
        class_cnt_lst.append(class_list.count(c))
    class_cnt['class_name']= class_name_lst
    class_cnt['count'] = class_cnt_lst

    # 개, 고양이, 곰, 알파카, 원숭이, 여우, 쥐, 말, 판다
    candidate_lst = ['dog','cat', 'alpaca', 'bear', 'fox', 'mouse', 'horse', 'panda']

    selected_name_lst = class_cnt['class_name'].values

    selected_jpg_lst = []
    selected_pts_lst = []
    label_lst = []

    for selected in candidate_lst:
        selected_jpg_lst += [i for i in file_list if selected in i and i[-3:]=='jpg' and 'africanwilddog' not in i]
        selected_pts_lst += [i for i in file_list if selected in i and i[-3:]=='npy' and 'africanwilddog' not in i]
        label_lst+= [selected for i in file_list if selected in i and i[-3:]=='npy' and 'africanwilddog' not in i]
    # 25개 동물

    data = np.array([])

    for i in selected_pts_lst:
        tmp = np.load("{}/{}".format(animal_input_path,i))
        data = np.append(data, tmp)

    data = data.reshape(-1,9,2)
    
    # x축 기준/y축 기준 normalize
    for i in range(len(data)):
        scaler = MinMaxScaler()
        scaler.fit(data[i,:])
        data[i,:] = scaler.transform(data[i,:])
    
    scaler = MinMaxScaler()
    scaler.fit(s)
    s = scaler.transform(s)

    me = s
    dist_lst = []
    for i in range(len(data)):
        dist = np.linalg.norm(me-data[i])
        dist_lst.append([i,dist])
    #     print(len(dist_lst))
    dist_lst.sort(key=lambda x: x[1])
    neighbors = np.array(dist_lst[:10])[:,0] # 10개 이웃 인덱스 추출
    
    neibor_lst = [label_lst[int(i)] for i in neighbors]
#     print(neibor_lst)
    dictionary = {string : round((neibor_lst.count(string))/10*100, 1) for string in neibor_lst}
    rank = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return rank