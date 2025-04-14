from api_client import APIClient


class CommentViewer:
    def __init__(self):
        self.client = APIClient()

    def display_posts(self):
        """Exibe os primeiros 5 posts disponíveis."""
        posts = self.client.get_posts()
        if posts:
            print("Lista dos primeiros 5 posts disponíveis:")
            for post in posts:
                print(f"ID: {post['id']} | Título: {post['title']}")
        else:
            print("Não foi possível listar os posts. Você pode tentar inserir um ID entre 1 e 100.")

    def get_post_id(self):
        """Solicita e valida o ID do post do usuário."""
        post_id = input("\nDigite o ID do post (1 a 100) para ver os comentários: ")
        try:
            post_id = int(post_id)
            if not 1 <= post_id <= 100:
                print("ID inválido. Use um número entre 1 e 100.")
                return None
            return post_id
        except ValueError:
            print("Por favor, insira um número válido.")
            return None

    def display_comments(self, post_id):
        """Exibe os comentários de um post específico."""
        comments = self.client.get_comments(post_id)
        if not comments:
            print(f"Nenhum comentário encontrado para o post ID {post_id}.")
            return

        print(f"\nComentários do Post ID {post_id}:")
        for comment in comments:
            print(f"\nNome: {comment['name']}")
            print(f"Email: {comment['email']}")
            print(f"Comentário: {comment['body']}")
            print("-" * 40)

    def run(self):
        """Executa o programa."""
        self.display_posts()
        post_id = self.get_post_id()
        if post_id is not None:
            self.display_comments(post_id)


if __name__ == "__main__":
    viewer = CommentViewer()
    viewer.run()
