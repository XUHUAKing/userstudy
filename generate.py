from glob import glob

url_pre = "https://github.com/XUHUAKing/userstudy/blob/master/Percep_all/"
Ins_img_paths = sorted(glob('Percep_all/*M_zhang_et_al*'))
Li_img_paths = sorted(glob('Percep_all/*T_Li_et_al*'))
Arv_img_paths = sorted(glob('Percep_all/*T_ReflectSuppress*'))
CEI_img_paths = sorted(glob('Percep_all/*T_CEILNet*'))
zhang_img_paths = sorted(glob('Percep_all/*T_zhang_et_al*'))
Wei_img_paths = sorted(glob('Percep_all/*T_Wei_et_al*'))
BDN_img_paths = sorted(glob('Percep_all/*T_BDN*'))
Wen_img_paths = sorted(glob('Percep_all/*T_Wen_et_al_focused*'))
CoRRN_img_paths= sorted(glob('Percep_all/*T_CoRRN*'))
Yang_img_paths= sorted(glob('Percep_all/*T_Yang_et_al*'))

for j in range(50):
    print(url_pre+Ins_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+Li_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+Arv_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+CEI_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+zhang_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+Wei_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+BDN_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+Wen_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+CoRRN_img_paths[j].split('/')[-1]+'?raw=true')
    print(url_pre+Yang_img_paths[j].split('/')[-1]+'?raw=true')
'''
for i in range(1,51):
    print('image_in_url_%s'%(str(i)))
    print('image_1_url_%s'%(str(i)))
    print('image_2_url_%s'%(str(i)))
    print('image_3_url_%s'%(str(i)))
    print('image_4_url_%s'%(str(i)))
    print('image_5_url_%s'%(str(i)))
    print('image_6_url_%s'%(str(i)))
    print('image_7_url_%s'%(str(i)))
    print('image_8_url_%s'%(str(i)))
    print('image_9_url_%s'%(str(i)))
'''
