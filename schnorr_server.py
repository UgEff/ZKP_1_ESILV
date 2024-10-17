from flask import Flask, jsonify, request
from hashlib import sha256
from random import randint
from Crypto.Util.number import getPrime

# Initialisation de l'application Flask
app = Flask(__name__)

# Générer un grand nombre premier p
p = getPrime(512)
g = 2  # Générateur
x = randint(1, p - 1)  # Clé privée
y = pow(g, x, p)  # Clé publique y = g^x mod p

@app.route('/schnorr-proof', methods=['GET'])
def schnorr_proof():
    """
    Générer une preuve Schnorr pour l'exposant secret `x`.
    Retourner la preuve sous forme d'un objet JSON.
    """
    # Générer un nonce aléatoire k
    k = randint(1, p - 1)
    # Calculer l'engagement r = g^k mod p
    r = pow(g, k, p)

    # Calculer le défi e en hachant l'engagement r
    e = int(sha256(str(r).encode()).hexdigest(), 16)

    # Calculer la réponse s = k - e * x mod (p - 1)
    s = (k - e * x) % (p - 1)

    # Retourner la preuve (r, e, s)
    proof = {
        'r': r,
        'e': e,
        's': s,
        'y': y,  # Clé publique
        'g': g,  # Générateur
        'p': p,  # Module premier
    }

    return jsonify(proof)

def verify_proof(y, r, e, s, g, p):
    """
    Vérifier une preuve Schnorr.
    Vérifie si g^s mod p = (r * y^e) mod p.
    """
    lhs = pow(g, s, p)  # g^s mod p
    rhs = (r * pow(y, e, p)) % p  # (r * y^e) mod p
    
    return lhs == rhs

@app.route('/verify-proof', methods=['POST'])
def verify_schnorr_proof():
    """
    Vérifier la preuve Schnorr fournie par l'utilisateur.
    Expects JSON with fields: 'r', 'e', 's', 'y', 'g', 'p'.
    """
    data = request.get_json()
    r = data['r']
    e = data['e']
    s = data['s']
    y = data['y']
    g = data['g']
    p = data['p']

    # Vérification de la preuve
    verif = verify_proof(y, r, e, s, g, p)
    result = {
        'valid': verif,
        'message': 'La preuve est valide' if verif else 'La preuve est invalide'
    }

    return jsonify(result)

@app.route('/')
def home():
    return "Schnorr Proof Server - Query /schnorr-proof to get a Schnorr proof or /verify-proof to verify a proof"

if __name__ == '__main__':
    # Démarrer le serveur Flask
    app.run(host='0.0.0.0', port=5000)
