from django.db import models
from current_user.models import CurrentUserField
from django.db.models.signals import pre_save

class PublicationTracker(models.Model):
    """ Stores the author, publication and update dates of entry. """

    created_by = CurrentUserField(editable=False, related_name="%(app_label)s_%(class)s")
    publication_datetime = models.DateTimeField(verbose_name="Publication datetime", auto_now_add=True, editable=False)
    update_datetime = models.DateTimeField(verbose_name="Update datetime", auto_now=True, editable=False)
    
    class Meta:
        abstract = True

    def get_current_user(self):
        _user = self.created_by
        pre_save.send(sender=self.__class__, instance=self, raw=True, using="default")
        _current = self.created_by
        self.created_by = _user
        return _current
