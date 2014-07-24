from django.db import models


# TODO: Confirm statuses
STATUS_CHOICES = (
	('O', 'open'),
	('S', 'submitted'),
	('P', 'processing'),
	('C', 'closed'),
	)

#TODO: Add slug to almost everything that could be a page, the 
# population that slug


class Department(models.Model):

	abbreviation =  models.CharField(max_length=5)
	name = models.CharField(max_length=250)
	description = models.TextField()

	def __str__(self):
		return 'Dept: %s' % (self.name,)


class Agency(models.Model):

	name = models.CharField(max_length=250)
	addres = models.TextField()
	phone = models.CharField(max_length=12)
	service_center = models.CharField(max_length=12)
	website = models.URLField()

	# Q: Do we need to store this link also? 
	# request_form: http://www.epa.gov/foia/requestform.html

	department = models.ForeignKey(Department)

	def __str__(self):
		return 'Agency: %s' % (self.name,)


class FOIAContact(models.Model):
	name = models.CharField(max_length=250) 
	phone = models.CharField(max_length=12) # 'service_center'
	email = models.EmailField()

	agency = models.ManyToManyField(Agency)
	department = models.ManyToManyField(Department)

	def __str__(self):
		return 'FOIA Contact: %s' % (self.name,)

class Requestor(models.Model):

	# TODO: name clarification -- first & last or one field?
	#first_name = Charfield.models(max_length=100)
	#last_name = models.Charfield(max_length=100)
	name = models.CharField(max_length=250) 
	phone = models.CharField(max_length=10)
	email = models.EmailField()

	#TODO: Add address fields or can we do this without?

	def __str__(self):
		return 'Requestor: %s' % (self.name,)


class FOIARequest(models.Model):

	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')	
	agency = models.ForeignKey('Requestor')

	request = models.TextField()

	# FEES
	#TODO: If news media, then validate news media email address?
	# How is a member legally defined? Are there other sources that we can 
	# validate against
	fee_newsmedia = models.BooleanField(default=False)  #Are you a member of media?
	fee_waiver = models.BooleanField(default=False) 	#Are you asking for a waiver?
	fee_limit = models.PositiveIntegerField() #What is the limit that the requestor is willing to pay?

	def __str__(self):
		return 'Request: %s' % (self.pk,)
