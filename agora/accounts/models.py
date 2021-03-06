import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from agora.utils import USER_ROLES, LEGAL_STATUSES, LIFECYCLE_STATUSES ,clean_html_fields
from common import helper

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):

        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):

        return self._create_user(username, email, password, True, True,
                                 **extra_fields)

# Smaller models used to provide other information for provider fields

class Network(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=60, default=None)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Network, self).save(*args, **kwargs)

class Structure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Structure, self).save(*args, **kwargs)

class Affiliation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Affiliation, self).save(*args, **kwargs)

class EsfriDomain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(EsfriDomain, self).save(*args, **kwargs)

class EsfriType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(EsfriType, self).save(*args, **kwargs)

class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Activity, self).save(*args, **kwargs)

class Challenge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Challenge, self).save(*args, **kwargs)

class Domain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Domain, self).save(*args, **kwargs)

class Subdomain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.ForeignKey('accounts.Domain', blank=True, null=True, related_name='domain_subdomain')
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Subdomain, self).save(*args, **kwargs)

class Organisation(models.Model):
    """
    The organisation providing the Service
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    pd_bai_3_legal_entity = models.BooleanField(('PD.BAI.3 Legal entity'),default=False)

    pd_bai_3_legal_status = models.CharField('PB.BAI.3_Legal_Status',
                                             max_length=255,
                                             default=None, blank=True, null=True,
                                             choices=LEGAL_STATUSES)

    pd_bai_0_id = models.TextField('PD.BAI.0_ID', default=None, blank=True, null=True)

    pd_bai_1_name = models.CharField('PD.BAI.1_Name', unique=True, max_length=100, default=None, blank=True, null=True)

    pd_bai_2_abbreviation = models.CharField('PD.BAI.2_Abbreviation', max_length=30, default=None, blank=True, null=True)

    pd_bai_4_website = models.TextField('PD.BAI.4_Website', default=None, blank=True, null=True)

    # Classification section
    pd_cli_1_scientific_domain = models.ManyToManyField(
        Domain,
        blank=True,
        verbose_name='PD.CLI.1 Scientific Domain',
        related_name='domain_providers')

    pd_cli_2_scientific_subdomain = models.ManyToManyField(
        Subdomain,
        blank=True,
        verbose_name='PD.CLI.2 Scientific Subdomain',
        related_name='subdomain_providers')

    pd_cli_3_tags = models.TextField('PD.CLI.2 Scientific Subdomain',default=None, blank=True, null=True)


    # Location section
    pd_loi_1_street_name_and_number = models.CharField('PD.LOI.1 Street Name and Number', max_length=50, default=None, blank=True, null=True)
    pd_loi_2_postal_code = models.CharField('PD.LOI.1 Postal Code', max_length=20, default=None, blank=True, null=True)
    pd_loi_3_city = models.CharField('PD.LOI.1 City', max_length=20, default=None, blank=True, null=True)
    pd_loi_4_region = models.CharField('PD.LOI.1 Region', max_length=20, default=None, blank=True, null=True)
    pd_loi_5_country_or_territory = models.CharField('PD.LOI.1 Country or Territory', max_length=50, default=None, blank=True, null=True)

    # Marketing section
    pd_mri_1_description = RichTextUploadingField('PD.MRI.1_Description', max_length=100, default=None, blank=True, null=True)

    pd_mri_2_logo = models.TextField('PD.MRI.2_Logo', default=None, blank=True, null=True)

    pd_mri_3_multimedia = models.TextField('PD.MRI.3_Multimedia', default=None, blank=True, null=True)

    # Contact Information
    main_contact = models.ForeignKey('owner.ContactInformation', blank=True, null=True, related_name="main_contact_provders")

    public_contact = models.ForeignKey('owner.ContactInformation', blank=True, null=True, related_name="public_contact_providers")

    # Maturity Information
    pd_mti_1_life_cycle_status = models.CharField('PD.MTI.1_Life_Cycle_Status', max_length=255,
                                                  default=None, blank=True, null=True,
                                                  choices=LIFECYCLE_STATUSES)

    pd_mti_2_certifications = models.CharField('PD.MTI.2_Certifications', default=None, blank=True, null=True,
                                               max_length=250)

   # Other information section

    pd_oth_1_hosting_legal_entity = models.CharField('PD.OTH.1 Hosting Legal Entity', max_length=80, default=None, blank=True, null=True)
    pd_oth_2_participating_countries = models.TextField('PD.OTH.2 Participating Countries',default=None, blank=True, null=True)

    pd_oth_3_affiliations = models.ManyToManyField(
        Affiliation,
        blank=True,
        verbose_name='PD.OTH.3 Affiliations',
        related_name='affiliated_providers')

    pd_oth_4_networks = models.ManyToManyField(
        Network,
        blank=True,
        verbose_name='PD.OTH.4 Networks',
        related_name='networked_providers')

    pd_oth_5_structure_type = models.ManyToManyField(
        Structure,
        blank=True,
        verbose_name='PD.OTH.5 Structure Type',
        related_name='structured_providers')

    pd_oth_6_esfri_domain = models.ManyToManyField(
        EsfriDomain,
        blank=True,
        verbose_name='PD.OTH.6 ESFRI Domain',
        related_name='esfridomain_providers')

    pd_oth_7_esfri_type = models.ForeignKey(
        'accounts.EsfriType',
        blank=True,
        null=True,
        verbose_name='PD.OTH.7 ESFRI Type',
        related_name='esfritype_providers')

    pd_oth_8_areas_of_activity = models.ManyToManyField(
        Activity,
        blank=True,
        verbose_name='PD.OTH.8 ESFRI Areas Of Activity',
        related_name='activity_providers')

    pd_oth_9_societal_grand_challenges = models.ManyToManyField(
        Challenge,
        blank=True,
        verbose_name='PD.OTH.9 Societal Grand Challenges',
        related_name='challenge_providers')

    pd_oth_10_national_roadmaps = models.CharField('PD.OTH.10 National Roadmaps', max_length=80, default=None, blank=True, null=True)

    @property
    def affiliation_names(self):
        return ", ".join(o.name for o in self.pd_oth_3_affiliations.all())

    @property
    def network_names(self):
        return ", ".join(o.name + " (" + o.abbreviation + ")" for o in self.pd_oth_4_networks.all())

    @property
    def structure_names(self):
        return ", ".join(o.name for o in self.pd_oth_5_structure_type.all())

    @property
    def esfridomain_names(self):
        return ", ".join(o.name for o in self.pd_oth_6_esfri_domain.all())

    @property
    def activity_names(self):
        return ", ".join(o.name for o in self.pd_oth_8_areas_of_activity.all())

    @property
    def challenge_names(self):
        return ", ".join(o.name for o in self.pd_oth_9_societal_grand_challenges.all())

    @property
    def domain_names(self):
        return ", ".join(o.name for o in self.pd_cli_1_scientific_domain.all())

    @property
    def subdomain_names(self):
        return ", ".join(o.name for o in self.pd_cli_2_scientific_subdomain.all())




    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Organisation, self).save(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions

    """
    username = models.CharField(('username'), max_length=30, unique=True,
                                default=None)
    email = models.EmailField(('email address'), max_length=254, unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    shibboleth_id = models.CharField(max_length=255,
                                     unique=True, null=True, default=None)
    role = models.CharField(choices=USER_ROLES, max_length=20, default='observer')
    organisations = models.ManyToManyField(Organisation, blank=True)
    organisation = models.ForeignKey(Organisation, blank=True, null=True, related_name='organisation_users')

    # Unused fields
    is_staff = models.BooleanField(('staff status'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    avatar = models.ImageField(upload_to='avatar', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']

    @property
    def apimas_roles(self):
        return [self.role]

    @property
    def admins_services(self):
        """
        Return True if a user has active service adminships
        """
        sa = self.serviceadminship_set.filter(state="approved")
        return sa.count() > 0

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def __unicode__(self):
        return str(self.email)
