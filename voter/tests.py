from django.test import TestCase
from .models import Show, Season, Episode
from django.utils import timezone
from datetime import timedelta
# Create your tests here. NEVERRRRR

class TestView(TestCase):

    def setUp(self):
        self.show_1 = Show.objects.create(name = "BB")
        self.show_2 = Show.objects.create(name = "RPDR ALL STARS")

    def test_index_links_to_show(self):
        """
        when the index page is accessed, we get all shows displayed
        """
        response = self.client.get("/voter/")
        self.assertContains(response, "<a href=\"/voter/1\" class=\"btn btn-primary\">Vote now!</a>")
        self.assertContains(response, "<a href=\"/voter/2\" class=\"btn btn-primary\">Vote now!</a>")

    def test_show_includes_show_1(self):
        response = self.client.get("/voter/1")
        self.assertContains(response, "BB")
        self.assertNotContains(response, "RPDR ALL STARS")

    def test_show_includes_show_2(self):
        response = self.client.get("/voter/2")
        self.assertNotContains(response, "BB")
        self.assertContains(response, "RPDR ALL STARS")

    def test_show_not_found(self):

        response = self.client.get("/voter/0")
        self.assertEquals(response.status_code, 404)

class TestModel(TestCase):

    def setUp(self):
        self.show_1 = Show.objects.create(name = "RPDR")
        Season.objects.create(number = 1,
                             airdate = timezone.now(),
                             show = self.show_1)
        self.latest_season = Season.objects.create(number = 10,
                             airdate = timezone.now(),
                             show = self.show_1)
        Season.objects.create(number = 3,
                             airdate = timezone.now(),
                             show = self.show_1)
        self.time = timezone.now()

        for i in range(100, 0, -1):
            Episode.objects.create(length = timedelta(hours = i),
                                   name  = str(i),
                                   airdate = self.time + timedelta(hours = i),
                                   season = self.latest_season)

    def test_current_season(self):
        self.assertEqual(self.show_1.current_season.number, 10)


    def test_season_ordered_episodes(self):
        for i, episode in enumerate(self.latest_season.ordered_episodes.all()):
            i = i + 1
            self.assertEqual(episode.length, timedelta(hours = i))
            self.assertEqual(episode.name, str(i))
            self.assertEqual(episode.airdate, self.time + timedelta(hours = i))
