class PersonalData:
    def __init__(self, firstname, middlename, lastname, nickname, title, company):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company


#class OptionalFields:
 #   def __init__(self, title, company):
  #      self.title = title
   #     self.company = company


class Contacts:
    def __init__(self, address, home, mobile, work, fax, email, email2, email3, homepage):
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage


class DateFields:
    def __init__(self, bday, bmonth, byear, aday, amonth, ayear):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear


# @dataclass
# class DateFields:
#   bday: str
#  bmonth: str
# byear: str
# aday: str
#   amonth: str
#  ayear: str


class FillComments:
    def __init__(self, comment):
        self.comment = comment


class FillContacts:
    def __init__(self, address, phone):
        self.address = address
        self.phone = phone
