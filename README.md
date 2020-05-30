<h1>Avaliação de desempenho</h1>

As APIs em Python e NodeJS foram criadas para avaliação de desempenho entre as duas linguagens.

Os códigos foram criados de modo que seus retornos sejam o mais semelhantes possível.

Para execução dos containers em docker é preciso realizar a instalação do docker primeiramente.

Próximo passo é realizar o download do repositorio e acessar a pasta da API desejada para execução.

Dentro de cada API existe um arquivo .sh para compilar e rodar o projeto. Para isso execute o seguinte comando:
    bash execute.sh

Para realização do teste, rodamos separadamente cada API, para ter certeza de que as aplicações não utilizaram os recursos da VM simultaneamente.

Quando desejar para a execução de um container, execute: 
    docker stop <nameContainer>


Para realização dos teste de envio de requisições, foi utilizado o Apache JMeter, o projeto está no repositório.

Importante no JMeter, habilitar somente o teste desejado enviar, deixar todos habilitados todos os testes serão enviados simultaneamente.
