# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
from app import TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        textresponse = response.get_data(as_text=True)
        assert "<title>{% block title %} {{ title }} {% endblock %}</title>" in textresponse
        # TODO Add more tests relating to the home page
       
        assert "<h2 id = \"home-header\">welcome.</h2>" in textresponse
        assert "<h2 id = \"home-intro\">- intro -</h2>" in textresponse


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page
        textresponse = response.get_data(as_text=True)
        print("the text response: ",textresponse, sep="---")
        

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<button type="submit">' in html
        assert '<input type="text" name="name">' in html
        assert '<input type="text" name="email">' in html
        assert '<input type="text" name="content">' in html

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        textresponse = response.get_data(as_text=True)
        assert "Invalid content" in textresponse

        response = self.client.post("/api/timeline_post", data = {
            "email": "john@example.com",
            "content": "Hello world, I\'m John!"
        })
        
        assert response.status_code == 400
        textresponse = response.get_data(as_text=True)
        assert "Invalid name" in textresponse

        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "wrong_format",
            "content": "Hello world, I\'m John!"
        })
        assert response.status_code == 400
        textresponse = response.get_data(as_text=True)
        assert "Invalid email" in textresponse