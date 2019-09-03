const countries = [
  'Europe',
  'Andorra',
  'United Arab Emirates',
  'Afghanistan',
  'Antigua and Barbuda',
  'Anguilla',
  'Albania',
  'Armenia',
  'Angola',
  'Argentina',
  'American Samoa',
  'Austria',
  'Australia',
  'Aruba',
  'Åland Islands',
  'Azerbaijan',
  'Bosnia and Herzegovina',
  'Barbados',
  'Bangladesh',
  'Belgium',
  'Burkina Faso',
  'Bulgaria',
  'Bahrain',
  'Burundi',
  'Benin',
  'Saint Barthélemy',
  'Bermuda',
  'Brunei Darussalam',
  'Bolivia (Plurinational State of)',
  'Bonaire, Sint Eustatius and Saba',
  'Brazil',
  'Bahamas',
  'Bhutan',
  'Botswana',
  'Belarus',
  'Belize',
  'Canada',
  'Democratic Republic of the Congo',
  'Central African Republic',
  'Congo',
  'Switzerland',
  'Côte d&amp;Ivoire',
  'Cook Islands',
  'Chile',
  'Cameroon',
  'China',
  'Colombia',
  'Costa Rica',
  'Cuba',
  'Cabo Verde',
  'Curaçao',
  'Cyprus',
  'Czech Republic',
  'Germany',
  'Djibouti',
  'Denmark',
  'Dominica',
  'Dominican Republic',
  'Algeria',
  'Ecuador',
  'Estonia',
  'Egypt',
  'Western Sahara',
  'Eritrea',
  'Spain',
  'Ethiopia',
  'Finland',
  'Fiji',
  'Falkland Islands (Malvinas)',
  'Micronesia (Federated States of)',
  'Faeroe Islands',
  'France',
  'Gabon',
  'United Kingdom of Great Britain and Northern Ireland',
  'Grenada',
  'Georgia',
  'French Guiana',
  'Guernsey',
  'Ghana',
  'Gibraltar',
  'Greenland',
  'Gambia',
  'Guinea',
  'Guadeloupe',
  'Equatorial Guinea',
  'Greece',
  'Guatemala',
  'Guam',
  'Guinea-Bissau',
  'Guyana',
  'China, Hong Kong Special Administrative Region',
  'Honduras',
  'Croatia',
  'Haiti',
  'Hungary',
  'Indonesia',
  'Ireland',
  'Israel',
  'Isle of Man',
  'India',
  'Iraq',
  'Iran (Islamic Republic of)',
  'Iceland',
  'Italy',
  'Jersey',
  'Jamaica',
  'Jordan',
  'Japan',
  'Kenya',
  'Kyrgyzstan',
  'Cambodia',
  'Kiribati',
  'Comoros',
  'Saint Kitts and Nevis',
  'Democratic People\'s Republic of Korea',
  'Republic of Korea',
  'Kuwait',
  'Cayman Islands',
  'Kazakhstan',
  'Lao People\'s Democratic Republic',
  'Lebanon',
  'Saint Lucia',
  'Liechtenstein',
  'Sri Lanka',
  'Liberia',
  'Lesotho',
  'Lithuania',
  'Luxembourg',
  'Latvia',
  'Libya',
  'Morocco',
  'Monaco',
  'Republic of Moldova',
  'Montenegro',
  'Saint Martin (French part)',
  'Madagascar',
  'Marshall Islands',
  'The former Yugoslav Republic of Macedonia',
  'Mali',
  'Myanmar',
  'Mongolia',
  'China, Macao Special Administrative Region',
  'Northern Mariana Islands',
  'Martinique',
  'Mauritania',
  'Montserrat',
  'Malta',
  'Mauritius',
  'Maldives',
  'Malawi',
  'Mexico',
  'Malaysia',
  'Mozambique',
  'Namibia',
  'New Caledonia',
  'Niger',
  'Norfolk Island',
  'Nigeria',
  'Nicaragua',
  'Netherlands',
  'Norway',
  'Nepal',
  'Nauru',
  'Niue',
  'New Zealand',
  'Oman',
  'Panama',
  'Peru',
  'French Polynesia',
  'Papua New Guinea',
  'Philippines',
  'Pakistan',
  'Poland',
  'Saint Pierre and Miquelon',
  'Pitcairn',
  'Puerto Rico',
  'State of Palestine',
  'Portugal',
  'Palau',
  'Paraguay',
  'Qatar',
  'Reunion',
  'Romania',
  'Serbia',
  'Russian Federation',
  'Rwanda',
  'Saudi Arabia',
  'Solomon Islands',
  'Seychelles',
  'Sudan',
  'Sweden',
  'Singapore',
  'Saint Helena',
  'Slovenia',
  'Svalbard and Jan Mayen Islands',
  'Slovakia',
  'Sierra Leone',
  'San Marino',
  'Senegal',
  'Somalia',
  'Suriname',
  'South Sudan',
  'Sao Tome and Principe',
  'El Salvador',
  'Sint Maarten (Dutch part)',
  'Syrian Arab Republic',
  'Swaziland',
  'Turks and Caicos Islands',
  'Chad',
  'Togo',
  'Thailand',
  'Tajikistan',
  'Tokelau',
  'Timor-Leste',
  'Turkmenistan',
  'Tunisia',
  'Tonga',
  'Turkey',
  'Trinidad and Tobago',
  'Tuvalu',
  'United Republic of Tanzania',
  'Ukraine',
  'Uganda',
  'United States of America',
  'Uruguay',
  'Uzbekistan',
  'Holy See',
  'Saint Vincent and the Grenadines',
  'Venezuela (Bolivarian Republic of)',
  'British Virgin Islands',
  'United States Virgin Islands',
  'Viet Nam',
  'Vanuatu',
  'Wallis and Futuna Islands',
  'Samoa',
  'Yemen',
  'Mayotte',
  'South Africa',
  'Zambia',
  'Zimbabwe',
  'Channel Islands',
  'Sark',
];

const disciplines = [
  'Accelerator physics',
  'Acoustics',
  'Aerobiology',
  'Aeronautical engineering',
  'Aerosol physics',
  'Aerospace engineering',
  'Agricultural Sciences',
  'Agricultural biotechnology',
  'Agriculture',
  'Agriculture forestry and fisheries',
  'Agronomy/plant breeding/plant protection',
  'Algorithms',
  'Allergy',
  'Anaesthesiology',
  'Analytical chemistry',
  'Anatomy and morphology',
  'Andrology',
  'Animal and dairy sciences',
  'Animal science',
  'Anthropology',
  'Applied mechanics',
  'Archaeology',
  'Architectural design',
  'Architecture engineering',
  'Artificial Intelligence (expert systems\,machine learning\, robotics)',
  'Arts',
  'Astrobiology',
  'Astronautical engineering',
  'Astronomy',
  'Astroparticle physics',
  'Astrophysics',
  'Atmospheric science',
  'Atomic',
  'Audio engineering',
  'Bacteriology',
  'Basic medicine',
  'Behavioural biology',
  'Bio-derived novel materials',
  'Biocatalysis',
  'Biochemistry and molecular biology',
  'Bioderived bulk and fine chemicals',
  'Biodiversity conservation',
  'Bioengineering',
  'Bioengineering and Biomedical engineering',
  'Biofuels',
  'Bioinformatics',
  'Biological Psychology',
  'Biological rhythm',
  'Biology',
  'Biomass feedstock production tech.',
  'Biomaterials',
  'Biomedical devices',
  'Biomedical engineering',
  'Biopharming',
  'Biophysical manipulation',
  'Biophysics',
  'Bioprocessing technologies',
  'Bioproducts',
  'Bioremediation',
  'Biotechnology and medical ethics',
  'Botany',
  'Business and Management',
  'Canon Law',
  'Cardiac and Cardiovascular systems',
  'Cell biology',
  'Ceramics',
  'Chemical engineering',
  'Chemical engineering (plants/products)',
  'Chemical physics',
  'Chemical process engineering',
  'Chemistry',
  'Civil Law',
  'Civil Protection',
  'Civil engineering',
  'Climate research',
  'Clinical Psychology',
  'Clinical medicine',
  'Coating and films',
  'Cognitive Psychology',
  'Colloid chemistry',
  'Communication engineering and systems',
  'Comparative Law',
  'Comparative Psychology',
  'Comparative politics',
  'Competition Law',
  'Composites',
  'Computational biology',
  'Computational chemistry',
  'Computational physics',
  'Computer architecture',
  'Computer communications',
  'Computer graphics',
  'Computer hardware and architecture',
  'Computer security and reliability',
  'Condensed matter physics',
  'Constitutional Law',
  'Construction/Structural engineering',
  'Criminal Law',
  'Critical care/Emergency medicine',
  'Cryobiology',
  'Cryogenics',
  'Cultural and economic geography',
  'Dairy science',
  'Data management',
  'Data mining',
  'Data structures',
  'Demography',
  'Dentistry, oral surgery/medicine',
  'Dermatology and venereal diseases',
  'Developmental Psychology',
  'Developmental biology',
  'Diagnostic biotechnologies',
  'Diagnostics',
  'Distributed computing',
  'Ecology',
  'Economics and Econometrics',
  'Economics finance and business',
  'Educational and School Psychology',
  'Educational sciences',
  'Electrical and electronic engineering',
  'Electrical, electronic and information engineering',
  'Electrochemistry',
  'Empirical pata analysis',
  'Energy and fuels',
  'Environmental biotechnology',
  'Environmental engineering',
  'Epidemiology',
  'Ethics',
  'Ethnology',
  'Evolutionary Psychology',
  'Evolutionary biology',
  'Family studies',
  'Fermentation',
  'Finance',
  'Fishery',
  'Fluid Mechanics',
  'Folklore studies',
  'Food biotechnology',
  'Forestry',
  'Fusion',
  'GM technology (crops/livestock)',
  'Gastroenterology and hepatology',
  'General Education',
  'General and internal medicine',
  'General language studies',
  'General literature studies',
  'Genetics and heredity',
  'Geochemistry',
  'Geological engineering',
  'Geology',
  'Geophysics',
  'Geotechnics',
  'Geriatrics and gerontology',
  'Health care science and services',
  'Health policy and services',
  'Health sciences',
  'Health-related biotechnology',
  'Hematology',
  'High energy physics',
  'History (Prehistory; Ancient; Modern world)',
  'History and Archaeology',
  'Horticulture and viticulture',
  'Human genetics',
  'Human-computer interaction',
  'Humanities',
  'Husbandry',
  'Hydrology',
  'Immunology',
  'Industrial biotechnology',
  'Industrial relations',
  'Industrial–organisational Psychology',
  'Infectious diseases',
  'Information management',
  'Information retrieval',
  'Information science - social',
  'Inorganic and nuclear chemistry',
  'Integrative and Complementary medicine',
  'International relations',
  'Islamic Law',
  'Jewish Law',
  'Journalism',
  'Jurisprudence (Philosophy of Law)',
  'Knowledge management',
  'Languages and literature',
  'Law',
  'Library science',
  'Linguistics',
  'Literary theory',
  'Livestock cloning',
  'Marine and Freshwater biology',
  'Marker assisted selection',
  'Materials engineering',
  'Mathematical biology',
  'Mathematical chemistry',
  'Mathematical physics',
  'Mechanical engineering',
  'Media Studies (Film/Radio/TV)',
  'Media and communications',
  'Media and socio-cultural communication',
  'Medical and Health Sciences',
  'Medical biotechnology',
  'Medical ethics',
  'Medical imaging',
  'Medical physics',
  'Medicinal chemistry',
  'Microbiology',
  'Mineralogy',
  'Mining and mineral processing',
  'Molecular diagnostics',
  'Molecular physics',
  'Multimedia/hypermedia',
  'Musicology',
  'Mycology',
  'Nano-materials',
  'Nano-processes',
  'Nano-technology',
  'Neuroscience',
  'Nuclear medicine',
  'Nuclear physics',
  'Nuclear related engineering',
  'Nursing',
  'Nutrition and Dietetics',
  'Obstetrics and gynaecology',
  'Occupational health',
  'Ocean engineering',
  'Oceanography',
  'Oncology',
  'Operating systems',
  'Ophthalmology',
  'Optics',
  'Optometry',
  'Organic chemistry',
  'Organisation theory',
  'Orthopaedics',
  'Other',
  'Otorhinolaryngology',
  'Paediatrics',
  'Palaeontology',
  'Paper and wood',
  'Parallel computing',
  'Parasitology',
  'Particle physics',
  'Pathology',
  'Performing arts studies',
  'Peripheral vascular disease',
  'Personality Psychology',
  'Petroleum engineering',
  'Pets',
  'Pharmaceutical biotechnology',
  'Pharmacology and pharmacy',
  'Philosophy',
  'Philosophy ethics and religion',
  'Philosophy of science/technology',
  'Physical chemistry',
  'Physical geography',
  'Physics',
  'Physiology',
  'Planetary science',
  'Plant science',
  'Plasma physics',
  'Political economy',
  'Political philosophy',
  'Political sciences',
  'Polymer science',
  'Positive Psychology',
  'Programming languages',
  'Psychiatry',
  'Psychology',
  'Public administration',
  'Public and environmental health',
  'Pure mathematics',
  'Quantum computing',
  'Quantum physics',
  'Radiology',
  'Reliability analysis',
  'Religious studies',
  'Remote sensing',
  'Reproductive biology',
  'Respiratory systems',
  'Rheumatology',
  'Robotics Automation and Control Systems',
  'Sea vessels',
  'Seismology',
  'Social Psychology',
  'Social Sciences',
  'Social and economic geography',
  'Social biomedical science',
  'Social issues',
  'Social work',
  'Sociology',
  'Sociology',
  'Software engineering',
  'Soil science',
  'Space science',
  'Special Education (learning disabilities)',
  'Specific languages',
  'Specific literatures',
  'Sport and fitness science',
  'Statistics and probability',
  'Structural biology',
  'Substance abuse',
  'Surgery',
  'Taxonomy',
  'Textiles',
  'Theology',
  'Theoretical biology',
  'Theories of the state',
  'Theory of computation',
  'Thermal biology',
  'Thermodynamics',
  'Toxicology',
  'Transplantation',
  'Transport engineering',
  'Transport planning',
  'Tropical medicine',
  'Urban studies',
  'Urology and nephrology',
  'Veterinary anaesthesiology',
  'Veterinary medicine',
  'Veterinary ophthalmology',
  'Veterinary pathobiology',
  'Veterinary radiology',
  'Veterinary reproduction',
  'Veterinary sciences',
  'Veterinary surgery',
  'Virology',
  'Volcanology',
  'Women\'s and gender studies',
  'Zoology',
];

const language_codes = [
  'ab',
  'aa',
  'af',
  'ak',
  'sq',
  'am',
  'ar',
  'an',
  'hy',
  'as',
  'av',
  'ae',
  'ay',
  'az',
  'bm',
  'ba',
  'eu',
  'be',
  'bn',
  'bh',
  'bi',
  'bs',
  'br',
  'bg',
  'my',
  'ca',
  'km',
  'ch',
  'ce',
  'ny',
  'zh',
  'cu',
  'cv',
  'kw',
  'co',
  'cr',
  'hr',
  'cs',
  'da',
  'dv',
  'nl',
  'dz',
  'en',
  'eo',
  'et',
  'ee',
  'fo',
  'fj',
  'fi',
  'fr',
  'ff',
  'gd',
  'gl',
  'lg',
  'ka',
  'de',
  'el',
  'gn',
  'gu',
  'ht',
  'ha',
  'he',
  'hz',
  'hi',
  'ho',
  'hu',
  'is',
  'io',
  'ig',
  'id',
  'ia',
  'ie',
  'iu',
  'ik',
  'ga',
  'it',
  'ja',
  'jv',
  'kl',
  'kn',
  'kr',
  'ks',
  'kk',
  'ki',
  'rw',
  'ky',
  'kv',
  'kg',
  'ko',
  'kj',
  'ku',
  'lo',
  'la',
  'lv',
  'li',
  'ln',
  'lt',
  'lu',
  'lb',
  'mk',
  'mg',
  'ms',
  'ml',
  'mt',
  'gv',
  'mi',
  'mr',
  'mh',
  'mn',
  'na',
  'nv',
  'ng',
  'ne',
  'nd',
  'se',
  'no',
  'nb',
  'nn',
  'oc',
  'oj',
  'or',
  'om',
  'os',
  'pi',
  'ps',
  'fa',
  'pl',
  'pt',
  'pa',
  'qu',
  'ro',
  'rm',
  'rn',
  'ru',
  'sm',
  'sg',
  'sa',
  'sc',
  'sr',
  'sn',
  'ii',
  'sd',
  'si',
  'sk',
  'sl',
  'so',
  'nr',
  'st',
  'es',
  'su',
  'sw',
  'ss',
  'sv',
  'tl',
  'ty',
  'tg',
  'ta',
  'tt',
  'te',
  'th',
  'bo',
  'ti',
  'to',
  'ts',
  'tn',
  'tr',
  'tk',
  'tw',
  'ug',
  'uk',
  'ur',
  'uz',
  've',
  'vi',
  'vo',
  'wa',
  'cy',
  'fy',
  'wo',
  'xh',
  'yi',
  'yo',
  'za',
  'zu',
];

export {
  countries,
  disciplines,
  language_codes,
}
