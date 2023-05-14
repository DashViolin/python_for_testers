from fixture.application import Application
from model.users_data import ContactForm


def test_contact_edit_first(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_home_page()
    app.contacts.init_contact_update()
    contact_form = ContactForm(firstname="a", middlename="a", lastname="Yes", nickname="a",
                               title="No", company="!", address="", home="", mobile="", work="",
                               fax="", email="", email2="", email3="", homepage="", bday="",
                               bmonth="", byear="", aday="", amonth="", ayear="",
                               address2="", phone="", comment="")
    app.contacts.fill_form(contact_form)
    app.contacts.submit_contact_update()
    app.session.logout()
