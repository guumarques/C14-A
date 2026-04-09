from flask import Flask, request, jsonify

from numeros import decimal_a_binario, decimal_a_octal, decimal_a_hexadecimal
from conversor_monetario import converter, listar_moedas, obter_taxa

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>Conversor Universal</h1>
    <ul>
        <li><a href="/numeros">/numeros</a> — Conversão numérica (decimal → binário)</li>
        <li><a href="/moedas">/moedas</a> — Listar moedas disponíveis</li>
        <li><a href="/converter?valor=100&origem=USD&destino=BRL">/converter?valor=100&amp;origem=USD&amp;destino=BRL</a> — Converter moeda</li>
        <li><a href="/taxa?origem=USD&destino=BRL">/taxa?origem=USD&amp;destino=BRL</a> — Consultar taxa de câmbio</li>
    </ul>
    """


@app.route("/numeros")
def decimal_to_binario():
    numero = request.args.get("n", 10, type=int)
    return jsonify({
        "decimal": numero,
        "binario": decimal_a_binario(numero),
        "octal": decimal_a_octal(numero),
        "hexadecimal": decimal_a_hexadecimal(numero),
    })


@app.route("/moedas")
def moedas():
    return jsonify({"moedas_suportadas": listar_moedas()})


@app.route("/converter")
def converter_moeda():
    try:
        valor = request.args.get("valor", type=float)
        origem = request.args.get("origem", "")
        destino = request.args.get("destino", "")

        if valor is None:
            return jsonify({"erro": "Parâmetro 'valor' é obrigatório"}), 400

        resultado = converter(valor, origem, destino)
        return jsonify({
            "valor_original": valor,
            "moeda_origem": origem.upper(),
            "moeda_destino": destino.upper(),
            "valor_convertido": resultado,
            "taxa": obter_taxa(origem, destino),
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/taxa")
def taxa():
    try:
        origem = request.args.get("origem", "")
        destino = request.args.get("destino", "")
        return jsonify({
            "origem": origem.upper(),
            "destino": destino.upper(),
            "taxa": obter_taxa(origem, destino),
        })
    except KeyError as e:
        return jsonify({"erro": str(e)}), 400