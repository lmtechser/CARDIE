# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inhertit='res.partner'
    
    birthday= fields.Datetime('Date of birth')
