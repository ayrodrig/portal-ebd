# -*- coding: utf-8 -*-
#
# This file is part of Lifewatch DAAP.
# Copyright (C) 2015 Rafael Salas Robledo
#
# Lifewatch DAAP is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lifewatch DAAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Lifewatch DAAP. If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, print_function, unicode_literals

from invenio.utils.forms import InvenioBaseForm

from wtforms_alchemy import model_form_factory
from wtforms import validators, RadioField
from .models import Instrument

ModelForm = model_form_factory(InvenioBaseForm)

class InstrumentForm(ModelForm):
    access_right = RadioField('Access right', choices=[('open',' Open Access'),('embargoed',' Embargoed Access'),
                                      ('restricted',' Restricted Access'), ('closed',' Closed Access')], default='open')

    class Meta:
        model = Instrument
        only = ['user_id', 'name', 'access_right', 'embargo_date',
                'conditions', 'license']