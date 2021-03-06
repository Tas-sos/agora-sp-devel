import pytest
from django.test import Client
from component.models import ServiceComponent, ServiceComponentImplementation
from accounts.models import User


class ApimasClient(Client):

    auth_token = None

    def set_token(self, token):
        self.auth_token = token

    def generic(self, *args, **kwargs):
        if self.auth_token:
            kwargs['HTTP_AUTHORIZATION'] = 'Token {}'.format(self.auth_token)
        print kwargs
        return super(ApimasClient, self).generic(*args, **kwargs)


def create_client(django_user_model, username, email, role,
                  is_superuser=False):
    user, _ = \
        django_user_model.objects.get_or_create(username=username,
                                                email=email,
                                                role=role,
                                                is_superuser=is_superuser)
    user.set_password('12345')
    user.save()

    credentials = {"username": username, "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client


@pytest.fixture(name="create_client")
def create_client_fixture(django_user_model, username, email, role,
                          is_superuser=False):
    return create_client(django_user_model, username, email, role,
                         is_superuser)


@pytest.fixture('function')
def superadmin(django_user_model):
    return create_client(django_user_model,
                         'superadmin',
                         'superadmin@test.org',
                         'superadmin',
                         True)


@pytest.fixture('function')
def admin(django_user_model):
    return create_client(django_user_model,
                         'admin',
                         'admin@test.org',
                         'admin')


@pytest.fixture('function')
def serviceadmin(django_user_model):
    return create_client(django_user_model,
                         'serviceadmin',
                         'serviceadmin@test.org',
                         'serviceadmin')


@pytest.fixture('function')
def serviceadmin_id(serviceadmin):
    s, _ = User.objects.get_or_create(username='serviceadmin')
    return s.id


@pytest.fixture('function')
def serviceadmin2(django_user_model):
    return create_client(django_user_model,
                         'serviceadmin2',
                         'serviceadmin2@test.org',
                         'serviceadmin')


@pytest.fixture('function')
def observer(django_user_model):
    return create_client(django_user_model,
                         'observer',
                         'observer@test.org',
                         'observer')



RESOURCES_CRUD = {
    'target_users': {
        'url': '/api/v2/target-users/',
        'create_data': {
            'user': 'Manager',
            'description': 'Cool manager'
        },
        'edit_data': {
            'user': 'Boss',
            'description': 'Even better boss'
        }
    },
    'providers': {
        'url': '/api/v2/providers/',
        'create_data': {
            'pd_bai_3_legal_status': "NPP",
            'pd_bai_3_legal_entity': False,
            'pd_bai_0_id': 'id',
            'pd_bai_1_name': 'pd_name',
            'pd_bai_2_abbreviation': 'pd_abb',
            'pd_bai_4_website': 'pd_website',
            'pd_loi_1_street_name_and_number': 'Kings Cross 7',
            'pd_loi_2_postal_code': '938393',
            'pd_loi_3_city': 'London',
            'pd_loi_4_region': 'Greater London',
            'pd_loi_5_country_or_territory': 'United Kingdom',
            'pd_mri_1_description': '<p>short provider description</p>',
            'pd_mri_2_logo': 'https://example.com/provider.png',
            'pd_mri_3_multimedia': 'https://vimeo.com/1001010938',
            'pd_mti_1_life_cycle_status': 'Operational',
            'pd_mti_2_certifications': 'ISO-27001'
        },
        'edit_data': {
            'pd_bai_3_legal_entity': True,
            'pd_bai_3_legal_status': "NPP",
            'pd_bai_0_id': 'id',
            'pd_bai_1_name': 'pd_name',
            'pd_bai_2_abbreviation': 'pd_abb',
            'pd_bai_4_website': 'pd_website',
            'pd_loi_1_street_name_and_number': 'Kings Cross 17',
            'pd_loi_2_postal_code': '538393',
            'pd_loi_3_city': 'London',
            'pd_loi_4_region': 'Major London',
            'pd_loi_5_country_or_territory': 'Great Britain',
            'pd_mri_1_description': '<p>short provider description</p>',
            'pd_mri_2_logo': 'https://example.com/provider.png',
            'pd_mri_3_multimedia': 'https://vimeo.com/1001010938',
            'pd_mti_1_life_cycle_status': 'Operational',
            'pd_mti_2_certifications': 'ISO-27001'
        },
    },
}
