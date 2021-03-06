/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    theme: 'theme-eosc',
    modulePrefix: 'agora-admin',
    environment: environment,
    i18n: {
      defaultLocale: 'en'
    },
    rootURL: '/ui/',
    locationType: 'auto',
    appURL: '/api/v2/',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      },
      EXTEND_PROTOTYPES: {
        // Prevent Ember Data from overriding Date.parse.
        Date: false
      }
    },
    tinyMCE:{
      version: 4
    },
    APP: {
      date_format: 'DD/MM/YYYY',
      default_route: 'resource.index',
      domestic_login_msg: 'Log in with Check-in',

      footer: {
        // If set, "Copyright © <copyright_years>" will appear in footer.
        copyright_years: '2018-2019',
        // If set, contact info  will be visible next to version in footer.
        contact: 'contact@example.com',
        // If set, <info> will be visible in footer.
        info: 'Agora is a service developed and maintained by <a href="https://grnet.gr/en/" alt="grnet">GRNET</a> co-funded by <a href="" alt="https://www.eosc-hub.eu/">EOSC-Hub</a> and <a href="https://www.eudat.eu/eudat-collaborative-data-infrastructure-cdi">EUDAT CDI</a>',
        // If set, a link will <policy_text> text will be visible in footer.
        policy_text: 'Privacy Policy',
        // If set, <policy_text> link will  redirect to <policy_url>. If not set,
        // <policy_text> link will point to policy.hbs template.
        policy_url: 'https://www.example.com',
        // If  set, logos will be visible in footer.
        logos: [{
          url: 'https://grnet.github.io/grnet-media-pack/grnet/logos/grnet_logo_en.svg',
          alt: 'grnet',
        }, {
          url: 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg',
          alt: 'europe',
        }],
      },
    }
  };

  ENV['ember-simple-auth'] = {
    authenticationRoute: 'auth.index',
    authorizer: 'authorizer:token'
  };

  ENV['ember-simple-auth-token'] = {
    serverTokenEndpoint: '/api/v2/auth/login/',
    identificationField: 'username',
    passwordField: 'password',
    tokenPropertyName: 'auth_token',
    authorizationPrefix: 'Token ',
    authorizationHeaderName: 'Authorization',
    headers: {},
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }

  return ENV;
};
