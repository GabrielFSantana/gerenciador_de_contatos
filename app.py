from flask import Flask, request, jsonify, render_template, send_file
import json
import os

app = Flask(__name__)

ARQUIVO_CONTATOS = "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, "r") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w") as arquivo:
        json.dump(contatos, arquivo, indent=4)

@app.route("/")
def home():
    contatos = carregar_contatos()
    return render_template("index.html", contatos=contatos)

@app.route("/adicionar", methods=["POST"])
def adicionar_contato():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    email = request.form.get("email")
    
    if not nome or not telefone or not email:
        return jsonify({"erro": "Todos os campos devem ser preenchidos!"}), 400
    
    contatos = carregar_contatos()
    if nome in contatos:
        return jsonify({"erro": "Contato já existe!"}), 400
    
    contatos[nome] = {"telefone": telefone, "email": email}
    salvar_contatos(contatos)
    return jsonify({"mensagem": f"Contato {nome} adicionado com sucesso!"})

@app.route("/deletar/<nome>", methods=["POST"])
def deletar_contato(nome):
    contatos = carregar_contatos()
    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
        return jsonify({"mensagem": f"Contato {nome} deletado com sucesso!"})
    return jsonify({"erro": "Contato não encontrado!"}), 404

# CAMPO PARA REALIZAR O DOWNLOAD DO ARQUIVO
@app.route("/download")
def download_json():
    if os.path.exists(ARQUIVO_CONTATOS):
        return send_file(ARQUIVO_CONTATOS, as_attachment=True)
    return jsonify({"erro": "Arquivo de contatos não encontrado!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
