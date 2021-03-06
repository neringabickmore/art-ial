from django.db import models


class About(models.Model):
    """
    About Section Model for home page
    """

    class Meta:
        verbose_name_plural = "About Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name


# Original code idea from:
# https://github.com/KarolSliwka/ArcticSchool/blob/main/home/models.py#L32
class SocialMedia(models.Model):
    """
    Social Media Model for dynamic Social Icons include
    """

    class Meta:
        verbose_name_plural = "Social Media Icons"

    class SelectName(models.TextChoices):
        """ Choices for dropdown list in Social Icons """
        Instagram = 'instagram'
        Facebook = 'facebook'
        TikTok = 'tiktok'
        Pintereset = 'pinterest'
        YouTube = 'youtube'
        Snapchat = 'snapchat'
        Twitter = 'twitter'

    class SelectIcon(models.TextChoices):
        """ Choices for dropdown list in Social Icons """
        Instagram = 'fa-instagram'
        Facebook = 'fa-facebook-f'
        TikTok = 'fa-tiktok'
        Pintereset = 'fa-pinterest-p'
        YouTube = 'fa-youtube'
        Snapchat = 'fa-snapchat-ghost'
        Twitter = 'fa-twitter'

    name = models.TextField(choices=SelectName.choices, max_length=254)
    icon = models.CharField(choices=SelectIcon.choices, max_length=50)
    url = models.URLField(max_length=1024, default='', null=True, blank=True)

    def __str__(self):
        return self.name
