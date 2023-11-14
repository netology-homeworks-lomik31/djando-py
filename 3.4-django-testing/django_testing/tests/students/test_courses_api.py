import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses():
    return lambda *args, **kwargs: baker.make(Course, *args, **kwargs)

@pytest.fixture
def students():
    return lambda *args, **kwargs: baker.make(Student, *args, **kwargs)

@pytest.mark.django_db
def test_get_course(client, courses):
    c = courses(_quantity=1)
    
    res = client.get(f"/api/v1/courses/{c[0].id}/")

    assert res.status_code == 200

    assert c[0].id == res.json()[0]["id"]

    assert c[0].name == res.json()[0]["name"]

@pytest.mark.django_db
def test_get_courses(client, courses):
    cs = courses(_quantity=10)

    res = client.get("/api/v1/courses/")

    assert res.status_code == 200

    json = res.json()


    for i in range(len(cs)):
        assert cs[i].id == json[i]["id"]
        assert cs[i].name == json[i]["name"]

@pytest.mark.django_db
def test_courses_filter_id(client, courses):
    cs = courses(_quantity=5)

    c = cs[1]

    res = client.get(f"/api/v1/courses/", {"id": c.id})

    assert res.status_code == 200

    json = res.json()

    assert c.id == json[0]["id"]
    assert c.name == json[0]["name"]

@pytest.mark.django_db
def test_courses_filter_name(client, courses):
    cs = courses(_quantity=5)

    c = cs[3]

    res = client.get(f"/api/v1/courses/", {"name": c.name})

    assert res.status_code == 200

    json = res.json()

    assert c.id == json[0]["id"]
    assert c.name == json[0]["name"]

@pytest.mark.django_db
def test_course_create(client):
    res = client.post("/api/v1/courses/", data = {"name": "aboba"}, format="json")

    assert res.status_code == 201

    json = res.json()
    c = Course.objects.first()

    assert c.id == json["id"]
    assert c.name == json["name"]

@pytest.mark.django_db
def test_course_update(client, courses):
    cs = courses(_quantity = 5)

    c = cs[4]
    
    patch_data = {"name": "aboba"}

    res = client.patch(f"/api/v1/courses/{c.id}/", data = patch_data, format="json")

    assert res.status_code == 200

    json = res.json()
    c_db = Course.objects.filter(id=c.id).first()

    assert c.id == json["id"]
    assert c_db == c.id
    assert c.name == json["name"]
    assert c_db.name == c.name
    assert patch_data["name"] == c.name

@pytest.mark.django_db
def test_course_update(client, courses):
    cs = courses(_quantity = 5)

    c = cs[1]

    res = client.delete(f"/api/v1/courses/{c.id}/")

    assert res.status_code == 204
    c_db = Course.objects.filter(id=c.id).first()

    assert c_db == None

