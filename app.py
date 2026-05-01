from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    a = None
    b = None
    c = None
    delta = None
    erro = None
    x = None
    x1 = None
    x2 = None
    grafico_url = None

    if request.method == 'POST':
        try:
            #recebendo dados
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            #gerando gráfico
            eixo_x = np.linspace(-10, 10, 100)
            eixo_y = a * eixo_x**2 + b * eixo_x + c

            plt.clf()
            plt.plot(eixo_x, eixo_y)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Gráfico da Função Quadrática')
            plt.grid(True)
            plt.savefig('static/grafico.png')
            grafico_url = 'grafico.png'
            
            #lógica do exercício
            delta = b**2 - 4*a*c
            if delta < 0:
                x = "Não há raízes reais."
            elif delta == 0:
                x = -b / (2*a)
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)

                #Arredondamentos
                x1 = round(x1, 2)
                x2 = round(x2, 2)
        
        except ValueError:
            erro = "Informação inválida, digite números válidos."
        except Exception as erro2:
            erro = f"Ocorreu um erro inesperado: {str(erro2)}"
    
    return render_template('index.html', a=a, b=b, c=c, delta=delta, x=x, x1=x1, x2=x2, erro=erro, grafico_url=grafico_url)

if __name__ == '__main__':
    app.run(debug=True)