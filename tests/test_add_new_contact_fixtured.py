import pytest
from fixture.Application import Application
from model.users_data import PersonalData
from model.users_data import Contacts
from model.users_data import DateFields
from model.users_data import FillComments
from model.users_data import FillContacts


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_contact_page()
    app.add_new_contact()
    personal_data = PersonalData(firstname="Dash", middlename="Kysyash", lastname="Loverats", nickname="Megadash",
                                 title="No", company="ZZ-Top")
    app.fill_personal_data_form(personal_data)
    fill_contacts = Contacts(address="111", home="222", mobile="333", work="444", fax="555", email="666",
                             email2="777", email3="8880", homepage="999")
    app.fill_contact_form(fill_contacts)
    date_fields = DateFields(bday="11", bmonth="December", byear="1999", aday="13", amonth="May", ayear="1985")
    app.fill_date_fields(date_fields)
    fill_address = FillContacts(address="Moscow", phone="123123123")
    app.fill_contacts(fill_address)
    fill_comments = FillComments(comment="comment")
    app.fill_comments(fill_comments)
    app.open_home_page_before_logout()
    app.session.logout()