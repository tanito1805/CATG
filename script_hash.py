import os
import hashlib
import json

IMAGE_DIR = "./images"
METADATA_DIR = "./metadata"

# Remplace par ton vrai lien GitHub brut (raw)
IMAGE_BASE_URL = "https://raw.githubusercontent.com/tanito1805/CATG/main/images/"
METADATA_BASE_URL = "https://raw.githubusercontent.com/tanito1805/CATG/main/metadata/"

def sha256(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def rename_file_with_hash(filepath, hash_value):
    ext = os.path.splitext(filepath)[1]
    new_name = f"{hash_value}{ext}"
    new_path = os.path.join(os.path.dirname(filepath), new_name)
    os.rename(filepath, new_path)
    return new_name, new_path

def create_metadata(image_hash_filename, name, description):
    metadata = {
        "name": name,
        "description": description,
        "image": IMAGE_BASE_URL + image_hash_filename,
        "attributes": [
            {"trait_type": "Style", "value": "Ghibli"},
            {"trait_type": "OriginalOwner", "value": True}
        ]
    }
    return json.dumps(metadata, indent=2).encode("utf-8")

def save_metadata_file(json_bytes, hash_value):
    filename = f"{hash_value}.json"
    path = os.path.join(METADATA_DIR, filename)
    with open(path, "wb") as f:
        f.write(json_bytes)
    return filename

def load_ia_metadata(image_filename):
    metadata_file = f"./ia_metadata/{image_filename}.json"
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def main():
    if not os.path.exists(METADATA_DIR):
        os.makedirs(METADATA_DIR)

    for filename in os.listdir(IMAGE_DIR):
        if filename.startswith("."):
            continue
        filepath = os.path.join(IMAGE_DIR, filename)
        
        # Étape 1 : hasher et renommer l'image
        image_hash = sha256(filepath)
        image_hash_filename, new_image_path = rename_file_with_hash(filepath, image_hash)

        # Étape 2 : Récupérer nom et description de l'IA
        metadata_info = load_ia_metadata(filename)
        if metadata_info:
            name = metadata_info["name"]
            description = metadata_info["description"]
        else:
            print(f"Aucune donnée trouvée pour {filename}, skipping.")
            continue

        # Créer les métadonnées avec les informations de l'IA
        metadata_bytes = create_metadata(image_hash_filename, name, description)

        # Étape 3 : hasher les métadonnées
        metadata_hash = hashlib.sha256(metadata_bytes).hexdigest()

        # Étape 4 : sauvegarder les métadonnées avec leur hash comme nom
        metadata_filename = save_metadata_file(metadata_bytes, metadata_hash)

        print(f"Image : {image_hash_filename}")
        print(f"Metadata : {metadata_filename}")
        print(f"TokenID à utiliser : {metadata_hash}\n")

if __name__ == "__main__":
    main()
