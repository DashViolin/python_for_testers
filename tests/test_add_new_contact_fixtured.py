import pytest
from fixture.application import Application
from model.users_data import ContactForm


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contacts.open_page()
    app.contacts.add_new_contact()
    contact_form = ContactForm(firstname="Dash", middlename="Kysyash", lastname="Loverats", nickname="Megadash",
                               title="No", company="ZZ-Top", address="111", home="222", mobile="333", work="444",
                               fax="555", email="666", email2="777", email3="8880", homepage="999", bday="11",
                               bmonth="December", byear="1999", aday="13", amonth="May", ayear="1985",
                               address2="Moscow", phone="123123123", comment="comment")
    app.contacts.fill_form(contact_form)
    app.session.logout()
