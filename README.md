# 🐱 CATG – NFT Ghibli Cats Collection

Ce projet est une collection de NFTs représentant différentes races de chats illustrées dans un style inspiré des studios Ghibli. Il s'appuie sur le standard **ERC-721**, en liant chaque NFT à un fichier JSON immuable et une image correspondante, tous deux hébergés sur GitHub.

---

## 🎯 Objectif

- Générer des images de chats avec une IA (style Ghibli)
- Hasher chaque image (SHA-256) et la renommer avec ce hash
- Créer un fichier JSON contenant les métadonnées du NFT avec l’URL de l’image
- Hasher le fichier JSON et le renommer avec ce hash
- Développer un smart contract ERC-721 permettant de minter des NFTs avec le hash JSON comme identifiant (`tokenId`)
- Héberger les images et métadonnées sur GitHub

---

## 📂 Structure du projet

```
CATG/
├── images/           # Contient les images .png nommées avec leur hash SHA-256
├── metadata/         # Contient les fichiers .json nommés avec leur hash SHA-256
├── CATG.sol          # Smart contract ERC-721 (mint avec tokenId défini)
└── README.md         # Ce fichier
```

---

## 🔐 Format des métadonnées JSON

Exemple :

```json
{
  "name": "British Short Hair - Ghibli Style",
  "description": "Un magnifique chat de race British Short Hair illustré dans un style inspiré du studio Ghibli.",
  "image": "https://raw.githubusercontent.com/tanito1805/CATG/main/images/<HASH_IMAGE>.png",
  "attributes": [
    { "trait_type": "Style", "value": "Ghibli" },
    { "trait_type": "Race", "value": "British Short Hair" },
    { "trait_type": "Couleur", "value": "Gris" }
  ]
}
```

---

## 🧠 Smart Contract

- Développé avec **Solidity** `^0.8.27`
- Basé sur `ERC721`, `ERC721URIStorage`, `ERC721Enumerable`, `Ownable`
- Mint avec une fonction `safeMint(address to, uint256 tokenId, string memory uri)`
- `tokenId` = hash du fichier JSON
- `tokenURI` = URL GitHub vers le fichier JSON

---

## 🚀 Déploiement

1. Compile et déploie le contrat via [Remix](https://remix.ethereum.org)
2. Utilise `safeMint()` en fournissant :
   - Adresse de réception
   - Token ID (hash JSON converti en uint256)
   - Lien vers le fichier `.json` sur GitHub
3. Visualisation du NFT sur un explorateur ou sur OpenSea (testnet)

---



---

## 📎 Auteur

Projet réalisé par **Tan Nguyen** dans le cadre d’un exercice d’intégration Web3 / NFTs avec hébergement décentralisé simulé via GitHub.
