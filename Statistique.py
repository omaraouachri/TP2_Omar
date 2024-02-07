from collections import Counter

def calculer_statistiques(data):
    # Initialiser les variables de statistiques
    total_tokens = 0
    num_documents = len(data)
    num_tokens_title = 0
    num_tokens_content = 0
    most_common_tokens = []

    # Parcourir les documents
    for document in data:
        # Extraire le titre et le contenu
        title = document['title']
        content = document['content']

        # Tokenizer le titre et le contenu
        title_tokens = title.lower().split()
        content_tokens = content.lower().split()

        # Mettre à jour le nombre total de tokens dans les titres et le contenu
        num_tokens_title += len(title_tokens)
        num_tokens_content += len(content_tokens)

        # Ajouter les tokens du titre et du contenu au total des tokens
        total_tokens += len(title_tokens) + len(content_tokens)

        # Compter la fréquence des tokens dans le contenu
        content_token_counter = Counter(content_tokens)

        # Extraire les 5 tokens les plus fréquents
        most_common_tokens.extend(content_token_counter.most_common(5))

    # Extraire les 5 tokens les plus fréquents
    most_common_tokens = [token for token, _ in Counter(dict(most_common_tokens)).most_common(5)]

    # Calculer la moyenne des tokens par document
    average_tokens_per_document = total_tokens / num_documents

    # Créer un dictionnaire de statistiques
    statistiques = {
        "num_documents": num_documents,
        "total_tokens": total_tokens,
        "num_tokens_title": num_tokens_title,
        "num_tokens_content": num_tokens_content,
        "average_tokens_per_document": average_tokens_per_document,
        "most_common_tokens": most_common_tokens
    }

    return statistiques
