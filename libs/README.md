# LIBS

## Descrição

Esta pasta contém os arquivos necessários para carregar e transformar a base de dados no formato do Detectron 2, bem como as configurações da rede para treinamento e inferência.

Os hiperparâmetros configurados estão listados abaixo. Os parâmetros não listados acima permanecem como padrão.

- Número de iterações: O número total de iterações que a rede Detectron 2 irá executar durante o treinamento.
25

- Iterações warmup: O número de iterações iniciais em que o learning rate é gradualmente au- mentado para evitar instabilidades no treinamento.

- Learning rate: A taxa de aprendizado, que determina o tamanho dos ajustes feitos nos pesos da rede durante o treinamento.

- Gamma: O fator de redução aplicado ao learning rate em épocas específicas do treinamento.

- Solver steps: As épocas em que o learning rate é ajustado pelo fator Gamma durante o treina-
mento.

- Eval Period: O número de iterações entre as avaliações da rede em um conjunto de validação para monitorar seu desempenho.

- Batch size per image: O número de amostras de treinamento usadas em cada iteração de atuali- zação dos pesos da rede para uma única imagem.

- Learning Rate Scheduler Name: O nome da estratégia usada para ajustar automaticamente o learning rate durante o treinamento.

- Momentum: Um valor que controla a influência das atualizações de pesos anteriores nas atuali- zações atuais durante o treinamento

- Gradients Clip: Um valor máximo para limitar a magnitude dos gradientes durante o treina- mento, evitando explosão dos gradientes.

- Norm Type: O tipo de normalização aplicado aos gradientes durante o treinamento.
- Clip Value: Um valor máximo para limitar a magnitude dos gradientes após a normalização.

### Arquivo utils.py

O arquivo `utils.py` contém as funções responsáveis por carregar e transformar a base de dados no formato compatível com o Detectron 2. Essas funções são essenciais para preparar os dados antes de serem utilizados nos processos de treinamento e inferência.

### Arquivo train_config.py

O arquivo `train_config.py` contém as configurações da rede para o treinamento. Aqui, você pode ajustar os parâmetros relevantes, como taxa de aprendizado, número de épocas, tamanho do lote (batch size), entre outros. Essas configurações são fundamentais para obter um bom desempenho do modelo durante o treinamento.

### Arquivo test_config.py

O arquivo `test_config.py` contém as configurações da rede para a inferência. Neste arquivo, você pode definir as configurações específicas para executar a inferência no modelo treinado. Isso inclui a seleção do modelo treinado, parâmetros de pós-processamento e qualquer outra configuração relevante para obter resultados precisos e confiáveis.

## Utilização

As funções de carregamento e transformação de dados são importadas por padrão nos Notebooks de Treino e Inferência e são utilizadas de acordo com suas necessidades. O mesmo acontece com os arquivos `train_config.py` e `test_config.py`.

## Requisitos

Certifique-se de ter o Detectron 2 e todas as suas dependências instaladas corretamente em seu ambiente Python antes de utilizar os arquivos deste diretório. Você também deve ter os dados da base de dados em um arquivo CSV corretamente organizado e disponível no local "/underwater_pipelines_segmentation_classification/database".

## Referências

Caso você precise de mais informações sobre o uso do Detectron 2, consulte a documentação oficial do Detectron 2 em [link da documentação](https://detectron2.readthedocs.io).

## Autores

- [Caio Emiliano Rodrigues](caio_emiliano@hotmail.com)
- [Marcus Vinicius Rosa de Oliveira](marcusrosa.14@hotmail.com)