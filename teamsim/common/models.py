from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Player(models.Model):
    name = models.CharField(_('Nombre'), max_length=100)
    year_born = models.DateField(_(u'Año de nacimiento'), blank=True, null=True)
    active = models.BooleanField(_('Activo?'), default=True)

    @property
    def played_games(self):
        return self.matches

    def __unicode__(self):
        return u'%s' % self.name


class Team(models.Model):
    """ Team on each particular match.
    """
    players = models.ManyToManyField(Player, blank=True, null=True)
    match = models.ForeignKey('Match')

    @property
    def total_players(self):
        return self.players.count()


class Match(models.Model):
    RESULT_CHOICES = (
        ('futuro', u'No se jugó aún'),
        ('suspendido', u'Se suspendió'),
        ('equipo1', u'Ganó el equipo1'),
        ('equipo2', u'Ganó el equipo2'),
        ('movido', u'Se cambió para otra fecha'),
    )
    date = models.DateField(_('Fecha de partido'), blank=True, null=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.match_type, self.date)


class FutbolMatch(Match):
    FUTBOL_MATCH_TYPE = (
        ('f4', u'Futbol4'),
        ('f5', u'Futbol5'),
        ('f6', u'Futbol6'),
        ('f7', u'Futbol7'),
        ('f9', u'Futbol9'),
        ('f11', u'Futbol11'),
    )
    match_type = models.CharField(_('Tipo de partido'), max_length=20, choices=FUTBOL_MATCH_TYPE)


class BasketMatch(Match):
    BASKET_MATCH_TYPE = (
        ('3x3', u'3 x 3'),
        ('4x4', u'4 x 4'),
        ('5x5', u'5 x 5'),
    )
    match_type = models.CharField(_('Tipo de partido'), max_length=20, choices=BASKET_MATCH_TYPE)
