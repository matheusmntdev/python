import requests


class APIClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self, limit=5):
        """Obtém uma lista de posts, limitada pelo parâmetro 'limit'."""
        url = f"{self.base_url}/posts"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json()[:limit]  # Retorna apenas os primeiros 'limit' posts
            else:
                print(f"Erro ao buscar posts: Status code {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Erro de conexão ao buscar posts: {e}")
            return []

    def get_comments(self, post_id):
        """Obtém os comentários associados a um post específico."""
        url = f"{self.base_url}/comments?postId={post_id}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro ao buscar comentários: Status code {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Erro de conexão ao buscar comentários: {e}")
            return []
