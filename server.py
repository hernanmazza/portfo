from flask import Flask, render_template, request, redirect

app = Flask(__name__)
""" 
Flask busca en la carpeta templates los htms
y en la carpeta statycs los javaScrpts .js y los Estilos .css """

@app.route("/")
def ind():
    return  render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return  render_template(page_name)

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method=='POST':
        return redirect('/gracias.html')

'''
LOs de abajo son ejemplos de html templates de python con un index.htm que 
ya no existe. por lo tanto no van a andar
'''
'''
@app.route("/<usuario>")
def usuarios(usuario=None):
    ##################################-->name esta en el html y se usa para imprimir
    return render_template('index.html', name=usuario+'!!!') #render_templates busca en la carpeta templates situada en el directorio actual

@app.route("/<usuario>/<int:post_id>")
def usuarios_pos(usuario=None, post_id=None):
    ##################################-->name esta en el html y se usa para imprimir
    return render_template('index.html', name=usuario+'!!!', p_id=post_id) #render_templates busca en la carpeta templates situada en el directorio actual

@app.route("/p1")
def p1():
    return "Otra cosa"
'''