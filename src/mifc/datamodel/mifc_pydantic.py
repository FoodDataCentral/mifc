from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'mifc',
     'default_range': 'string',
     'description': 'The Minimum Information (about any) Food Composition (MIFC) '
                    'data standard.',
     'id': 'https://w3id.org/FoodDataCentral/mifc',
     'imports': ['linkml:types'],
     'license': 'CC0',
     'name': 'mifc',
     'prefixes': {'FDC': {'prefix_prefix': 'FDC',
                          'prefix_reference': 'https://fdc.nal.usda.gov/'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PTFI': {'prefix_prefix': 'PTFI',
                           'prefix_reference': 'https://foodperiodictable.org/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mifc': {'prefix_prefix': 'mifc',
                           'prefix_reference': 'https://w3id.org/FoodDataCentral/mifc/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'}},
     'see_also': ['https://FoodDataCentral.github.io/mifc'],
     'source_file': 'src/mifc/schema/mifc.yaml',
     'subsets': {'RecommendedSubset': {'description': 'A subset of the MIFC slots '
                                                      'that are required and '
                                                      'recommended for use use in '
                                                      'a Food Composition '
                                                      'Table/Database.',
                                       'from_schema': 'https://w3id.org/FoodDataCentral/mifc',
                                       'name': 'RecommendedSubset',
                                       'title': 'Recommended subset'},
                 'RequiredSubset': {'description': 'A subset of the MIFC slots '
                                                   'that are required for use use '
                                                   'in a Food Composition '
                                                   'Table/Database.',
                                    'from_schema': 'https://w3id.org/FoodDataCentral/mifc',
                                    'name': 'RequiredSubset',
                                    'title': 'Required subset'}},
     'title': 'mifc'} )

class CompoundAnalyticalMeasurementMethod(str, Enum):
    AAS = "AAS"
    """
    Atomic absorption spectroscopy
    """
    AES = "AES"
    """
    Atomic emission spectroscopy
    """
    Colorimetric = "Colorimetric"
    """
    Colorimetric analysis
    """
    Combustion = "Combustion"
    Enzymatic_colorimetric = "Enzymatic-colorimetric"
    Enzymatic_gravimetric = "Enzymatic-gravimetric"
    Enzymatic_spectrometric = "Enzymatic-spectrometric"
    Extraction = "Extraction"
    Fluorometric = "Fluorometric"
    GC = "GC"
    """
    Gas chromatography
    """
    GLC = "GLC"
    """
    Gas-liquid chromatography
    """
    Gravimetric = "Gravimetric"
    HPAEC_PAD = "HPAEC-PAD"
    """
    High-performance anion-exchange chromatography with pulsed amperometric detection
    """
    HPLC = "HPLC"
    """
    High-performance liquid chromatography
    """
    HPLC_MSSOLIDUSMS = "HPLC-MS/MS"
    """
    High-performance liquid chromatography with tandem mass spectrometry
    """
    HPLC_UV = "HPLC-UV"
    """
    High-performance liquid chromatography with ultra-violet spectroscopy
    """
    ICP = "ICP"
    """
    Inductively coupled plasma
    """
    ICP_MS = "ICP-MS"
    """
    Inductively coupled plasma mass spectrometry
    """
    ICP_OES = "ICP-OES"
    """
    Inductively coupled plasma optical emission spectroscopy
    """
    ID_GC_MS = "ID-GC-MS"
    """
    Isotope dilution gas chromatography mass spectrometry
    """
    Kjeldahl = "Kjeldahl"
    """
    Kjeldahl digestion
    """
    Nephelometric = "Nephelometric"
    LC = "LC"
    """
    Liquid chromatography
    """
    LC_FLD = "LC-FLD"
    """
    Liquid chromatography with fluorescence detection
    """
    LC_ESI_IDMS = "LC-ESI-IDMS"
    """
    Liquid chromatography with electrospray ionization-isotope dilution mass spectrometry
    """
    Microbiological = "Microbiological"
    """
    Microbiological assay
    """
    Microfluorometric = "Microfluorometric"
    Polarimetric = "Polarimetric"


class FoodPreservationState(str, Enum):
    air_dried = "air-dried"
    artificially_dried = "artificially dried"
    brined = "brined"
    candied = "candied"
    canned = "canned"
    cured = "cured"
    dried = "dried"
    fermented = "fermented"
    freeze_dried = "freeze-dried"
    fresh = "fresh"
    heat_treated = "heat treated"
    irradiated = "irradiated"
    jellied = "jellied"
    kippered = "kippered"
    naturally_dried = "naturally dried"
    pasteurized = "pasteurized"
    pickled = "pickled"
    raw = "raw"
    shelf_stable = "shelf stable"
    sun_dried = "sun-dried"
    ultraviolet_light_exposed = "ultraviolet light exposed"


class FoodStorageTemperatureState(str, Enum):
    chilled = "chilled"
    foodsafe_chilled = "foodsafe chilled"
    frozen = "frozen"
    refrigerated = "refrigerated"


class FoodRipenessState(str, Enum):
    ripe = "ripe"
    overripe = "overripe"
    unripe = "unripe"
    slightly_ripe = "slightly ripe"


class FoodAcquisitionLocationType(str, Enum):
    grower = "grower"
    field = "field"
    retailer = "retailer"
    fresh_market = "fresh market"
    small_grocery = "small grocery"
    supermarket = "supermarket"
    distributor = "distributor"
    biobank = "biobank"
    unknown = "unknown"
    other = "other"


class FoodCookingMethod(str, Enum):
    baked = "baked"
    blanched = "blanched"
    boiled = "boiled"
    braised = "braised"
    broiled = "broiled"
    cooked = "cooked"
    dry_heat_cooked = "dry-heat cooked"
    dry_roasted = "dry-roasted"
    fried = "fried"
    grilled = "grilled"
    heated = "heated"
    microwaved = "microwaved"
    moist_heat_cooked = "moist-heat cooked"
    oil_roasted = "oil-roasted"
    pan_broiled = "pan-broiled"
    pan_browned = "pan-browned"
    pan_fried = "pan-fried"
    parboiled = "parboiled"
    partially_fried = "partially fried"
    poached = "poached"
    precooked = "precooked"
    refried = "refried"
    roasted = "roasted"
    sauteed = "sauteed"
    simmered = "simmered"
    slow_roasted = "slow-roasted"
    smoked = "smoked"
    spit_roasted = "spit-roasted"
    steamed = "steamed"
    stewed = "stewed"
    stir_fried = "stir-fried"
    toasted = "toasted"
    uncooked = "uncooked"
    unheated = "unheated"


class SkosMatchType(str, Enum):
    skosCOLONexactMatch = "skos:exactMatch"
    """
    Mappings assessed to indicate that the concepts expressed in the subject and object terms can be used interchangeably following the transitive property.
    """
    skosCOLONcloseMatch = "skos:closeMatch"
    """
    Mappings between the subject and object terms that convey a high degree of similarity, but are not exactly the same or interchangeable. Assignments of closeMatch should only be used when there is no appropriate broadMatch or narrowMatch to be found within the subject and object vocabulaires.
    """
    skosCOLONbroadMatch = "skos:broadMatch"
    """
    Mappings between a subject and an object term, where the object term is above the subject within a concept hierarchy. A broadMatch is the inverse of a narrowMatch.
    """
    skosCOLONnarrowMatch = "skos:narrowMatch"
    """
    Mappings between a subject and an object term, where the object term that is below the subject within a concept hierarchy. A narrowMatch is the inverse of a broadMatch.
    """
    skosCOLONrelatedMatch = "skos:relatedMatch"
    """
    Mappings between subject and object terms that are not broadMatch, narrowMatch, closeMatch or exactMatch but have some association.
    """


class ResourceMIFCVersionTag(str, Enum):
    v0FULL_STOP1FULL_STOP0 = "v0.1.0"
    v0FULL_STOP2FULL_STOP0 = "v0.2.0"
    v0FULL_STOP3FULL_STOP0 = "v0.3.0"
    v0FULL_STOP3FULL_STOP1 = "v0.3.1"
    v0FULL_STOP3FULL_STOP2 = "v0.3.2"


class CountryCode(str, Enum):
    AFG = "AFG"
    """
    Afghanistan
    """
    ALA = "ALA"
    """
    Aland Islands
    """
    ALB = "ALB"
    """
    Albania
    """
    DZA = "DZA"
    """
    Algeria
    """
    ASM = "ASM"
    """
    American Samoa
    """
    AND = "AND"
    """
    Andorra
    """
    AGO = "AGO"
    """
    Angola
    """
    AIA = "AIA"
    """
    Anguilla
    """
    ATA = "ATA"
    """
    Antarctica
    """
    ATG = "ATG"
    """
    Antigua and Barbuda
    """
    ARG = "ARG"
    """
    Argentina
    """
    ARM = "ARM"
    """
    Armenia
    """
    ABW = "ABW"
    """
    Aruba
    """
    AUS = "AUS"
    """
    Australia
    """
    AUT = "AUT"
    """
    Austria
    """
    AZE = "AZE"
    """
    Azerbaijan
    """
    BHS = "BHS"
    """
    Bahamas
    """
    BHR = "BHR"
    """
    Bahrain
    """
    BGD = "BGD"
    """
    Bangladesh
    """
    BRB = "BRB"
    """
    Barbados
    """
    BLR = "BLR"
    """
    Belarus
    """
    BEL = "BEL"
    """
    Belgium
    """
    BLZ = "BLZ"
    """
    Belize
    """
    BEN = "BEN"
    """
    Benin
    """
    BMU = "BMU"
    """
    Bermuda
    """
    BTN = "BTN"
    """
    Bhutan
    """
    BOL = "BOL"
    """
    Bolivia
    """
    BIH = "BIH"
    """
    Bosnia and Herzegovina
    """
    BWA = "BWA"
    """
    Botswana
    """
    BVT = "BVT"
    """
    Bouvet Island
    """
    BRA = "BRA"
    """
    Brazil
    """
    VGB = "VGB"
    """
    British Virgin Islands
    """
    IOT = "IOT"
    """
    British Indian Ocean Territory
    """
    BRN = "BRN"
    """
    Brunei Darussalam
    """
    BGR = "BGR"
    """
    Bulgaria
    """
    BFA = "BFA"
    """
    Burkina Faso
    """
    BDI = "BDI"
    """
    Burundi
    """
    KHM = "KHM"
    """
    Cambodia
    """
    CMR = "CMR"
    """
    Cameroon
    """
    CAN = "CAN"
    """
    Canada
    """
    CPV = "CPV"
    """
    Cape Verde
    """
    CYM = "CYM"
    """
    Cayman Islands
    """
    CAF = "CAF"
    """
    Central African Republic
    """
    TCD = "TCD"
    """
    Chad
    """
    CHL = "CHL"
    """
    Chile
    """
    CHN = "CHN"
    """
    China
    """
    HKG = "HKG"
    """
    Hong Kong, SAR China
    """
    MAC = "MAC"
    """
    Macao, SAR China
    """
    CXR = "CXR"
    """
    Christmas Island
    """
    CCK = "CCK"
    """
    Cocos (Keeling) Islands
    """
    COL = "COL"
    """
    Colombia
    """
    COM = "COM"
    """
    Comoros
    """
    COG = "COG"
    """
    Congo (Brazzaville)
    """
    COD = "COD"
    """
    Congo, (Kinshasa)
    """
    COK = "COK"
    """
    Cook Islands
    """
    CRI = "CRI"
    """
    Costa Rica
    """
    CIV = "CIV"
    """
    Côte d'Ivoire
    """
    HRV = "HRV"
    """
    Croatia
    """
    CUB = "CUB"
    """
    Cuba
    """
    CYP = "CYP"
    """
    Cyprus
    """
    CZE = "CZE"
    """
    Czech Republic
    """
    DNK = "DNK"
    """
    Denmark
    """
    DJI = "DJI"
    """
    Djibouti
    """
    DMA = "DMA"
    """
    Dominica
    """
    DOM = "DOM"
    """
    Dominican Republic
    """
    ECU = "ECU"
    """
    Ecuador
    """
    EGY = "EGY"
    """
    Egypt
    """
    SLV = "SLV"
    """
    El Salvador
    """
    GNQ = "GNQ"
    """
    Equatorial Guinea
    """
    ERI = "ERI"
    """
    Eritrea
    """
    EST = "EST"
    """
    Estonia
    """
    ETH = "ETH"
    """
    Ethiopia
    """
    FLK = "FLK"
    """
    Falkland Islands (Malvinas)
    """
    FRO = "FRO"
    """
    Faroe Islands
    """
    FJI = "FJI"
    """
    Fiji
    """
    FIN = "FIN"
    """
    Finland
    """
    FRA = "FRA"
    """
    France
    """
    GUF = "GUF"
    """
    French Guiana
    """
    PYF = "PYF"
    """
    French Polynesia
    """
    ATF = "ATF"
    """
    French Southern Territories
    """
    GAB = "GAB"
    """
    Gabon
    """
    GMB = "GMB"
    """
    Gambia
    """
    GEO = "GEO"
    """
    Georgia
    """
    DEU = "DEU"
    """
    Germany
    """
    GHA = "GHA"
    """
    Ghana
    """
    GIB = "GIB"
    """
    Gibraltar
    """
    GRC = "GRC"
    """
    Greece
    """
    GRL = "GRL"
    """
    Greenland
    """
    GRD = "GRD"
    """
    Grenada
    """
    GLP = "GLP"
    """
    Guadeloupe
    """
    GUM = "GUM"
    """
    Guam
    """
    GTM = "GTM"
    """
    Guatemala
    """
    GGY = "GGY"
    """
    Guernsey
    """
    GIN = "GIN"
    """
    Guinea
    """
    GNB = "GNB"
    """
    Guinea-Bissau
    """
    GUY = "GUY"
    """
    Guyana
    """
    HTI = "HTI"
    """
    Haiti
    """
    HMD = "HMD"
    """
    Heard and Mcdonald Islands
    """
    VAT = "VAT"
    """
    Holy See (Vatican City State)
    """
    HND = "HND"
    """
    Honduras
    """
    HUN = "HUN"
    """
    Hungary
    """
    ISL = "ISL"
    """
    Iceland
    """
    IND = "IND"
    """
    India
    """
    IDN = "IDN"
    """
    Indonesia
    """
    IRN = "IRN"
    """
    Iran, Islamic Republic of
    """
    IRQ = "IRQ"
    """
    Iraq
    """
    IRL = "IRL"
    """
    Ireland
    """
    IMN = "IMN"
    """
    Isle of Man
    """
    ISR = "ISR"
    """
    Israel
    """
    ITA = "ITA"
    """
    Italy
    """
    JAM = "JAM"
    """
    Jamaica
    """
    JPN = "JPN"
    """
    Japan
    """
    JEY = "JEY"
    """
    Jersey
    """
    JOR = "JOR"
    """
    Jordan
    """
    KAZ = "KAZ"
    """
    Kazakhstan
    """
    KEN = "KEN"
    """
    Kenya
    """
    KIR = "KIR"
    """
    Kiribati
    """
    PRK = "PRK"
    """
    Korea (North)
    """
    KOR = "KOR"
    """
    Korea (South)
    """
    KWT = "KWT"
    """
    Kuwait
    """
    KGZ = "KGZ"
    """
    Kyrgyzstan
    """
    LAO = "LAO"
    """
    Lao PDR
    """
    LVA = "LVA"
    """
    Latvia
    """
    LBN = "LBN"
    """
    Lebanon
    """
    LSO = "LSO"
    """
    Lesotho
    """
    LBR = "LBR"
    """
    Liberia
    """
    LBY = "LBY"
    """
    Libya
    """
    LIE = "LIE"
    """
    Liechtenstein
    """
    LTU = "LTU"
    """
    Lithuania
    """
    LUX = "LUX"
    """
    Luxembourg
    """
    MKD = "MKD"
    """
    Macedonia, Republic of
    """
    MDG = "MDG"
    """
    Madagascar
    """
    MWI = "MWI"
    """
    Malawi
    """
    MYS = "MYS"
    """
    Malaysia
    """
    MDV = "MDV"
    """
    Maldives
    """
    MLI = "MLI"
    """
    Mali
    """
    MLT = "MLT"
    """
    Malta
    """
    MHL = "MHL"
    """
    Marshall Islands
    """
    MTQ = "MTQ"
    """
    Martinique
    """
    MRT = "MRT"
    """
    Mauritania
    """
    MUS = "MUS"
    """
    Mauritius
    """
    MYT = "MYT"
    """
    Mayotte
    """
    MEX = "MEX"
    """
    Mexico
    """
    FSM = "FSM"
    """
    Micronesia, Federated States of
    """
    MDA = "MDA"
    """
    Moldova
    """
    MCO = "MCO"
    """
    Monaco
    """
    MNG = "MNG"
    """
    Mongolia
    """
    MNE = "MNE"
    """
    Montenegro
    """
    MSR = "MSR"
    """
    Montserrat
    """
    MAR = "MAR"
    """
    Morocco
    """
    MOZ = "MOZ"
    """
    Mozambique
    """
    MMR = "MMR"
    """
    Myanmar
    """
    NAM = "NAM"
    """
    Namibia
    """
    NRU = "NRU"
    """
    Nauru
    """
    NPL = "NPL"
    """
    Nepal
    """
    NLD = "NLD"
    """
    Netherlands
    """
    ANT = "ANT"
    """
    Netherlands Antilles
    """
    NCL = "NCL"
    """
    New Caledonia
    """
    NZL = "NZL"
    """
    New Zealand
    """
    NIC = "NIC"
    """
    Nicaragua
    """
    NER = "NER"
    """
    Niger
    """
    NGA = "NGA"
    """
    Nigeria
    """
    NIU = "NIU"
    """
    Niue
    """
    NFK = "NFK"
    """
    Norfolk Island
    """
    MNP = "MNP"
    """
    Northern Mariana Islands
    """
    NOR = "NOR"
    """
    Norway
    """
    OMN = "OMN"
    """
    Oman
    """
    PAK = "PAK"
    """
    Pakistan
    """
    PLW = "PLW"
    """
    Palau
    """
    PSE = "PSE"
    """
    Palestinian Territory
    """
    PAN = "PAN"
    """
    Panama
    """
    PNG = "PNG"
    """
    Papua New Guinea
    """
    PRY = "PRY"
    """
    Paraguay
    """
    PER = "PER"
    """
    Peru
    """
    PHL = "PHL"
    """
    Philippines
    """
    PCN = "PCN"
    """
    Pitcairn
    """
    POL = "POL"
    """
    Poland
    """
    PRT = "PRT"
    """
    Portugal
    """
    PRI = "PRI"
    """
    Puerto Rico
    """
    QAT = "QAT"
    """
    Qatar
    """
    REU = "REU"
    """
    Réunion
    """
    ROU = "ROU"
    """
    Romania
    """
    RUS = "RUS"
    """
    Russian Federation
    """
    RWA = "RWA"
    """
    Rwanda
    """
    BLM = "BLM"
    """
    Saint-Barthélemy
    """
    SHN = "SHN"
    """
    Saint Helena
    """
    KNA = "KNA"
    """
    Saint Kitts and Nevis
    """
    LCA = "LCA"
    """
    Saint Lucia
    """
    MAF = "MAF"
    """
    Saint-Martin (French part)
    """
    SPM = "SPM"
    """
    Saint Pierre and Miquelon
    """
    VCT = "VCT"
    """
    Saint Vincent and Grenadines
    """
    WSM = "WSM"
    """
    Samoa
    """
    SMR = "SMR"
    """
    San Marino
    """
    STP = "STP"
    """
    Sao Tome and Principe
    """
    SAU = "SAU"
    """
    Saudi Arabia
    """
    SEN = "SEN"
    """
    Senegal
    """
    SRB = "SRB"
    """
    Serbia
    """
    SYC = "SYC"
    """
    Seychelles
    """
    SLE = "SLE"
    """
    Sierra Leone
    """
    SGP = "SGP"
    """
    Singapore
    """
    SVK = "SVK"
    """
    Slovakia
    """
    SVN = "SVN"
    """
    Slovenia
    """
    SLB = "SLB"
    """
    Solomon Islands
    """
    SOM = "SOM"
    """
    Somalia
    """
    ZAF = "ZAF"
    """
    South Africa
    """
    SGS = "SGS"
    """
    South Georgia and the South Sandwich Islands
    """
    SSD = "SSD"
    """
    South Sudan
    """
    ESP = "ESP"
    """
    Spain
    """
    LKA = "LKA"
    """
    Sri Lanka
    """
    SDN = "SDN"
    """
    Sudan
    """
    SUR = "SUR"
    """
    Suriname
    """
    SJM = "SJM"
    """
    Svalbard and Jan Mayen Islands
    """
    SWZ = "SWZ"
    """
    Swaziland
    """
    SWE = "SWE"
    """
    Sweden
    """
    CHE = "CHE"
    """
    Switzerland
    """
    SYR = "SYR"
    """
    Syrian Arab Republic (Syria)
    """
    TWN = "TWN"
    """
    Taiwan, Republic of China
    """
    TJK = "TJK"
    """
    Tajikistan
    """
    TZA = "TZA"
    """
    Tanzania, United Republic of
    """
    THA = "THA"
    """
    Thailand
    """
    TLS = "TLS"
    """
    Timor-Leste
    """
    TGO = "TGO"
    """
    Togo
    """
    TKL = "TKL"
    """
    Tokelau
    """
    TON = "TON"
    """
    Tonga
    """
    TTO = "TTO"
    """
    Trinidad and Tobago
    """
    TUN = "TUN"
    """
    Tunisia
    """
    TUR = "TUR"
    """
    Turkey
    """
    TKM = "TKM"
    """
    Turkmenistan
    """
    TCA = "TCA"
    """
    Turks and Caicos Islands
    """
    TUV = "TUV"
    """
    Tuvalu
    """
    UGA = "UGA"
    """
    Uganda
    """
    UKR = "UKR"
    """
    Ukraine
    """
    ARE = "ARE"
    """
    United Arab Emirates
    """
    GBR = "GBR"
    """
    United Kingdom
    """
    USA = "USA"
    """
    United States of America
    """
    UMI = "UMI"
    """
    US Minor Outlying Islands
    """
    URY = "URY"
    """
    Uruguay
    """
    UZB = "UZB"
    """
    Uzbekistan
    """
    VUT = "VUT"
    """
    Vanuatu
    """
    VEN = "VEN"
    """
    Venezuela (Bolivarian Republic)
    """
    VNM = "VNM"
    """
    Viet Nam
    """
    VIR = "VIR"
    """
    Virgin Islands, US
    """
    WLF = "WLF"
    """
    Wallis and Futuna Islands
    """
    ESH = "ESH"
    """
    Western Sahara
    """
    YEM = "YEM"
    """
    Yemen
    """
    ZMB = "ZMB"
    """
    Zambia
    """
    ZWE = "ZWE"
    """
    Zimbabwe
    """



class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/FoodDataCentral/mifc'})

    pass


class Food(NamedThing):
    """
    Metadata about foods analyzed for components of nutritional interest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Food',
         'from_schema': 'https://w3id.org/FoodDataCentral/mifc',
         'id_prefixes': ['mifc'],
         'in_subset': ['RequiredSubset', 'RecommendedSubset']})

    food_sample_id: str = Field(default=..., description="""A string denoting the primary identifier for a sample of the class Food. Note that food_sample_id should be unique in a given dataset and should be used to relate Food and Component records via component_sample_id from the Component class.""", json_schema_extra = { "linkml_meta": {'comments': ['Instead of `identifier: true` perhaps we can use unique_keys '
                      'https://linkml.io/linkml/schemas/constraints.html'],
         'domain_of': ['Food'],
         'examples': [{'value': 'CY121UM'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    food_description_label: str = Field(default=..., description="""A string clearly and unambiguous describing the sampled primary food material, in accordance with globally accepted guidelines for the description of foods.""", json_schema_extra = { "linkml_meta": {'comments': ["For reference see book by Greenfield and Southgate 'Food "
                      "Composition Data: Production Management and Use' ISBN-10 "
                      '9251049491 and cited literature'],
         'domain_of': ['Food'],
         'examples': [{'value': 'Yam, raw'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    food_primary_type: Optional[str] = Field(default=None, description="""A controlled vocabulary term representing the primary food material which was sampled.""", json_schema_extra = { "linkml_meta": {'comments': ['The food_primary_type could be sourced from one of various food '
                      "vocabularies such as USDA's FDC vocabulary, FoodEx2, LanguaL, "
                      'or FoodOn.'],
         'domain_of': ['Food'],
         'exact_mappings': ['FDC:NDB_number'],
         'examples': [{'value': 'FOODON:03311865'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True,
         'slot_uri': 'schema:name'} })
    food_primary_type_label: Optional[str] = Field(default=None, description="""A string denoting the label of a controlled vocabulary term representing the primary food material which was sampled.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['PTFI:Specimen_Food_Product_Name'],
         'comments': ['This field is to be used only for the string labels of from '
                      'controlled vocabulary terms which are mapped to the '
                      'food_description_label.'],
         'domain_of': ['Food'],
         'examples': [{'value': 'piece of chicken (raw)'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_primary_type_scientific_name: Optional[str] = Field(default=None, description="""A string denoting the scientific name, (in binomial nomenclature) of an organism that a food material is primarily composed of.""", json_schema_extra = { "linkml_meta": {'comments': ['This slot should only be used in cases where food materials are '
                      'single ingredient foods or have a limited number of additives '
                      'e.g. "salted Nori seaweed" or "filleted anchovies canned in '
                      'oil".'],
         'domain_of': ['Food'],
         'examples': [{'value': 'Gallus gallus'}]} })
    food_primary_type_cultivar_name: Optional[str] = Field(default=None, description="""A string denoting the cultivar name of the primary food material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'Adirondack Blue'}]} })
    food_primary_type_animal_breed_name: Optional[str] = Field(default=None, description="""A string denoting the breed name of the primary food material.""", json_schema_extra = { "linkml_meta": {'comments': ['This slot should only be used in cases where food material is '
                      'an animal with a recognizable breed name that is managed by a '
                      'national breed registry, breed association, or similar '
                      'organization. E.g., "Wagyu" for the Wagu cattle breed.'],
         'domain_of': ['Food'],
         'examples': [{'value': 'Wagyu'}]} })
    food_primary_type_ncbi_taxon_id: Optional[str] = Field(default=None, description="""A curie from the ontology representation of the NCBI organismal taxonomy (NCBITaxon) describing the taxonomic identifier of the primary food material.""", json_schema_extra = { "linkml_meta": {'comments': ['To do specify an NCBITaxon curie as the range for the slot.'],
         'domain_of': ['Food'],
         'examples': [{'value': 'NCBITaxon:9031'}]} })
    food_description_match_type: Optional[SkosMatchType] = Field(default=None, description="""A value from a controlled vocabulary term representing the type of mapping between the food_description_label and food_primary_type_label.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that the subject is the food_description_label and the '
                      'object is food_primary_type_label',
                      'See '
                      'https://github.com/mapping-commons/sssom/blob/master/src/sssom_schema/schema/sssom_schema.yaml'],
         'domain_of': ['Food'],
         'examples': [{'description': 'Mappings assessed to indicate a high degree of '
                                      'confidence that the concepts expressed in the '
                                      'subject and object terms can be used '
                                      'interchangeably. In SKOS this is described as '
                                      'following the transitive property.',
                       'value': 'skos:exactMatch'},
                      {'description': 'Mappings between the subject and object terms '
                                      'that convey a high degree of similarity, but '
                                      'are not exactly the same or interchangeable.',
                       'value': 'skos:closeMatch'},
                      {'description': 'Mappings between a subject and object terms, '
                                      'where the object term is above the subject '
                                      'within a concept hierarchy.',
                       'value': 'skos:broadMatch'},
                      {'description': 'Mappings between a subject and object terms, '
                                      'where the object term that is below the subject '
                                      'within a concept hierarchy.',
                       'value': 'skos:narrowMatch'},
                      {'description': 'Mappings between subject and object terms that '
                                      'might have some association but are not clearly '
                                      'not referring to the the same or similar '
                                      'concepts.',
                       'value': 'skos:relatedMatch'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_upc_code: Optional[str] = Field(default=None, description="""An string denoting a Universal Product Code (UPC) barcode of a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': '40822011143'}]} })
    food_preservation_state: Optional[list[FoodPreservationState]] = Field(default=[], description="""One or multiple values from an enumerated set of controlled vocabulary terms representing the preservation state(s) of a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'examples': [{'value': '[raw]'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_storage_temperature_state: Optional[list[FoodStorageTemperatureState]] = Field(default=[], description="""One or multiple values from an enumerated set of controlled vocabulary terms representing the qualitative temperature state at which a food sample was stored prior to acquisition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'examples': [{'value': '[frozen]'}, {'value': '[frozen|refrigerated]'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_ripeness_state: Optional[FoodRipenessState] = Field(default=None, description="""A value from a enumerated set of controlled vocabulary terms representing the qualitative freshness state of a food sample when prepared for analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'unripe'}]} })
    food_cooking_method: Optional[list[FoodCookingMethod]] = Field(default=[], description="""One or multiple values from an enumerated set of controlled vocabulary terms representing the any cooking method(s) applied to a food sample prior to analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'examples': [{'value': '[boiled|steamed]'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_origin_country: Optional[CountryCode] = Field(default=None, description="""A value from an enumerated set of controlled vocabulary terms denoting denoting the country code from which a food sample originates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'AFG'}]} })
    food_acquisition_city: Optional[str] = Field(default=None, description="""A string denoting the city in which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['PTFI:Collection_Location'],
         'domain_of': ['Food'],
         'examples': [{'value': 'Tucson'}]} })
    food_acquisition_country: Optional[CountryCode] = Field(default=None, description="""A value from an enumerated set of controlled vocabulary terms denoting denoting the country code from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'examples': [{'value': 'AFG'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_acquisition_country_subdivision: Optional[str] = Field(default=None, description="""A string denoting the country subdivision (state or province) from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'PA'}]} })
    food_acquisition_date: Optional[date] = Field(default=None, description="""A date value representing the date a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'exact_mappings': ['PTFI:Collection_Date'],
         'examples': [{'value': '2023-03-08'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_acquisition_year: Optional[str] = Field(default=None, description="""A string value representing the year a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'comments': ['When possible food_acquisition_date should be used instead of '
                      'food_acquisition_date_year.'],
         'domain_of': ['Food'],
         'examples': [{'value': '2011'}]} })
    food_acquisition_location_type: Optional[FoodAcquisitionLocationType] = Field(default=None, description="""A value from an enumerated set of controlled vocabulary terms describing the type of location from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'exact_mappings': ['PTFI:Collection_Type'],
         'examples': [{'value': 'supermarket'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    food_acquisition_location_name: Optional[str] = Field(default=None, description="""A string describing the name of the location from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'Safeway'}]} })
    food_acquisition_latitude: Optional[float] = Field(default=None, description="""A float representing the latitude of the place from which the food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'exact_mappings': ['PTFI:Collection_Latitude'],
         'examples': [{'value': '25.761681'}]} })
    food_acquisition_longitude: Optional[float] = Field(default=None, description="""A float representing the longitude of the place from which the food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'exact_mappings': ['PTFI:Collection_Longitude'],
         'examples': [{'value': '-80.191788'}]} })
    food_acquisition_agent_name: Optional[str] = Field(default=None, description="""A string denoting the name of the agent (person, device or other type of service) that acquired the food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'exact_mappings': ['PTFI:Collector_Name'],
         'examples': [{'value': 'Denise Trainer'}]} })
    food_acquisition_organization: Optional[str] = Field(default=None, description="""A string denoting the name of the organization responsible for acquired the food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'exact_mappings': ['PTFI:Collector_Organization'],
         'examples': [{'value': 'USDA Food for Health of People and the Environment '
                                'Laboratory'}]} })
    food_distributor_city: Optional[str] = Field(default=None, description="""A string denoting the city of a distributor organization from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'Veracruz'}]} })
    food_distributor_country: Optional[CountryCode] = Field(default=None, description="""A value from an enumerated set of controlled vocabulary terms denoting denoting the country code of a distributor organization from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'AFG'}]} })
    food_distributor_country_subdivision: Optional[str] = Field(default=None, description="""A string denoting the country subdivision (state or province) of a distributor organization from which a food sample was acquired.""", json_schema_extra = { "linkml_meta": {'comments': ['To be determined if state codes should be specified over full '
                      'names of states/provinces for countries globally.'],
         'domain_of': ['Food'],
         'examples': [{'value': 'Ohio'}]} })
    food_expiration_date: Optional[date] = Field(default=None, description="""A date value representing the food expiration date as shown on the labeling information of the food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': '2023-03-08'}]} })
    food_label_date: Optional[date] = Field(default=None, description="""A date value representing the food label date as shown on the labeling information of the food sample.""", json_schema_extra = { "linkml_meta": {'comments': ['This field can be used in cases where it is unclear if a label '
                      'date is an expiration date, sell by date, use by or other date '
                      'on a product label.'],
         'domain_of': ['Food'],
         'examples': [{'value': '2023-03-08'}]} })
    food_sell_by_date: Optional[date] = Field(default=None, description="""A date value representing a date that indicates to stores how long to display a food product for sale for inventory management purposes.""", json_schema_extra = { "linkml_meta": {'comments': ['Definition sourced from '
                      'https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/food-product-dating.'],
         'domain_of': ['Food'],
         'examples': [{'value': '2023-03-08'}]} })
    food_category_label: Optional[str] = Field(default=None, description="""A string or controlled vocabulary denoting the label of the food group or category of the primary food material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'Beverages'}]} })
    food_category_type: Optional[str] = Field(default=None, description="""A controlled vocabulary term representing the category of the food material that was sampled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'FOOD:1400'}]} })
    food_additional_types: Optional[list[str]] = Field(default=[], description="""A list of controlled vocabulary denoting the label(s) of additional food types, not including the food_primary_type that are in a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'examples': [{'value': '[wheat flour (enriched)|syrup|water|salt]'}]} })
    food_brand_name: Optional[str] = Field(default=None, description="""A string denoting a name identifying a product, service, or organization selling and or distributing the primary food material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': "Bob's Red Mill"}]} })
    food_lot_number: Optional[str] = Field(default=None, description="""A string denoting the identifying lot number number assigned by a manufacturer to a particular quantity, (or lot) of the sampled primary food material.""", json_schema_extra = { "linkml_meta": {'comments': ['A lot number can also be referred to as lot code.'],
         'domain_of': ['Food'],
         'examples': [{'value': '9500'}]} })
    food_label_weight: Optional[float] = Field(default=None, description="""A float denoting the mass, (or weight on earth) as specified on the product label of a sampled primary food material.""", json_schema_extra = { "linkml_meta": {'comments': ['This field should be used in along with '
                      'food_acquisition_label_weight_unit to express the units the '
                      'food_label_weight was measured.'],
         'domain_of': ['Food'],
         'examples': [{'value': '24'}]} })
    food_label_weight_unit: Optional[str] = Field(default=None, description="""A unit code representing the unit of measurement in which a food_label_weight is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': '[oz_av]'}]} })
    food_sample_publication_date: Optional[str] = Field(default=None, description="""A date value representing the date in which a food sample was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': '2020-10-30'}]} })
    food_comment: Optional[str] = Field(default=None, description="""A string representing a comment relating to a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'],
         'examples': [{'value': 'Bananas where green at time of sampling and yellow at '
                                'the time of analysis.'}]} })
    food_sample_weight: Optional[float] = Field(default=None, description="""A float denoting the mass, (or weight on earth) of a food sample.""", json_schema_extra = { "linkml_meta": {'comments': ['This field should be used in along with food_sample_weight_unit '
                      'to express the units the food_sample_weight was measured in.'],
         'domain_of': ['Food'],
         'examples': [{'value': '304'}]} })
    food_sample_weight_unit: Optional[str] = Field(default=None, description="""A unit code representing the unit of measurement in which a food_sample_weight_unit is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'g'}]} })
    food_sample_digested_weight: Optional[float] = Field(default=None, description="""A float denoting the mass, (or weight on earth) of a food sample after being subject to a chemical or enzymatic digestion process prior to analysis of components of nutritional interest.""", json_schema_extra = { "linkml_meta": {'comments': ['This field should be used in along with '
                      'food_sample_digested_weight_unit to express the units the '
                      'food_sample_digested_weight was measured in.'],
         'domain_of': ['Food'],
         'examples': [{'value': '209'}]} })
    food_sample_digested_weight_unit: Optional[str] = Field(default=None, description="""A unit code representing the unit of measurement in which a food_sample_digested_weight is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Food'], 'examples': [{'value': 'g'}]} })


class Component(NamedThing):
    """
    Metadata about components of nutritional interest measured from foods.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Component',
         'from_schema': 'https://w3id.org/FoodDataCentral/mifc',
         'in_subset': ['RequiredSubset', 'RecommendedSubset']})

    component_sample_id: str = Field(default=..., description="""A string denoting the primary identifier for a sample of the class Component.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that component_sample_id does not need be unique in a '
                      'given dataset and should be used to relate Food and Component '
                      'records via food_sample_id from the Food class.'],
         'domain_of': ['Component'],
         'examples': [{'value': 'CY121UM'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    component_description_label: str = Field(default=..., description="""A string clearly and unambiguous describing an analyzed component of nutritional interest analyzed from a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': 'Acetic acid'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    component_type: Optional[str] = Field(default=None, description="""A controlled vocabulary term representing the type of component of nutritional interest analyzed from a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': 'COMPONENT:1007'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    component_type_label: Optional[str] = Field(default=None, description="""A string denoting the label of a controlled vocabulary term representing an analyzed component_type from a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': 'Ash'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    component_description_match_type: Optional[SkosMatchType] = Field(default=None, description="""A value from a controlled vocabulary term representing the type of mapping between the component_description_label and component_type_label.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that the subject is the component_description_label and '
                      'the object is component_type_label',
                      'See '
                      'https://github.com/mapping-commons/sssom/blob/master/src/sssom_schema/schema/sssom_schema.yaml'],
         'domain_of': ['Component'],
         'examples': [{'description': 'Mappings assessed to indicate a high degree of '
                                      'confidence that the concepts expressed in the '
                                      'subject and object terms can be used '
                                      'interchangeably. In SKOS this is described as '
                                      'following the transitive property.',
                       'value': 'skos:exactMatch'},
                      {'description': 'Mappings between the subject and object terms '
                                      'that convey a high degree of similarity, but '
                                      'are not exactly the same or interchangeable.',
                       'value': 'skos:closeMatch'},
                      {'description': 'Mappings between a subject and object terms, '
                                      'where the object term is above the subject '
                                      'within a concept hierarchy.',
                       'value': 'skos:broadMatch'},
                      {'description': 'Mappings between a subject and object terms, '
                                      'where the object term that is below the subject '
                                      'within a concept hierarchy.',
                       'value': 'skos:narrowMatch'},
                      {'description': 'Mappings between subject and object terms that '
                                      'might have some association but are not clearly '
                                      'not referring to the the same or similar '
                                      'concepts.',
                       'value': 'skos:relatedMatch'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    component_recorded_value: float = Field(default=..., description="""A float representing a recorded value of a component of nutritional interest measured from a laboratory sample derived from a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': '0.52'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    component_measurement_unit: str = Field(default=..., description="""A unit code representing the unit of measurement in which a component_recorded_value is measured.""", json_schema_extra = { "linkml_meta": {'comments': ['TODO find a way to constrain these with valid UCUM codes '
                      'perhaps enum or recommended LINKML units docs.'],
         'domain_of': ['Component'],
         'examples': [{'value': 'g/(100.g)'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    component_data_points_number: int = Field(default=..., description="""An integer representing the number of individual samples that comprise a component sample. 1 if an individual sample >1 if an aggregation of samples.""", json_schema_extra = { "linkml_meta": {'comments': ['This slot defines if component is source from an individual '
                      'sample, or an aggregated collection of sample (a profile).'],
         'domain_of': ['Component'],
         'examples': [{'value': '7'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    component_record_date: Optional[date] = Field(default=None, description="""A date value representing recorded date pertaining to an analyzed sample.""", json_schema_extra = { "linkml_meta": {'comments': ['Allows for ambiguity of date record relative to '
                      'component_analysis_date. Use this if a date for a record is '
                      'know but it is unclear if it is specifically the date of '
                      'analysis.'],
         'domain_of': ['Component'],
         'examples': [{'value': '2023-03-08'}]} })
    component_analysis_date: Optional[date] = Field(default=None, description="""A date value representing the date in which a component of nutritional interest was analyzed.""", json_schema_extra = { "linkml_meta": {'comments': ['Use this field if the exact date of analysis is known if there '
                      'is date ambiguity use component_record_date.'],
         'domain_of': ['Component'],
         'examples': [{'value': '2023-03-08'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    component_analysis_organization: Optional[list[str]] = Field(default=[], description="""One or more string value(s) representing the name(s) of any organization(s) involved in the analysis of a component of nutritional interest from a food sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': 'USDA'}, {'value': 'Unknown manufacturer'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    component_comment: Optional[str] = Field(default=None, description="""A string representing a comment relating to an analyzed component of nutritional interest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': 'Samples were obtained from 12 retail stores using a '
                                'probability-based sampling plan. Some fish had been '
                                'treated during processing to retain moisture on '
                                'thawing. Untreated fish = 265 mg sodium/100g.'}]} })
    component_derivation_type: Optional[str] = Field(default=None, description="""A controlled vocabulary term denoting how a component of nutritional interest was generated.""", json_schema_extra = { "linkml_meta": {'comments': ['Should make an enumeration with appropriate values (e.g, '
                      'Analytical as default, Calculated, inferred/Estimated, Sourced '
                      'from literature etc)'],
         'domain_of': ['Component'],
         'examples': [{'value': 'Analytical'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    component_limit_of_quantitation: Optional[str] = Field(default=None, description="""A string representing the the level above which quantitative results may be determined with acceptable accuracy and precision. Limit of quantitation (or quantification) (LOQ) is variously defined but must be a value greater than the Method Detection Limit (MDL) and should apply to the complete analytical method.""", json_schema_extra = { "linkml_meta": {'comments': ['Description reference: '
                      'https://www.fda.gov/science-research/field-science-and-laboratories/field-science-laboratory-manual. '
                      'Alternative definition: the minimum amount/concentration that '
                      'can be quantified with acceptable precision.'],
         'domain_of': ['Component'],
         'examples': [{'value': '<0.25'}]} })
    component_limit_of_blank: Optional[float] = Field(default=None, description="""A float representing the highest apparent analyte concentration expected to be found when measuring replicates of a blank sample containing no analyte.""", json_schema_extra = { "linkml_meta": {'comments': ['Description reference from '
                      'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2556583/.'],
         'domain_of': ['Component'],
         'examples': [{'value': '0.0785'}]} })
    component_limit_of_detection: Optional[str] = Field(default=None, description="""A string representing the lowest amount of analyte in a sample which can be detected but not necessarily quantified as an exact value. It is often called the Limit Of Detection (LOD) which is the lowest concentration level that can be determined statistically different from a blank at a specified level of confidence.""", json_schema_extra = { "linkml_meta": {'comments': ['Description reference: '
                      'https://www.fda.gov/science-research/field-science-and-laboratories/field-science-laboratory-manual.'],
         'domain_of': ['Component'],
         'examples': [{'value': '<0.15'}]} })
    component_method_detection_limit: Optional[float] = Field(default=None, description="""A string representing the Method Detection Limit (MDL), the minimum concentration of a substance that can be measured and reported with 99% confidence that the analyte concentration is greater than zero. It is determined from analysis of a sample in a given matrix containing the analyte.""", json_schema_extra = { "linkml_meta": {'comments': ['Description reference: '
                      'https://www.fda.gov/science-research/field-science-and-laboratories/field-science-laboratory-manual.'],
         'domain_of': ['Component'],
         'examples': [{'value': '0.57'}]} })
    compound_trace_analysis_boolean: Optional[bool] = Field(default=None, description="""A boolean value denoting True if a measured component of nutritional is present at a very low concentration, requiring the use of precise analytical instrumentation.""", json_schema_extra = { "linkml_meta": {'comments': ['Trace analyses typically refer to analyte concentrations in the '
                      'range of parts per million, parts per billion or lower.'],
         'domain_of': ['Component'],
         'examples': [{'value': 'False'}]} })
    compound_sample_aggregation_minimum_value: Optional[float] = Field(default=None, description="""A float representing the minimum measured compound value of an aggregation of compound samples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'examples': [{'value': '0.8'}]} })
    compound_sample_aggregation_maximum_value: Optional[float] = Field(default=None, description="""A float representing the maximum measured compound value of an aggregation of compound samples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'examples': [{'value': '2.2'}]} })
    compound_sample_aggregation_median_value: Optional[float] = Field(default=None, description="""A float representing the median measured compound value of an aggregation of compound samples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'examples': [{'value': '1.5'}]} })
    compound_sample_aggregation_standard_deviation: Optional[float] = Field(default=None, description="""A float representing the standard deviation of a measured compound value of an aggregation of compound samples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'examples': [{'value': '0.61'}]} })
    compound_analytical_measurement_protocol_url: Optional[str] = Field(default=None, description="""A string denoting a uniform resource locator (URL) linking to a measurement protocol used to conduct an analytical analysis on a sample.""", json_schema_extra = { "linkml_meta": {'comments': ['Ideally a protocol with a digital object identifier (DOI) '
                      'should be used in place of a generic URL if possible.'],
         'domain_of': ['Component'],
         'examples': [{'value': 'https://doi.org/10.1093/9780197610145.003.3363'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    compound_analytical_measurement_method: Optional[CompoundAnalyticalMeasurementMethod] = Field(default=None, description="""A value from an enumerated set of controlled vocabulary terms denoting the method used to conduct an analytical analysis on a sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'],
         'examples': [{'value': 'HPLC'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    compound_analytical_laboratory_name: Optional[str] = Field(default=None, description="""A string denoting the name of a laboratory that conducted the analytical analysis of a component of nutritional interest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'examples': [{'value': 'Covance'}]} })
    component_quality_control_remeasurement: Optional[bool] = Field(default=None, description="""A boolean value denoting TRUE if a component_recorded_value was measured more than once for internal laboratory quality control purposes.""", json_schema_extra = { "linkml_meta": {'comments': ['This could be alternatively be modeled with an integer rather '
                      'than a boolean. Note this might give some issues with the way '
                      'excel saves boolean values.'],
         'domain_of': ['Component'],
         'examples': [{'value': 'False'}]} })
    compound_individual_sample_id_list: Optional[list[str]] = Field(default=[], description="""A list of component_sample_id's that were used to create a component profile.""", json_schema_extra = { "linkml_meta": {'comments': ['This would typically be the list of individual samples the '
                      'values of which were averaged to create a generic component '
                      'profile.'],
         'domain_of': ['Component'],
         'examples': [{'value': '[CY123W2|CY123W3|CY123W7|CY123W5|CY123W4|CY123W6]'}]} })
    component_atwater_protein_conversion_factor: Optional[float] = Field(default=None, description="""A float representing the protein conversion factor used to calculate the available energy of a food when employing the Atwater system or a derivative thereof.""", json_schema_extra = { "linkml_meta": {'comments': ['The Atwater general factor for protein is 4. See the USDA '
                      'Handbook 74 '
                      'https://www.ars.usda.gov/ARSUSERFILES/80400535/DATA/CLASSICS/USDA%20HANDBOOK%2074.PDF '
                      'for the calculation of energy using Atwater specific factors.'],
         'domain_of': ['Component'],
         'examples': [{'value': '2.78'}]} })
    component_atwater_fat_conversion_factor: Optional[float] = Field(default=None, description="""A float representing the fat conversion factor used to calculate the available energy of a food when employing the Atwater system or a derivative thereof.""", json_schema_extra = { "linkml_meta": {'comments': ['The Atwater general factor for fat is 9. See the USDA Handbook '
                      '74 '
                      'https://www.ars.usda.gov/ARSUSERFILES/80400535/DATA/CLASSICS/USDA%20HANDBOOK%2074.PDF '
                      'for the calculation of energy using Atwater specific factors.'],
         'domain_of': ['Component'],
         'examples': [{'value': '8.37'}]} })
    component_atwater_carbohydrate_conversion_factor: Optional[float] = Field(default=None, description="""A float representing the carbohydrate conversion factor used to calculate the available energy of a food when employing the Atwater system or a derivative thereof.""", json_schema_extra = { "linkml_meta": {'comments': ['The Atwater general factor for carbohydrates is of 4. See the '
                      'USDA Handbook 74 '
                      'https://www.ars.usda.gov/ARSUSERFILES/80400535/DATA/CLASSICS/USDA%20HANDBOOK%2074.PDF '
                      'for the calculation of energy using Atwater specific factors.'],
         'domain_of': ['Component'],
         'examples': [{'value': '3.84'}]} })
    component_protein_from_nitrogen_conversion_factor: Optional[float] = Field(default=None, description="""A float representing the nitrogen to protein conversion factor used to calculate a protein value indirectly using a measured nitrogen value.""", json_schema_extra = { "linkml_meta": {'comments': ["Also known as Jones' factors. "
                      'https://www.ars.usda.gov/ARSUserFiles/80400525/Data/Classics/cir183.pdf. '
                      'A commonly used value for the '
                      'component_protein_from_nitrogen_conversion_factor is 6.25 based '
                      'on the assumptions that all proteins have a nitrogen content of '
                      '16%, and that all nitrogen is derived from protein. It should '
                      'be noted that these assumptions might not always hold.'],
         'domain_of': ['Component'],
         'examples': [{'value': '6.38'}]} })


class Resource(NamedThing):
    """
    Supplemental data about the provenance of MIFC collection resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Resource',
         'from_schema': 'https://w3id.org/FoodDataCentral/mifc',
         'in_subset': ['RequiredSubset', 'RecommendedSubset']})

    resource_dataset_label: str = Field(default=..., description="""A string corresponding to the labeled name of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource'],
         'examples': [{'value': 'Standard Reference (SR) Legacy'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    resource_dataset_version_number: int = Field(default=..., description="""An integer corresponding to the version number of the MIFC dataset.""", json_schema_extra = { "linkml_meta": {'comments': ['This could alternatively be modeled as a version tag with a '
                      'string like with resource_mifc_version_tag.'],
         'domain_of': ['Resource'],
         'examples': [{'value': '2'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    resource_mifc_version_tag: ResourceMIFCVersionTag = Field(default=..., description="""A value from an enumerated set of controlled vocabulary terms representing a string corresponding to a named MIFC release number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource'],
         'examples': [{'value': 'v0.3.0'}],
         'in_subset': ['RequiredSubset', 'RecommendedSubset'],
         'recommended': True} })
    resource_contributor_orcid: Optional[list[str]] = Field(default=[], description="""A list of strings representing ORCIDs URLs of people who contributed to a MIFC-formatted dataset.""", json_schema_extra = { "linkml_meta": {'comments': ['See https://orcid.org/.'],
         'domain_of': ['Resource'],
         'examples': [{'value': '[https://orcid.org/0000-0003-0857-700X|https://orcid.org/0000-0002-3410-4655]'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })
    resource_organization_name: Optional[list[str]] = Field(default=[], description="""A list of strings representing the names of organizations who were involved in the creation of a MIFC-formatted dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource'],
         'examples': [{'value': '[USDA Food for Health of People and the Environment '
                                'Laboratory|University of Maryland]'}],
         'in_subset': ['RecommendedSubset'],
         'recommended': True} })


class Container(ConfiguredBaseModel):
    """
    A holder for Food, Component or Resource objects
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/FoodDataCentral/mifc', 'tree_root': True})

    foods: Optional[list[Food]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    components: Optional[list[Component]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    resources: Optional[list[Resource]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Food.model_rebuild()
Component.model_rebuild()
Resource.model_rebuild()
Container.model_rebuild()
