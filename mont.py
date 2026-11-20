import sys
from PIL import Image
ids=[int(x) for x in sys.argv[2].split(',')];pre=sys.argv[1]
ims=[]
for i in ids:
    for v in 'ab':ims.append(Image.open(f'test/shots/{pre}-{i}{v}.png').resize((195,210)))
cols=6;rows=(len(ims)+cols-1)//cols
W=Image.new('RGB',(195*cols,210*rows))
for k,im in enumerate(ims):W.paste(im,((k%cols)*195,(k//cols)*210))
W.save(sys.argv[3])
