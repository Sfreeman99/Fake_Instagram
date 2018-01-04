import pytest
from app.models import ImageModel
from app.forms import *


def test_Post_Photo_Form():
    form = PostPhotoForm({'name': ''})
    assert not form.is_valid()
    assert 'name' in form.errors


@pytest.mark.django_db
def test_Image_can_be_added():
    new_image = ImageModel(name='Picture of me', image='foo.jpg')
    new_image.save()
    assert new_image.name == 'Picture of me'
    assert new_image.image == 'foo.jpg'
    assert ImageModel.objects.get(name='Picture of me')