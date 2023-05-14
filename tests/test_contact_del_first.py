from fixture.application import Application


def test_del_first_contact(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_home_page()
    app.contacts.del_first_contact()
    app.session.logout()
