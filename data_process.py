import demo2
from utils import *

def runtime(dictionary_path):
    document = {}
    corners = extract_corner_from_ad_unit_json(os.path.join(dictionary_path,'ad_units.json'))
    dictionary_path = os.path.join(dictionary_path,'Frames')
    seqs = 2500
    img1s = []
    img2s = []
    kp1s = []
    kp2s = []
    for i in range(0,seqs-1):
            image1_path = os.path.join(generator_image_path_on_image_number(dictionary_path,str(i),'','.jpg'))
            image2_path = os.path.join(generator_image_path_on_image_number(dictionary_path,str(i+1),'','.jpg'))
            img1,img2,kp1,kp2 = demo2.Detect_process(image1_path,image2_path)
            img1s.append(img1)
            img2s.append(img2)
            kp1s.append(kp1)
            kp2s.append(kp2)
            print(i)
    img1s = np.asarray(img1s)
    img2s = np.asarray(img2s)
    kp1s = np.asarray(kp1s)
    kp2s = np.asarray(kp2s)
    np.save('img1s.npy', img1s)
    np.save('img2s.npy', img2s)
    np.save('kp1s.npy', kp1s)
    np.save('kp2s.npy', kp2s)
    """img1s = np.load('img1s.npy')
    kp1s = np.load('kp1s.npy')"""
    #demo2.Detect_result_based_on_corner(img1s,img2s,kp1s,kp2s,corners,seqs)


    
runtime(r'./vedios')
