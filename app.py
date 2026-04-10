from flask import Flask, request, jsonify

# Importando sua lógica
from numeros import decimal_a_binario, decimal_a_octal, decimal_a_hexadecimal
from conversor_monetario import converter, listar_moedas, obter_taxa
from temperatura import TemperatureConverter

app = Flask(__name__)
# O erro da temperatura acontecia porque faltava instanciar a classe!
temp_conv = TemperatureConverter()

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API de Conversão Ativa!",
        "rotas_disponiveis": [
            "/numeros?n=10",
            "/moedas",
            "/converter?valor=100&origem=USD&destino=BRL",
            "/temperatura?valor=32&unidade=C"
        ]
    })

@app.route("/numeros")
def rota_numeros():
    n = request.args.get("n", 10, type=int) # Se não passar 'n', assume 10
    return jsonify({
        "original": n,
        "binario": decimal_a_binario(n),
        "octal": decimal_a_octal(n),
        "hexadecimal": decimal_a_hexadecimal(n)
    })

@app.route("/moedas")
def rota_moedas():
    return jsonify({"suportadas": listar_moedas()})

@app.route("/converter")
def rota_converter():
    v = request.args.get("valor", 1.0, type=float)
    o = request.args.get("origem", "USD").upper()
    d = request.args.get("destino", "BRL").upper()
    try:
        return jsonify({
            "resultado": converter(v, o, d),
            "taxa_aplicada": obter_taxa(o, d)
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@app.route("/temperatura")
def rota_temperatura():
    try:
        v = request.args.get("valor", 0.0, type=float)
        u = request.args.get("unidade", "C").upper()
        
        # Agora chamando os métodos da classe corretamente
        if u == "C":
            res = {"K": temp_conv.celsius_to_kelvin(v), "F": temp_conv.celsius_to_fahrenheit(v)}
        elif u == "F":
            res = {"C": temp_conv.fahrenheit_to_celsius(v)}
        elif u == "K":
            res = {"C": temp_conv.kelvin_to_celsius(v)}
        else:
            return jsonify({"erro": "Use unidade C, F ou K"}), 400
            
        return jsonify({"entrada": v, "unidade": u, "conversoes": res})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400