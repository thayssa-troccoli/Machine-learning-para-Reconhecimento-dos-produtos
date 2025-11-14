import numpy as np
import os
import pandas as pd
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

model = load_model('product_recognition_model.h5')

class_names = {
    0: 'Ariel Expert Líquido',
    1: 'Brilhante Limpeza Total Líquido',
    2: 'Omo Lavagem perfeita - Líquido',
    3: 'Omo Lavagem perfeita - Pó',
    4: 'Omo Ultra Power Líquido'
}

def predict_product(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions[0])
    return class_names[class_idx]

def predict_directory(directory_path, output_excel):
    results = []
    for img_name in os.listdir(directory_path):
        if img_name.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(directory_path, img_name)
            product_name = predict_product(img_path)
            results.append([img_name, product_name])

    df = pd.DataFrame(results, columns=['Nome da Foto', 'Produto'])

    df.to_excel(output_excel, index=False)

directory_path = 'C:/Users/Thayssa Brock/Desktop/Nike/PANTRY CHECK-20240613T150851Z-001/PANTRY CHECK/Terezinha'  # Substitua pelo caminho do seu diretório de imagens
output_excel = 'predictions.xlsx'  

predict_directory(directory_path, output_excel)

print(f'Resultados salvos em {output_excel}')
