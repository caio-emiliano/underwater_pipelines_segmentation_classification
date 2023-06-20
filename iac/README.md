# IaC - Infraestrutura como Código

Este diretório contém os arquivos e definições necessários para provisionar e configurar a infraestrutura na AWS para o projeto de segmentação e clusterização de anomalias em oleodutos subaquáticos.

## Arquivo serverless.yml

O arquivo `serverless.yml` contém a definição do serviço serverless que pode ser utilizado para implantar e gerenciar a infraestrutura do projeto. Ele usa a estrutura do Serverless Framework para facilitar a implantação e configuração dos recursos na AWS.

## Pasta resources

A pasta `resources` contém as definições de recursos para subir uma instância EC2 na AWS. Esses recursos são fornecidos como um exemplo para reproduzir o projeto em um ambiente diferente, usando um banco de dados alternativo.

Os arquivos na pasta `resources` incluem:

- `ec2.yaml`: um arquivo de modelo CloudFormation que define a configuração da instância EC2, como tipo de instância, tamanho do disco, grupo de segurança, etc.
- Outros arquivos e scripts relevantes para a configuração e personalização da instância EC2.

## Uso

Para implantar a infraestrutura na AWS utilizando o Serverless Framework, siga as etapas abaixo:

1. Certifique-se de ter as credenciais corretas da AWS configuradas localmente.

2. Acesse a pasta `IaC` neste repositório.

3. No terminal, execute o seguinte comando para implantar a infraestrutura:

   ```shell
   serverless deploy
   ```

   Esse comando usará as definições do arquivo `serverless.yml` para criar e configurar os recursos na AWS.

4. Após a conclusão bem-sucedida do comando, você poderá acessar os recursos provisionados na AWS.

> Nota: Lembre-se de que as imagens utilizadas no projeto são confidenciais e não estão incluídas neste repositório. Caso deseje reproduzir o projeto com seu próprio banco de dados, certifique-se de substituir as imagens de exemplo pelos dados apropriados.

Certifique-se de seguir as práticas recomendadas de segurança e gerenciamento de recursos ao implantar e usar a infraestrutura definida neste diretório.

## Recursos adicionais

- Documentação do Serverless Framework: [https://www.serverless.com/framework/docs/](https://www.serverless.com/framework/docs/)
- Documentação da AWS: [https://aws.amazon.com/documentation/](https://aws.amazon.com/documentation/)

## Autores

- [Caio Emiliano Rodrigues](caio_emiliano@hotmail.com)
- [Marcus Vinicius Rosa de Oliveira](marcusrosa.14@hotmail.com)