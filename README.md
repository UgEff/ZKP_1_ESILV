2.BUILD SERVEUR

Explication du code :
Paramètres du protocole Schnorr :

𝑝 : Un grand nombre premier (512 bits) qui sera notre module.
𝑔: Le générateur.
𝑥: La clé privée que l'on definie choisie aléatoirement.
𝑦=𝑔**𝑥 mod 𝑝 : La clé publique dérivée de la clé privée.


Preuve de Schnorr :

𝑘: Nonce aléatoire généré à chaque requête.
𝑟=𝑔**𝑘 mod 𝑝 : Engagement calculé à partir du nonce.
𝑒: Défi calculé en hachant l'engagement 𝑟 (via la fonction SHA-256).
𝑠=𝑘+𝑒⋅𝑥 mod (𝑝−1): Réponse combinant le nonce, le défi et la clé privée.
