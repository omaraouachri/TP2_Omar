import json
from Build_index import inverted_index, positional_index
from Statistique import calculer_statistiques
if __name__ == "__main__":
    # Charger les docs depuis le fichier JSON
    with open('crawled_urls.json', 'r') as file:
        documents = json.load(file)

    # Construire les index :
    index_inverse= inverted_index(documents)
    index_pos = positional_index(documents)
    index_stemmer=inverted_index(documents, use_stemmer=True)
    # Calculer les statistiques
    statistics = calculer_statistiques(documents)

    # Écrire les statistiques dans metadata.json
    with open('metadata.json', 'w') as metadata_file:
        json.dump(statistics, metadata_file, indent=4)

    # Écrire l'index inversé dans title.non_pos_index.json
    with open('title.non_pos_index.json', 'w') as index_file:
        json.dump(index_inverse, index_file, indent=4)
    
    # Écrire l'index stemmer dans un fichier

    with open('mon_stemmer.title.non_pos_index.json', 'w') as index_file:
        json.dump(index_stemmer, index_file, indent=4)

    # Écrire l'index positionnel dans un fichier

    with open('title.pos_index.json', 'w') as index_file:
        json.dump(index_pos, index_file, indent=4)