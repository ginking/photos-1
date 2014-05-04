from django.db import models

class MediaBase(models.model):
    title = models.Charfield(max_length=256)    


class Picture(MediaBase):
    file = models.ImageField(upload_to= )
    albums = models.ManyToManyField(album)


class Album(modesl.model):
    pass
