from django.test import TestCase
from markdown import markdown


class DocTest(TestCase):

    def test_markdown(self):
        markdown_text = '# Headline'
        html_text = markdown(markdown_text)
        self.assertEqual(html_text, '<h1>Headline</h1>')

    def test_doc_index_view(self):
        response = self.client.get('/doc/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Web Dev')

    def test_doc_default_view(self):
        response = self.client.get('/doc')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/doc/')
