import datetime

from django.test import TestCase
from django.urls import reverse

from blog.models import Post
from .models import Project


class HomePageTests(TestCase):
    def test_home_displays_projects_and_links_to_their_urls(self):
        project = Project.objects.create(
            title="Portfolio demo",
            description="A Django portfolio project.",
            url="https://example.com/project",
        )

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, project.title)
        self.assertContains(response, project.url)
        self.assertContains(response, "portfolio/style.")
        self.assertContains(response, "portfolio/main.")

    def test_home_displays_recent_blog_posts_linked_to_detail_pages(self):
        post = Post.objects.create(
            title="Django article",
            description="An introduction to Django.",
            date=datetime.date(2026, 1, 2),
        )

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, reverse("blog:post_detail", args=[post.pk]))
        self.assertContains(response, reverse("blog:posts"))
        self.assertContains(response, "portfolio/Yonathan_Muset_CV.")

    def test_home_displays_empty_states_when_no_content_exists(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aún no hay proyectos publicados.")
        self.assertContains(response, "Aún no hay publicaciones.")


class BlogPageTests(TestCase):
    def test_blog_list_and_detail_render_with_the_shared_layout(self):
        post = Post.objects.create(
            title="Django article",
            description="An introduction to Django.",
            date=datetime.date(2026, 1, 2),
        )

        list_response = self.client.get(reverse("blog:posts"))
        detail_response = self.client.get(
            reverse("blog:post_detail", args=[post.pk])
        )

        self.assertEqual(list_response.status_code, 200)
        self.assertContains(list_response, post.title)
        self.assertContains(
            list_response,
            reverse("blog:post_detail", args=[post.pk]),
        )
        self.assertEqual(detail_response.status_code, 200)
        self.assertContains(detail_response, post.description)
        self.assertContains(detail_response, "Saltar al contenido")
