# WebII_Formula_Bhaskara

## Resumo
Este projeto consiste em uma aplicação web desenvolvida com Flask para o cálculo das raízes reais de uma equação do segundo grau no formato $ax^2 + bx + c = 0$, utilizando o método de Bhaskara. A proposta integra conceitos matemáticos e fundamentos de desenvolvimento web, com interface simples para entrada de coeficientes e apresentação dos resultados.

## Objetivo
Implementar uma solução didática que permita:
1. Receber os coeficientes $a$, $b$ e $c$ via formulário web.
2. Calcular o discriminante ($\Delta$).
3. Determinar e exibir a natureza das raízes reais da equação.
4. Gerar o gráfico da função quadrática.
5. Salvar o histórico dos cálculos.

## Fundamentação Teórica
Para uma equação quadrática, o discriminante é dado por:

$$
\Delta = b^2 - 4ac
$$

Com base no valor de $\Delta$:
1. Se $\Delta < 0$, não existem raízes reais.
2. Se $\Delta = 0$, existe uma raiz real dupla:

$$
x = \frac{-b}{2a}
$$

3. Se $\Delta > 0$, existem duas raízes reais distintas:

$$
x_1 = \frac{-b + \sqrt{\Delta}}{2a}, \quad x_2 = \frac{-b - \sqrt{\Delta}}{2a}
$$

## Estrutura do Projeto
O projeto está organizado nos seguintes arquivos:
1. app.py: implementa o servidor Flask, o processamento dos dados e a lógica do cálculo.
2. templates/index.html: define a interface para entrada dos coeficientes e exibição dos resultados.
3. static/: armazena o gráfico gerado pela aplicação.
4. historico.json: guarda o histórico dos cálculos.
5. README.md: documentação do projeto.

## Tecnologias Utilizadas
1. Python 3
2. Flask
3. NumPy
4. Matplotlib
5. HTML5
6. Pico CSS (via CDN)

## Procedimento de Execução
1. Instalar dependências:

```bash
pip install flask numpy matplotlib
```

2. Executar a aplicação:

```bash
python app.py
```

3. Acessar no navegador:

```text
http://127.0.0.1:5000/
```

## Validação e Tratamento de Erros
A aplicação contempla tratamento básico para:
1. Entradas inválidas não numéricas.
2. Exibição de mensagens de erro em caso de exceções inesperadas.
3. Persistência do histórico em arquivo JSON.

## Limitações
1. O caso $a = 0$ não está tratado explicitamente, podendo gerar comportamento inadequado para equações não quadráticas.
2. O sistema contempla apenas raízes reais.

## Conclusão
O projeto atende ao propósito acadêmico de aplicar a fórmula de Bhaskara em um contexto de aplicação web, promovendo a integração entre lógica matemática, validação de entrada e renderização dinâmica de resultados.