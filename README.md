# PantryCheck — Classificação Automática de Fotos com Machine Learning
Este projeto foi desenvolvido para automatizar e acelerar o processo de conferência de fotos do Pantry Check em estudos de pesquisa de mercado.
Antes da automação, a conferência era feita foto por foto, verificando manualmente qual produto aparecia na imagem e depois cruzando com a resposta do questionário — um processo que podia levar até 4 horas por projeto.

Com este script de Machine Learning, a classificação passou a ser quase instantânea, reduzindo drasticamente o tempo de validação e aumentando a precisão.

🚀 Objetivo do Projeto
O objetivo foi criar um modelo capaz de:

🔍 Classificar automaticamente os produtos presentes nas fotos enviadas pelos participantes.
📝 Gerar uma lista estruturada com o nome do arquivo e o produto detectado.
🧪 Apoiar a auditoria do PantryCheck, facilitando a comparação entre fotos e respostas do questionário.

Este projeto trouxe uma automação decisiva em um processo antes repetitivo e altamente manual.

🏗️ Como Funciona
- O modelo de Machine Learning é treinado com imagens dos produtos utilizados no estudo.
- As fotos do PantryCheck são carregadas e processadas.
- O modelo identifica o produto e devolve uma lista pronta para conferência.
- O resultado final é exportado com o nome do arquivo + produto identificado.

⚠️ Sobre as Imagens

As fotos usadas neste repositório foram editadas para remover rostos, garantindo privacidade dos participantes e adequação às normas de pesquisa.
O modelo foi treinado apenas para fins de demonstração, sem uso de dados sensíveis.

🛠️ Tecnologias Utilizadas
- Python 3.x
- Bibliotecas de Machine Learning e Deep Learning
- TensorFlow — framework principal usado para criar, treinar e salvar o modelo.
- Keras (dentro do TensorFlow) — API usada para construir a rede neural (Sequential, Layers, Optimizers, Data Augmentation).

🛠️ Processamento de Imagens

- ImageDataGenerator (TensorFlow/Keras) — para:
- Data augmentation (zoom, shear, rotation, brightness shift)
- Normalização das imagens (rescale)
- Criação automática de batches
- Carregamento das imagens ou diretórios
