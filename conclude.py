import csv
import numpy as np
from imageio import imread, imsave

data_dir = './Percep_all/'
# get answer
csv_reader_1 = csv.reader(open('Book1.csv', encoding='utf-8-sig'), delimiter=',')
line_count = 0
answer = {}
for row in csv_reader_1:
    if line_count == 0:
        index = row
    elif line_count == 1:
        coln_count = 0
        for column in row:
            answer[index[coln_count]] = [int(column)]
            coln_count += 1
    else:
        coln_count = 0
        for column in row:
            answer[index[coln_count]].append(int(column))
            coln_count += 1
    line_count += 1

# get input index
csv_reader_2 = csv.reader(open('Book2.csv', encoding='utf-8-sig'), delimiter=',')
line_count = 0
for row in csv_reader_2:
    if line_count == 0:
        index_name = row
    elif line_count == 1:
        input_name = row
    line_count += 1

choice = 1
for i in answer:
    key = int(i.split('_')[-1])
    value = np.argwhere(answer[i] == np.amax(answer[i])).flatten().tolist()
    # 'Input.image_1_url_47'
    pick_images = []
    outputs = []
    marks = []
    for j in range(10):
        if j == 0:
            img_name = 'Input.image_%s_url_%s'%('in',str(key))
        else:
            img_name = 'Input.image_%s_url_%s'%(str(j),str(key))
        img_name = data_dir + input_name[index_name.index(img_name)].split('/')[-1].split('?')[0]
        print(key, ':', img_name)
        img = imread(img_name)
        # mark
        if j-1 in value:
            marks.append(np.full(img.shape, 255))
        else:
            marks.append(np.full(img.shape, 0))
        outputs.append(img)
    print('-------------')
    img1 = np.concatenate(outputs, axis = 1)
    img2 = np.concatenate(marks, axis = 1)
    img = np.concatenate([img1, img2], axis = 0)

    imsave("results/%s.jpg"%key, img)
    choice += 1
