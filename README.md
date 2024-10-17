# Zero-Knowledge Proofs (ZKP) - DM1

## Description
Ce projet implémente un serveur basé sur le protocole de preuve à divulgation nulle de connaissance (**Zero-Knowledge Proof**) utilisant le **Schnorr Proof**. Le serveur Flask permet de générer et de vérifier des preuves cryptographiques de manière sécurisée, sans divulguer la clé privée de l'utilisateur.

## Fonctionnalités
- **Génération de preuve Schnorr** : Le serveur génère une preuve basée sur l'exposant secret \( x \), et renvoie les valeurs \( r \), \( e \), \( s \), \( y \), \( g \), et \( p \) sous forme de JSON.
- **Vérification de la preuve Schnorr** : Le serveur vérifie la validité de la preuve en comparant \( g^s \mod p \) avec \( (r \cdot y^e) \mod p \).

## Structure du projet

```
.
├── Dockerfile            # Fichier de configuration pour créer un conteneur Docker pour le projet
├── README.md             # Documentation du projet
├── schnorr_server.py     # Serveur Flask implémentant le protocole Schnorr
├── requirement.txt       # Liste des dépendances Python
├── retour.json           # Exemple de fichier JSON de retour pour la vérification
└── tests                 # Répertoire pour les tests (optionnel)
```

## Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.x**
- **Flask** (framework web Python)
- **pycryptodome** (bibliothèque pour les opérations cryptographiques)

### Installation des dépendances

Les dépendances du projet sont listées dans le fichier `requirements.txt`. Pour les installer, utilisez la commande suivante :

```bash
pip install -r requirements.txt
```

## Exécution du projet

### 1. Lancer le serveur Flask
Pour démarrer le serveur Flask qui gère la génération et la vérification des preuves Schnorr, exécutez :

```bash
python schnorr_server.py
```

Le serveur sera accessible à l'adresse **http://127.0.0.1:5000** ou à l'adresse réseau indiquée dans le terminal.

### 2. Générer une preuve Schnorr

Pour générer une preuve, envoyez une requête **GET** à l'endpoint **/schnorr-proof** :

```bash
curl http://localhost:5000/schnorr-proof
```

Cela retournera une preuve Schnorr sous forme de JSON, avec les valeurs suivantes :
- \( r \) : L'engagement
- \( e \) : Le défi (généré à partir de \( r \))
- \( s \) : La réponse (calculée à partir de la clé privée)
- \( y \) : La clé publique
- \( g \) : Le générateur
- \( p \) : Le module premier

### 3. Vérifier une preuve Schnorr

Pour vérifier une preuve générée, envoyez une requête **POST** avec les valeurs obtenues à l'endpoint **/verify-proof** :

```bash
curl -X POST http://localhost:5000/verify-proof -H "Content-Type: application/json" -d '{"r": <valeur_r>, "e": <valeur_e>, "s": <valeur_s>, "y": <valeur_y>, "g": <valeur_g>, "p": <valeur_p>}'
```

Cela renverra un JSON indiquant si la preuve est valide ou non.

### Exemple de réponse
Si la preuve est valide :

```json
{
  "valid": true,
  "message": "La preuve est valide"
}
```

## Utilisation avec Docker

### 1. Construire l'image Docker

Pour construire l'image Docker, exécutez la commande suivante dans le répertoire du projet où se trouve le **Dockerfile** :

```bash
docker build -t schnorr-server .
```

### 2. Lancer le conteneur Docker

Une fois l'image construite, vous pouvez lancer le conteneur :

```bash
docker run -p 5000:5000 schnorr-server
```

Le serveur Flask sera maintenant accessible via **http://127.0.0.1:5000** dans votre navigateur ou avec **curl**.

## Tests

Des tests peuvent être ajoutés dans le répertoire `tests`. Vous pouvez utiliser des outils comme **pytest** pour automatiser les tests des fonctionnalités de génération et de vérification des preuves.

## Auteur
Projet développé par **Idir Guettab** dans le cadre du cours de ZeroKnowledge Proof à l'ESILV (A5).
