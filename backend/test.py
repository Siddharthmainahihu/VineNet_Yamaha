from model import *
from data import *
import time
data_gen_args=dict()
model=unet()
model.load_weights('unet_membrane.hdf5')

test_path="path to the test data folder"
files=os.listdir(test_path+'/images')
images_no=len(files)
files.sort()
testGene = testGenerator(test_path+'/images',as_gray=False)
begin=time.time()
results = model.predict_generator(testGene,images_no,verbose=1)
end=time.time()
print(end-begin,"s for 1 imgs")
saveResult("results/pred",results)
for i in range(images_no):
        img = io.imread(os.path.join(test_path+'/masks',files[i].strip('.png')+'_instanceIds.png'),as_gray = False)
        img = trans.resize(img,(256,256))
        io.imsave(os.path.join("results/gt","%d_gt.png"%i),img)