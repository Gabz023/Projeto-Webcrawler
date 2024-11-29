Relatório do Projeto: Desenvolvimento de um Web Crawler para Coleta de Preços e Produtos

1. Introdução
Este relatório apresenta o desenvolvimento de um web crawler realizado em parceria com a loja Naturimel, com o objetivo de coletar informações de preços e produtos de dois sites e organizá-los em um relatório em formato PDF. A ideia surgiu da necessidade de facilitar a pesquisa de mercado e consolidar os dados de maneira prática para uso estratégico.

2. Descrição do Problema
O projeto foi motivado pela dificuldade enfrentada por pequenas empresas em acompanhar e comparar preços de produtos em sites concorrentes de forma eficiente. Um dos desafios encontrados durante o desenvolvimento foi a presença de cookies, que dificultavam o acesso às informações necessárias. Estes mecanismos de proteção bloqueavam o rastreamento, obrigando a equipe a buscar alternativas técnicas para a coleta dos dados.

3. Metodologia

3.1 Ferramentas Utilizadas
Linguagem de Programação: Python
Bibliotecas:
requests e BeautifulSoup para coleta e parsing dos dados.
Selenium para contornar proteções relacionadas a cookies.
Reportlab para a geração do arquivo PDF.

3.2 Funcionamento do Web Crawler
Identificação dos sites de interesse: dois sites foram selecionados para a coleta de informações.
Rastreamento e extração de dados:
Foi implementada uma rotina para acessar as páginas de produtos e coletar informações como nome, preço e descrição.
Utilizamos Selenium para interagir com os sites que bloqueavam acessos devido à presença de cookies.
Processamento dos dados:
As informações coletadas foram organizadas em tabelas.
Erros ou inconsistências na coleta foram tratados para evitar dados duplicados ou inválidos.
Geração do PDF:
Os dados processados foram formatados e exportados para um arquivo PDF amigável e de fácil leitura.

3.3 Superação das Barreiras de Cookies
Para superar as barreiras impostas pelos cookies, utilizamos:

Navegação automatizada com o Selenium, simulando interações humanas.
Configuração de cabeçalhos HTTP para replicar acessos legítimos.

4. Resultados
O web crawler foi bem-sucedido em coletar informações de diversos produtos. Os dados foram apresentados em um arquivo PDF contendo tabelas organizadas por categorias. Um exemplo de saída é mostrado abaixo:

Produto	/     Preço     /   	Descrição
Mel Natural 500g   /	R$ 25,00   /	Mel 100% puro e orgânico
Geleia Real 30g    / 	R$ 18,50  /	Geleia real fresca

5. Dificuldades Enfrentadas
A maior dificuldade foi contornar os bloqueios gerados pelos cookies. Inicialmente, a tentativa de usar apenas a biblioteca requests resultava em páginas incompletas ou bloqueadas. A solução foi integrar o Selenium para simular a navegação e aceitar os cookies de forma automatizada, garantindo o acesso às informações.

6. Conclusão
O projeto atingiu seus objetivos ao desenvolver uma ferramenta funcional para a coleta de preços e produtos, contribuindo para a análise de mercado da loja Naturimel. Apesar dos desafios técnicos, o aprendizado e a experiência adquiridos foram significativos. Como melhoria futura, pretendemos otimizar o código para reduzir o tempo de execução e expandir o número de sites suportados.

7. Referências
Documentação da biblioteca Selenium: https://selenium.dev
Documentação da biblioteca Reportlab: https://www.reportlab.com/
Link para o Pitch: https://youtu.be/CPcrjVVuoA0
