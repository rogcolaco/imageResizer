# Image Resizer

Script python utilizado para redimensionar um conjunto de imagens para as dimensões dadas pelo usuário

## Dependências

Para funcionamento é necessário a instação da biblioteca Pillow  
[Link para a documentação](https://pillow.readthedocs.io/en/stable/)  

> Instalação utilizando o pip  
> python3 -m pip install --upgrade pip  
> python3 -m pip install --upgrade Pillow  

## Funcionamento

1. Definir as dimensões finais das imagens no arquivo data.py
2. Copiar as imagens de que serão redimensionadas na pasta "imagesToResizer"
3. Rodar o script do arquivo "reiser_folder.py"
4. Imagens redimensionadas serão copiadas para a pasta "imagesResized"

**Cuidado especial**

O nome dos arquivos não podem contem "."
