import pytest
from app.forms import *


def test_Post_Photo_Form():
    form = PostPhotoForm({'name': ''})
    assert not form.is_valid()
    assert 'name' in form.errors