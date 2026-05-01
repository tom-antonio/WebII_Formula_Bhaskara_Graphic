from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
import os

app = Flask(__name__)
JSON_FILE = os.path.join(app.root_path, 'historico.json')


def ler_historico():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_historico(historico):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

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
    historico = ler_historico()

    if request.method == 'POST':
        try:
            # recebendo dados
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            # gerando gráfico
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
            
            # lógica do exercício
            delta = b**2 - 4*a*c
            if delta < 0:
                x = "Não há raízes reais."
            elif delta == 0:
                x = -b / (2*a)
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                x1 = round(x1, 2)
                x2 = round(x2, 2)

            registro = {
                'a': a,
                'b': b,
                'c': c,
                'delta': delta,
                'raizes': {
                    'x': x,
                    'x1': x1,
                    'x2': x2,
                }
            }
            historico.append(registro)
            salvar_historico(historico)
        
        except ValueError:
            erro = "Informação inválida, digite números válidos."
        except Exception as erro2:
            erro = f"Ocorreu um erro inesperado: {str(erro2)}"

    historico = ler_historico()
    return render_template(
        'index.html',
        a=a,
        b=b,
        c=c,
        delta=delta,
        x=x,
        x1=x1,
        x2=x2,
        erro=erro,
        grafico_url=grafico_url,
        historico=historico,
    )

if __name__ == '__main__':
    app.run(debug=True)