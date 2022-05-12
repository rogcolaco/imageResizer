from PIL import Image
from os import listdir, remove
from os.path import isfile, join

import data
import glob
import math

# ./venv/Scripts/python resizer_folder.py

def getProporcionFile(file):
    proporcion = file.height/file.width
    return proporcion

def getProporcion(newSize, oldSize):
    proporcion = newSize/oldSize
    return proporcion

def getGap(file, sizeX, sizeY):
    gap = math.trunc((sizeY-img.height)/2) if (file.width == sizeX) else math.trunc((sizeX-img.width)/2)
    return gap

def recicle_outputfolder(outputfolder):
    old_files_resized = glob.glob(outputfolder+'/*.*')

    for trash in old_files_resized:
        try:
            remove(trash)
        except OSError as e:
            print(f'Error:{e.strerror}')
            return False
    
    return True

    

#largura desejada da imagem
sizeX = data.sizeX
#altura desejada da imagem
sizeY = data.sizeY

print('Folder imagesResized recicled.\n') if recicle_outputfolder(data.outputFolder) else print('Verifique os dados de acesso à pasta')
 
images = glob.glob(data.inputFolder +'/*.*')

onlyFiles = [f for f in listdir(data.inputFolder) if isfile(join(data.inputFolder, f))]
onlyFilesName=[]

for f in onlyFiles:
    splitedName = f.split('.')[0]
    onlyFilesName.append(splitedName)

indexFile=0

print(f'selected size:\n' +
      f'Altura: {sizeX}\n' +
      f'Largura: {sizeY}\n')

try:
    for image in images:
        
        with open(image,'rb') as file:
            img=Image.open(file)
            proporcion = getProporcionFile(img)

            resizedProporcion = getProporcion(sizeX, img.width)
            newHeigth = img.height * resizedProporcion
            if (newHeigth < sizeY):
                img = img.resize( (sizeX, math.trunc( newHeigth ) ), Image.ANTIALIAS)
            else:
                resizedProporcion = getProporcion(sizeY, img.height)
                newWidth = img.width * resizedProporcion
                img = img.resize( ( math.trunc( newWidth ), sizeY), Image.ANTIALIAS)
            
            
            gap = getGap(img, sizeX, sizeY)
            newImage = Image.new('RGBA', (sizeX, sizeY) , color = (0,0,0,0))
            newImage.paste(img, (0, gap)) if (img.width == sizeX) else newImage.paste(img, (gap, 0))

            onlyFilesName[indexFile] = onlyFilesName[indexFile].replace(' ','_')
            newImage.save(data.outputFolder+'/'+onlyFilesName[indexFile]+'.png',format='png')
            print(f'{onlyFilesName[indexFile]} was resized')

        indexFile += 1

    print('\nImagens Redimensionadas com Sucesso!')

except:
    print('\nFALHA AO REDIMENDIONAR IMAGENS!')
