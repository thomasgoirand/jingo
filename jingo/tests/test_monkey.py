from __future__ import unicode_literals

from django import forms
import six

from jinja2 import escape
from nose.tools import eq_

import jingo.monkey

from .utils import render


class MyForm(forms.Form):
    email = forms.EmailField()


def test_monkey_patch():
    form = MyForm()
    html = form.as_ul()
    context = {'form': form}
    t = '{{ form.as_ul() }}'

    eq_(escape(html), render(t, context))

    jingo.monkey.patch()
    eq_(html, render(t, context))

    s = six.text_type(form['email'])
    eq_(s, render('{{ form.email }}', {'form': form}))
