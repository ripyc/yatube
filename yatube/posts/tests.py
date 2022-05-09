from django.test import TestCase, Client
from .models import Post, User
from django.urls import reverse


class TestIndexPost(TestCase):
    def test_index_available(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class TestPostCreate(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="alfa",
            email="alfa@email.ru",
            password="test_al123fa",
        )

    # тест на открытие страницы профиля при создании пользователя
    def test_creating_profile_page(self):
        self.client.login(username="alfa", password="test_al123fa")
        response = self.client.get(reverse("profile", kwargs={"username": "alfa"}))
        self.assertEqual(response.status_code, 200)

    # тест на открытия страницы редактирования поста
    def test_post_edit_page(self):
        self.client.login(username="alfa", password="test_al123fa")
        self.client.post(reverse("new_post"), {"text": "тест alfa"})
        response = self.client.get(reverse("post_edit", kwargs={"username": "alfa", "post_id": 1}))
        self.assertEqual(response.status_code, 200)

    # тест на невозможность открытия страницы создания поста неаторизованным пользователем
    def test_logout_user_post_create(self):
        self.client.logout()
        response = self.client.get(reverse("new_post"))
        self.assertEqual(response.status_code, 302)


class TestPostEdit(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="alfa",
            email="alfa@email.ru",
            password="test_al123fa",
            )

    # тест на появление поста в профиле, на главное странице и на странице поста
    def test_post_at_3pages(self):
        self.client.login(username="alfa", password="test_al123fa")
        self.test_post = Post.objects.create(
            text="alfa beta gama delta",
            author=self.user
        )
        self.new_text = "аз буки веди глаголь добро"
        response = self.client.post(
            reverse("post_edit", kwargs={"username": "alfa", "post_id": self.test_post.pk}),
            data={"text": self.new_text},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.get(id=self.test_post.pk).text, self.new_text)
        for url in (
                '',
                reverse("profile", kwargs={"username": self.test_post.author}),
                reverse("post", kwargs={"username": self.test_post.author, "post_id": self.test_post.pk})
                ):
            response = self.client.post(url)
            self.assertContains(response, self.new_text)
