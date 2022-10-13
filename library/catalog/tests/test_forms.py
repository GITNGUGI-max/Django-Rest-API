from django.test import TestCase

import datetime
from catalog.forms import RewBookForm
class RenewBookFormTest(TestCase):

	def test_renew_form_date_in_past(self): 
		date=datetime.datae.today() - datetime.timedelta(days=1)
		form = RewBookForm(data={'renewal_date':date})
		self.assertFalse(form.is_valid())

	def test_renew_form_date_too_far_in_future(self):
		date=datetime.date.today()+ datetime.timedelta(weeks=4)+datetime.timedelta(days=1)
		form=RewBookForm(data={'renewal_date':date})
		self.assertFalse(form.is_invalid())

	def test_renew_form_date_today(self):
		date=datetime.date.today()
		form=RewBookForm(data={'renewal_date':date})
		self.assertFalse(form.is_invalid())

	def test_renew_form_date_max(self):
		date=datetime.date.today() + datetime.timedelta(weeks=4)
		form=RewBookForm(data={'renewal_date':date})
		self.assertFalse(form.is_invalid())	
	def test_renew_form_date_field_label(self):
		
		form=RewBookForm()
		self.assertTrue(
			form.fields['renewal_date'].label is None or
			form.fields['renewal_date'].label=='renewal_date')


	def test_renew_form_date_field_help_text(self):
		
		form=RewBookForm()
		self.assertEqual(
			form.fields['renewal_date'].help_text,
			'Enter a date between now and 4 weeks (default 3).')			