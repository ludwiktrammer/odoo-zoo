# -*- coding: utf-8 -*-
from openerp import models, fields


class Animal(models.Model):
    _name = 'zoo.animal'

    name = fields.Char(required=True)
