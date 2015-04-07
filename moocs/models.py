from django.db import models

class Language(models.Model):
    language_name = models.TextField()

    def __str__(self):
        return self.language_name

class University(models.Model):
    abbreviation = models.TextField()
    full_name = models.TextField()

    def image_address(self):
        return "moocs/" + self.abbreviation + ".png"

    def __str__(self):
        return self.abbreviation

class Lector(models.Model):
    name = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name

class Mooc(models.Model):
    title = models.TextField()
    description_short = models.TextField()
    description_full = models.TextField()
    curriculum = models.TextField()
    language = models.ForeignKey(Language, related_name='mooc_language')
    subtitles = models.ManyToManyField(Language, related_name='mooc_subtitles_language')
    university = models.ForeignKey(University)
    workload = models.IntegerField()
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    lector = models.ForeignKey(Lector, null=True)


    def __str__(self):
        return self.title

class Lesson(models.Model):
    number = models.IntegerField()
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return '{0}: {1}'.format(self.number, self.title)

    def as_dict(self):
        return {
            'mooc': self.mooc.title,
            'number': self.number,
            'title': self.title,
            'description': self.description
        }

class Module(models.Model):
    lesson = models.ForeignKey(Lesson)
    number = models.IntegerField()
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{0}: ({1}) {2}'.format(self.number, self.status, self.text)