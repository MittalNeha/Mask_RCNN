from pycocotools.coco import COCO
import os
import numpy as np
from PIL import Image

from matplotlib import pyplot as plt
# %matplotlib inline


# coco = COCO("train.json")
coco = COCO("labels_my-project-name_2022-10-11-12-39-12.json")
img_dir = "../dataset_images"

list_img = os.listdir(img_dir)

for item in list(coco.imgs.values()):
    img_name = item['file_name']
    print(img_name)
    img_id = item['id']
    img = item

    image = np.array(Image.open(os.path.join(img_dir, item['file_name'])))
    # plt.imshow(image, interpolation='nearest')
    # plt.show()

    cat_ids = coco.getCatIds()
    anns_ids = coco.getAnnIds(imgIds=img_id, catIds=cat_ids, iscrowd=None)
    anns = coco.loadAnns(anns_ids)

    print(len(anns))
    mask = coco.annToMask(anns[0])
    for i in range(len(anns)):
        if anns[i]['category_id'] == 1:
            mask += (coco.annToMask(anns[i]) * 255)
        else:
            mask += (coco.annToMask(anns[i]) * 128)

    plt.imshow(mask, cmap='gray', vmin=0, vmax=255)
