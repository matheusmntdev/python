import requests


def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()[:5]  # Retorna apenas os primeiros 5 posts
        else:
            print(f"Erro ao buscar posts: Status code {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Erro de conexão ao buscar posts: {e}")
        return []


def get_comments(post_id):
    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
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


def main():
    # Listar os primeiros 5 posts (diferencial opcional)
    print("Lista dos primeiros 5 posts disponíveis:")
    posts = get_posts()
    if posts:
        for post in posts:
            print(f"ID: {post['id']} | Título: {post['title']}")
    else:
        print("Não foi possível listar os posts. Você pode tentar inserir um ID entre 1 e 100.")

    # Solicita o ID do post
    post_id = input("\nDigite o ID do post (1 a 100) para ver os comentários: ")
    try:
        post_id = int(post_id)
        if not 1 <= post_id <= 100:
            print("ID inválido. Use um número entre 1 e 100.")
            return
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    # Obtém e exibe os comentários
    comments = get_comments(post_id)
    if not comments:
        print(f"Nenhum comentário encontrado para o post ID {post_id}.")
        return

    print(f"\nComentários do Post ID {post_id}:")
    for comment in comments:
        print(f"\nNome: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Comentário: {comment['body']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
