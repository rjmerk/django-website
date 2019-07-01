import pytest
from apps.core.models import Article

pytestmark = pytest.mark.django_db


def test_add_article(admin_client):
    response = admin_client.get(
        "/admin/core/article/add/")
    assert response.status_code == 200


def test_add_article_post(admin_client):
    response = admin_client.post(
        "/admin/core/article/add/",
        {
            "title": "jeee",
            "slug": "jee-eee",
            "content": "a fine move",
            "publish_date_0": "2012-01-01",
            "publish_date_1": "11:11"
        }

    )
    assert response.content == b""
    assert response.status_code == 302
    assert Article.objects.first().title == "jeee"
