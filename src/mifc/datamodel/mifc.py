# Auto generated from mifc.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-03T13:42:37
# Schema: mifc
#
# id: https://w3id.org/FoodDataCentral/mifc
# description: The Minimum Information (about any) Food Composition (MIFC) data standard.
# license: CC0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
FDC = CurieNamespace('FDC', 'https://fdc.nal.usda.gov/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PTFI = CurieNamespace('PTFI', 'https://foodperiodictable.org/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIFC = CurieNamespace('mifc', 'https://w3id.org/FoodDataCentral/mifc/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = MIFC


# Types

# Class references



class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MIFC.NamedThing


@dataclass(repr=False)
class Food(NamedThing):
    """
    Metadata about foods analyzed for components of nutritional interest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Food"]
    class_class_curie: ClassVar[str] = "schema:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = MIFC.Food

    food_sample_id: str = None
    food_description_label: str = None
    food_primary_type: Optional[str] = None
    food_primary_type_label: Optional[str] = None
    food_primary_type_scientific_name: Optional[str] = None
    food_primary_type_cultivar_name: Optional[str] = None
    food_primary_type_animal_breed_name: Optional[str] = None
    food_primary_type_ncbi_taxon_id: Optional[str] = None
    food_description_match_type: Optional[Union[str, "SkosMatchType"]] = None
    food_upc_code: Optional[str] = None
    food_preservation_state: Optional[Union[Union[str, "FoodPreservationState"], list[Union[str, "FoodPreservationState"]]]] = empty_list()
    food_storage_temperature_state: Optional[Union[Union[str, "FoodStorageTemperatureState"], list[Union[str, "FoodStorageTemperatureState"]]]] = empty_list()
    food_ripeness_state: Optional[Union[str, "FoodRipenessState"]] = None
    food_cooking_method: Optional[Union[Union[str, "FoodCookingMethod"], list[Union[str, "FoodCookingMethod"]]]] = empty_list()
    food_origin_country: Optional[Union[str, "CountryCode"]] = None
    food_acquisition_city: Optional[str] = None
    food_acquisition_country: Optional[Union[str, "CountryCode"]] = None
    food_acquisition_country_subdivision: Optional[str] = None
    food_acquisition_date: Optional[Union[str, XSDDate]] = None
    food_acquisition_year: Optional[str] = None
    food_acquisition_location_type: Optional[Union[str, "FoodAcquisitionLocationType"]] = None
    food_acquisition_location_name: Optional[str] = None
    food_acquisition_latitude: Optional[float] = None
    food_acquisition_longitude: Optional[float] = None
    food_acquisition_agent_name: Optional[str] = None
    food_acquisition_organization: Optional[str] = None
    food_distributor_city: Optional[str] = None
    food_distributor_country: Optional[Union[str, "CountryCode"]] = None
    food_distributor_country_subdivision: Optional[str] = None
    food_expiration_date: Optional[Union[str, XSDDate]] = None
    food_label_date: Optional[Union[str, XSDDate]] = None
    food_sell_by_date: Optional[Union[str, XSDDate]] = None
    food_category_label: Optional[str] = None
    food_category_type: Optional[str] = None
    food_additional_types: Optional[Union[str, list[str]]] = empty_list()
    food_brand_name: Optional[str] = None
    food_lot_number: Optional[str] = None
    food_label_weight: Optional[float] = None
    food_label_weight_unit: Optional[str] = None
    food_sample_publication_date: Optional[str] = None
    food_comment: Optional[str] = None
    food_sample_weight: Optional[float] = None
    food_sample_weight_unit: Optional[str] = None
    food_sample_digested_weight: Optional[float] = None
    food_sample_digested_weight_unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.food_sample_id):
            self.MissingRequiredField("food_sample_id")
        if not isinstance(self.food_sample_id, str):
            self.food_sample_id = str(self.food_sample_id)

        if self._is_empty(self.food_description_label):
            self.MissingRequiredField("food_description_label")
        if not isinstance(self.food_description_label, str):
            self.food_description_label = str(self.food_description_label)

        if self.food_primary_type is not None and not isinstance(self.food_primary_type, str):
            self.food_primary_type = str(self.food_primary_type)

        if self.food_primary_type_label is not None and not isinstance(self.food_primary_type_label, str):
            self.food_primary_type_label = str(self.food_primary_type_label)

        if self.food_primary_type_scientific_name is not None and not isinstance(self.food_primary_type_scientific_name, str):
            self.food_primary_type_scientific_name = str(self.food_primary_type_scientific_name)

        if self.food_primary_type_cultivar_name is not None and not isinstance(self.food_primary_type_cultivar_name, str):
            self.food_primary_type_cultivar_name = str(self.food_primary_type_cultivar_name)

        if self.food_primary_type_animal_breed_name is not None and not isinstance(self.food_primary_type_animal_breed_name, str):
            self.food_primary_type_animal_breed_name = str(self.food_primary_type_animal_breed_name)

        if self.food_primary_type_ncbi_taxon_id is not None and not isinstance(self.food_primary_type_ncbi_taxon_id, str):
            self.food_primary_type_ncbi_taxon_id = str(self.food_primary_type_ncbi_taxon_id)

        if self.food_description_match_type is not None and not isinstance(self.food_description_match_type, SkosMatchType):
            self.food_description_match_type = SkosMatchType(self.food_description_match_type)

        if self.food_upc_code is not None and not isinstance(self.food_upc_code, str):
            self.food_upc_code = str(self.food_upc_code)

        if not isinstance(self.food_preservation_state, list):
            self.food_preservation_state = [self.food_preservation_state] if self.food_preservation_state is not None else []
        self.food_preservation_state = [v if isinstance(v, FoodPreservationState) else FoodPreservationState(v) for v in self.food_preservation_state]

        if not isinstance(self.food_storage_temperature_state, list):
            self.food_storage_temperature_state = [self.food_storage_temperature_state] if self.food_storage_temperature_state is not None else []
        self.food_storage_temperature_state = [v if isinstance(v, FoodStorageTemperatureState) else FoodStorageTemperatureState(v) for v in self.food_storage_temperature_state]

        if self.food_ripeness_state is not None and not isinstance(self.food_ripeness_state, FoodRipenessState):
            self.food_ripeness_state = FoodRipenessState(self.food_ripeness_state)

        if not isinstance(self.food_cooking_method, list):
            self.food_cooking_method = [self.food_cooking_method] if self.food_cooking_method is not None else []
        self.food_cooking_method = [v if isinstance(v, FoodCookingMethod) else FoodCookingMethod(v) for v in self.food_cooking_method]

        if self.food_origin_country is not None and not isinstance(self.food_origin_country, CountryCode):
            self.food_origin_country = CountryCode(self.food_origin_country)

        if self.food_acquisition_city is not None and not isinstance(self.food_acquisition_city, str):
            self.food_acquisition_city = str(self.food_acquisition_city)

        if self.food_acquisition_country is not None and not isinstance(self.food_acquisition_country, CountryCode):
            self.food_acquisition_country = CountryCode(self.food_acquisition_country)

        if self.food_acquisition_country_subdivision is not None and not isinstance(self.food_acquisition_country_subdivision, str):
            self.food_acquisition_country_subdivision = str(self.food_acquisition_country_subdivision)

        if self.food_acquisition_date is not None and not isinstance(self.food_acquisition_date, XSDDate):
            self.food_acquisition_date = XSDDate(self.food_acquisition_date)

        if self.food_acquisition_year is not None and not isinstance(self.food_acquisition_year, str):
            self.food_acquisition_year = str(self.food_acquisition_year)

        if self.food_acquisition_location_type is not None and not isinstance(self.food_acquisition_location_type, FoodAcquisitionLocationType):
            self.food_acquisition_location_type = FoodAcquisitionLocationType(self.food_acquisition_location_type)

        if self.food_acquisition_location_name is not None and not isinstance(self.food_acquisition_location_name, str):
            self.food_acquisition_location_name = str(self.food_acquisition_location_name)

        if self.food_acquisition_latitude is not None and not isinstance(self.food_acquisition_latitude, float):
            self.food_acquisition_latitude = float(self.food_acquisition_latitude)

        if self.food_acquisition_longitude is not None and not isinstance(self.food_acquisition_longitude, float):
            self.food_acquisition_longitude = float(self.food_acquisition_longitude)

        if self.food_acquisition_agent_name is not None and not isinstance(self.food_acquisition_agent_name, str):
            self.food_acquisition_agent_name = str(self.food_acquisition_agent_name)

        if self.food_acquisition_organization is not None and not isinstance(self.food_acquisition_organization, str):
            self.food_acquisition_organization = str(self.food_acquisition_organization)

        if self.food_distributor_city is not None and not isinstance(self.food_distributor_city, str):
            self.food_distributor_city = str(self.food_distributor_city)

        if self.food_distributor_country is not None and not isinstance(self.food_distributor_country, CountryCode):
            self.food_distributor_country = CountryCode(self.food_distributor_country)

        if self.food_distributor_country_subdivision is not None and not isinstance(self.food_distributor_country_subdivision, str):
            self.food_distributor_country_subdivision = str(self.food_distributor_country_subdivision)

        if self.food_expiration_date is not None and not isinstance(self.food_expiration_date, XSDDate):
            self.food_expiration_date = XSDDate(self.food_expiration_date)

        if self.food_label_date is not None and not isinstance(self.food_label_date, XSDDate):
            self.food_label_date = XSDDate(self.food_label_date)

        if self.food_sell_by_date is not None and not isinstance(self.food_sell_by_date, XSDDate):
            self.food_sell_by_date = XSDDate(self.food_sell_by_date)

        if self.food_category_label is not None and not isinstance(self.food_category_label, str):
            self.food_category_label = str(self.food_category_label)

        if self.food_category_type is not None and not isinstance(self.food_category_type, str):
            self.food_category_type = str(self.food_category_type)

        if not isinstance(self.food_additional_types, list):
            self.food_additional_types = [self.food_additional_types] if self.food_additional_types is not None else []
        self.food_additional_types = [v if isinstance(v, str) else str(v) for v in self.food_additional_types]

        if self.food_brand_name is not None and not isinstance(self.food_brand_name, str):
            self.food_brand_name = str(self.food_brand_name)

        if self.food_lot_number is not None and not isinstance(self.food_lot_number, str):
            self.food_lot_number = str(self.food_lot_number)

        if self.food_label_weight is not None and not isinstance(self.food_label_weight, float):
            self.food_label_weight = float(self.food_label_weight)

        if self.food_label_weight_unit is not None and not isinstance(self.food_label_weight_unit, str):
            self.food_label_weight_unit = str(self.food_label_weight_unit)

        if self.food_sample_publication_date is not None and not isinstance(self.food_sample_publication_date, str):
            self.food_sample_publication_date = str(self.food_sample_publication_date)

        if self.food_comment is not None and not isinstance(self.food_comment, str):
            self.food_comment = str(self.food_comment)

        if self.food_sample_weight is not None and not isinstance(self.food_sample_weight, float):
            self.food_sample_weight = float(self.food_sample_weight)

        if self.food_sample_weight_unit is not None and not isinstance(self.food_sample_weight_unit, str):
            self.food_sample_weight_unit = str(self.food_sample_weight_unit)

        if self.food_sample_digested_weight is not None and not isinstance(self.food_sample_digested_weight, float):
            self.food_sample_digested_weight = float(self.food_sample_digested_weight)

        if self.food_sample_digested_weight_unit is not None and not isinstance(self.food_sample_digested_weight_unit, str):
            self.food_sample_digested_weight_unit = str(self.food_sample_digested_weight_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Component(NamedThing):
    """
    Metadata about components of nutritional interest measured from foods.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Component"]
    class_class_curie: ClassVar[str] = "schema:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = MIFC.Component

    component_sample_id: str = None
    component_description_label: str = None
    component_recorded_value: float = None
    component_measurement_unit: str = None
    component_data_points_number: int = None
    component_type: Optional[str] = None
    component_type_label: Optional[str] = None
    component_description_match_type: Optional[Union[str, "SkosMatchType"]] = None
    component_record_date: Optional[Union[str, XSDDate]] = None
    component_analysis_date: Optional[Union[str, XSDDate]] = None
    component_analysis_organization: Optional[Union[str, list[str]]] = empty_list()
    component_comment: Optional[str] = None
    component_derivation_type: Optional[str] = None
    component_limit_of_quantitation: Optional[str] = None
    component_limit_of_blank: Optional[float] = None
    component_limit_of_detection: Optional[str] = None
    component_method_detection_limit: Optional[float] = None
    compound_trace_analysis_boolean: Optional[Union[bool, Bool]] = None
    compound_sample_aggregation_minimum_value: Optional[float] = None
    compound_sample_aggregation_maximum_value: Optional[float] = None
    compound_sample_aggregation_median_value: Optional[float] = None
    compound_sample_aggregation_standard_deviation: Optional[float] = None
    compound_analytical_measurement_protocol_url: Optional[str] = None
    compound_analytical_measurement_method: Optional[Union[str, "CompoundAnalyticalMeasurementMethod"]] = None
    compound_analytical_laboratory_name: Optional[str] = None
    component_quality_control_remeasurement: Optional[Union[bool, Bool]] = None
    compound_individual_sample_id_list: Optional[Union[str, list[str]]] = empty_list()
    component_atwater_protein_conversion_factor: Optional[float] = None
    component_atwater_fat_conversion_factor: Optional[float] = None
    component_atwater_carbohydrate_conversion_factor: Optional[float] = None
    component_protein_from_nitrogen_conversion_factor: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_sample_id):
            self.MissingRequiredField("component_sample_id")
        if not isinstance(self.component_sample_id, str):
            self.component_sample_id = str(self.component_sample_id)

        if self._is_empty(self.component_description_label):
            self.MissingRequiredField("component_description_label")
        if not isinstance(self.component_description_label, str):
            self.component_description_label = str(self.component_description_label)

        if self._is_empty(self.component_recorded_value):
            self.MissingRequiredField("component_recorded_value")
        if not isinstance(self.component_recorded_value, float):
            self.component_recorded_value = float(self.component_recorded_value)

        if self._is_empty(self.component_measurement_unit):
            self.MissingRequiredField("component_measurement_unit")
        if not isinstance(self.component_measurement_unit, str):
            self.component_measurement_unit = str(self.component_measurement_unit)

        if self._is_empty(self.component_data_points_number):
            self.MissingRequiredField("component_data_points_number")
        if not isinstance(self.component_data_points_number, int):
            self.component_data_points_number = int(self.component_data_points_number)

        if self.component_type is not None and not isinstance(self.component_type, str):
            self.component_type = str(self.component_type)

        if self.component_type_label is not None and not isinstance(self.component_type_label, str):
            self.component_type_label = str(self.component_type_label)

        if self.component_description_match_type is not None and not isinstance(self.component_description_match_type, SkosMatchType):
            self.component_description_match_type = SkosMatchType(self.component_description_match_type)

        if self.component_record_date is not None and not isinstance(self.component_record_date, XSDDate):
            self.component_record_date = XSDDate(self.component_record_date)

        if self.component_analysis_date is not None and not isinstance(self.component_analysis_date, XSDDate):
            self.component_analysis_date = XSDDate(self.component_analysis_date)

        if not isinstance(self.component_analysis_organization, list):
            self.component_analysis_organization = [self.component_analysis_organization] if self.component_analysis_organization is not None else []
        self.component_analysis_organization = [v if isinstance(v, str) else str(v) for v in self.component_analysis_organization]

        if self.component_comment is not None and not isinstance(self.component_comment, str):
            self.component_comment = str(self.component_comment)

        if self.component_derivation_type is not None and not isinstance(self.component_derivation_type, str):
            self.component_derivation_type = str(self.component_derivation_type)

        if self.component_limit_of_quantitation is not None and not isinstance(self.component_limit_of_quantitation, str):
            self.component_limit_of_quantitation = str(self.component_limit_of_quantitation)

        if self.component_limit_of_blank is not None and not isinstance(self.component_limit_of_blank, float):
            self.component_limit_of_blank = float(self.component_limit_of_blank)

        if self.component_limit_of_detection is not None and not isinstance(self.component_limit_of_detection, str):
            self.component_limit_of_detection = str(self.component_limit_of_detection)

        if self.component_method_detection_limit is not None and not isinstance(self.component_method_detection_limit, float):
            self.component_method_detection_limit = float(self.component_method_detection_limit)

        if self.compound_trace_analysis_boolean is not None and not isinstance(self.compound_trace_analysis_boolean, Bool):
            self.compound_trace_analysis_boolean = Bool(self.compound_trace_analysis_boolean)

        if self.compound_sample_aggregation_minimum_value is not None and not isinstance(self.compound_sample_aggregation_minimum_value, float):
            self.compound_sample_aggregation_minimum_value = float(self.compound_sample_aggregation_minimum_value)

        if self.compound_sample_aggregation_maximum_value is not None and not isinstance(self.compound_sample_aggregation_maximum_value, float):
            self.compound_sample_aggregation_maximum_value = float(self.compound_sample_aggregation_maximum_value)

        if self.compound_sample_aggregation_median_value is not None and not isinstance(self.compound_sample_aggregation_median_value, float):
            self.compound_sample_aggregation_median_value = float(self.compound_sample_aggregation_median_value)

        if self.compound_sample_aggregation_standard_deviation is not None and not isinstance(self.compound_sample_aggregation_standard_deviation, float):
            self.compound_sample_aggregation_standard_deviation = float(self.compound_sample_aggregation_standard_deviation)

        if self.compound_analytical_measurement_protocol_url is not None and not isinstance(self.compound_analytical_measurement_protocol_url, str):
            self.compound_analytical_measurement_protocol_url = str(self.compound_analytical_measurement_protocol_url)

        if self.compound_analytical_measurement_method is not None and not isinstance(self.compound_analytical_measurement_method, CompoundAnalyticalMeasurementMethod):
            self.compound_analytical_measurement_method = CompoundAnalyticalMeasurementMethod(self.compound_analytical_measurement_method)

        if self.compound_analytical_laboratory_name is not None and not isinstance(self.compound_analytical_laboratory_name, str):
            self.compound_analytical_laboratory_name = str(self.compound_analytical_laboratory_name)

        if self.component_quality_control_remeasurement is not None and not isinstance(self.component_quality_control_remeasurement, Bool):
            self.component_quality_control_remeasurement = Bool(self.component_quality_control_remeasurement)

        if not isinstance(self.compound_individual_sample_id_list, list):
            self.compound_individual_sample_id_list = [self.compound_individual_sample_id_list] if self.compound_individual_sample_id_list is not None else []
        self.compound_individual_sample_id_list = [v if isinstance(v, str) else str(v) for v in self.compound_individual_sample_id_list]

        if self.component_atwater_protein_conversion_factor is not None and not isinstance(self.component_atwater_protein_conversion_factor, float):
            self.component_atwater_protein_conversion_factor = float(self.component_atwater_protein_conversion_factor)

        if self.component_atwater_fat_conversion_factor is not None and not isinstance(self.component_atwater_fat_conversion_factor, float):
            self.component_atwater_fat_conversion_factor = float(self.component_atwater_fat_conversion_factor)

        if self.component_atwater_carbohydrate_conversion_factor is not None and not isinstance(self.component_atwater_carbohydrate_conversion_factor, float):
            self.component_atwater_carbohydrate_conversion_factor = float(self.component_atwater_carbohydrate_conversion_factor)

        if self.component_protein_from_nitrogen_conversion_factor is not None and not isinstance(self.component_protein_from_nitrogen_conversion_factor, float):
            self.component_protein_from_nitrogen_conversion_factor = float(self.component_protein_from_nitrogen_conversion_factor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(NamedThing):
    """
    Supplemental data about the provenance of MIFC collection resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Resource"]
    class_class_curie: ClassVar[str] = "schema:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = MIFC.Resource

    resource_dataset_label: str = None
    resource_dataset_version_number: int = None
    resource_mifc_version_tag: Union[str, "ResourceMIFCVersionTag"] = None
    resource_contributor_orcid: Optional[Union[str, list[str]]] = empty_list()
    resource_organization_name: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resource_dataset_label):
            self.MissingRequiredField("resource_dataset_label")
        if not isinstance(self.resource_dataset_label, str):
            self.resource_dataset_label = str(self.resource_dataset_label)

        if self._is_empty(self.resource_dataset_version_number):
            self.MissingRequiredField("resource_dataset_version_number")
        if not isinstance(self.resource_dataset_version_number, int):
            self.resource_dataset_version_number = int(self.resource_dataset_version_number)

        if self._is_empty(self.resource_mifc_version_tag):
            self.MissingRequiredField("resource_mifc_version_tag")
        if not isinstance(self.resource_mifc_version_tag, ResourceMIFCVersionTag):
            self.resource_mifc_version_tag = ResourceMIFCVersionTag(self.resource_mifc_version_tag)

        if not isinstance(self.resource_contributor_orcid, list):
            self.resource_contributor_orcid = [self.resource_contributor_orcid] if self.resource_contributor_orcid is not None else []
        self.resource_contributor_orcid = [v if isinstance(v, str) else str(v) for v in self.resource_contributor_orcid]

        if not isinstance(self.resource_organization_name, list):
            self.resource_organization_name = [self.resource_organization_name] if self.resource_organization_name is not None else []
        self.resource_organization_name = [v if isinstance(v, str) else str(v) for v in self.resource_organization_name]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Container(YAMLRoot):
    """
    A holder for Food, Component or Resource objects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIFC["Container"]
    class_class_curie: ClassVar[str] = "mifc:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = MIFC.Container

    foods: Optional[Union[Union[dict, Food], list[Union[dict, Food]]]] = empty_list()
    components: Optional[Union[Union[dict, Component], list[Union[dict, Component]]]] = empty_list()
    resources: Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.foods, list):
            self.foods = [self.foods] if self.foods is not None else []
        self.foods = [v if isinstance(v, Food) else Food(**as_dict(v)) for v in self.foods]

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, Component) else Component(**as_dict(v)) for v in self.components]

        if not isinstance(self.resources, list):
            self.resources = [self.resources] if self.resources is not None else []
        self.resources = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.resources]

        super().__post_init__(**kwargs)


# Enumerations
class CompoundAnalyticalMeasurementMethod(EnumDefinitionImpl):

    AAS = PermissibleValue(
        text="AAS",
        description="Atomic absorption spectroscopy")
    AES = PermissibleValue(
        text="AES",
        description="Atomic emission spectroscopy")
    Colorimetric = PermissibleValue(
        text="Colorimetric",
        description="Colorimetric analysis")
    Combustion = PermissibleValue(text="Combustion")
    Extraction = PermissibleValue(text="Extraction")
    Fluorometric = PermissibleValue(text="Fluorometric")
    GC = PermissibleValue(
        text="GC",
        description="Gas chromatography")
    GLC = PermissibleValue(
        text="GLC",
        description="Gas-liquid chromatography")
    Gravimetric = PermissibleValue(text="Gravimetric")
    HPLC = PermissibleValue(
        text="HPLC",
        description="High-performance liquid chromatography",
        meaning=OBI["0002116"])
    ICP = PermissibleValue(
        text="ICP",
        description="Inductively coupled plasma")
    Kjeldahl = PermissibleValue(
        text="Kjeldahl",
        description="Kjeldahl digestion")
    Nephelometric = PermissibleValue(text="Nephelometric")
    LC = PermissibleValue(
        text="LC",
        description="Liquid chromatography")
    Microbiological = PermissibleValue(
        text="Microbiological",
        description="Microbiological assay")
    Microfluorometric = PermissibleValue(text="Microfluorometric")
    Polarimetric = PermissibleValue(text="Polarimetric")

    _defn = EnumDefinition(
        name="CompoundAnalyticalMeasurementMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Enzymatic-colorimetric",
            PermissibleValue(text="Enzymatic-colorimetric"))
        setattr(cls, "Enzymatic-gravimetric",
            PermissibleValue(text="Enzymatic-gravimetric"))
        setattr(cls, "Enzymatic-spectrometric",
            PermissibleValue(text="Enzymatic-spectrometric"))
        setattr(cls, "HPAEC-PAD",
            PermissibleValue(
                text="HPAEC-PAD",
                description="High-performance anion-exchange chromatography with pulsed amperometric detection"))
        setattr(cls, "HPLC-MS/MS",
            PermissibleValue(
                text="HPLC-MS/MS",
                description="High-performance liquid chromatography with tandem mass spectrometry"))
        setattr(cls, "HPLC-UV",
            PermissibleValue(
                text="HPLC-UV",
                description="High-performance liquid chromatography with ultra-violet spectroscopy"))
        setattr(cls, "ICP-MS",
            PermissibleValue(
                text="ICP-MS",
                description="Inductively coupled plasma mass spectrometry"))
        setattr(cls, "ICP-OES",
            PermissibleValue(
                text="ICP-OES",
                description="Inductively coupled plasma optical emission spectroscopy"))
        setattr(cls, "ID-GC-MS",
            PermissibleValue(
                text="ID-GC-MS",
                description="Isotope dilution gas chromatography mass spectrometry"))
        setattr(cls, "LC-FLD",
            PermissibleValue(
                text="LC-FLD",
                description="Liquid chromatography with fluorescence detection"))
        setattr(cls, "LC-ESI-IDMS",
            PermissibleValue(
                text="LC-ESI-IDMS",
                description="Liquid chromatography with electrospray ionization-isotope dilution mass spectrometry"))

class FoodPreservationState(EnumDefinitionImpl):

    brined = PermissibleValue(text="brined")
    candied = PermissibleValue(text="candied")
    canned = PermissibleValue(text="canned")
    cured = PermissibleValue(text="cured")
    dried = PermissibleValue(text="dried")
    fermented = PermissibleValue(text="fermented")
    fresh = PermissibleValue(text="fresh")
    irradiated = PermissibleValue(text="irradiated")
    jellied = PermissibleValue(text="jellied")
    kippered = PermissibleValue(text="kippered")
    pasteurized = PermissibleValue(text="pasteurized")
    pickled = PermissibleValue(text="pickled")
    raw = PermissibleValue(text="raw")

    _defn = EnumDefinition(
        name="FoodPreservationState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "air-dried",
            PermissibleValue(text="air-dried"))
        setattr(cls, "artificially dried",
            PermissibleValue(text="artificially dried"))
        setattr(cls, "freeze-dried",
            PermissibleValue(text="freeze-dried"))
        setattr(cls, "heat treated",
            PermissibleValue(text="heat treated"))
        setattr(cls, "naturally dried",
            PermissibleValue(text="naturally dried"))
        setattr(cls, "shelf stable",
            PermissibleValue(text="shelf stable"))
        setattr(cls, "sun-dried",
            PermissibleValue(text="sun-dried"))
        setattr(cls, "ultraviolet light exposed",
            PermissibleValue(text="ultraviolet light exposed"))

class FoodStorageTemperatureState(EnumDefinitionImpl):

    chilled = PermissibleValue(text="chilled")
    frozen = PermissibleValue(text="frozen")
    refrigerated = PermissibleValue(text="refrigerated")

    _defn = EnumDefinition(
        name="FoodStorageTemperatureState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "foodsafe chilled",
            PermissibleValue(text="foodsafe chilled"))

class FoodRipenessState(EnumDefinitionImpl):

    ripe = PermissibleValue(text="ripe")
    overripe = PermissibleValue(text="overripe")
    unripe = PermissibleValue(text="unripe")

    _defn = EnumDefinition(
        name="FoodRipenessState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "slightly ripe",
            PermissibleValue(text="slightly ripe"))

class FoodAcquisitionLocationType(EnumDefinitionImpl):

    grower = PermissibleValue(text="grower")
    field = PermissibleValue(text="field")
    retailer = PermissibleValue(text="retailer")
    supermarket = PermissibleValue(text="supermarket")
    distributor = PermissibleValue(text="distributor")
    biobank = PermissibleValue(text="biobank")
    unknown = PermissibleValue(text="unknown")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="FoodAcquisitionLocationType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "fresh market",
            PermissibleValue(text="fresh market"))
        setattr(cls, "small grocery",
            PermissibleValue(text="small grocery"))

class FoodCookingMethod(EnumDefinitionImpl):

    baked = PermissibleValue(text="baked")
    blanched = PermissibleValue(text="blanched")
    boiled = PermissibleValue(text="boiled")
    braised = PermissibleValue(text="braised")
    broiled = PermissibleValue(text="broiled")
    cooked = PermissibleValue(text="cooked")
    fried = PermissibleValue(text="fried")
    grilled = PermissibleValue(text="grilled")
    heated = PermissibleValue(text="heated")
    microwaved = PermissibleValue(text="microwaved")
    parboiled = PermissibleValue(text="parboiled")
    poached = PermissibleValue(text="poached")
    precooked = PermissibleValue(text="precooked")
    refried = PermissibleValue(text="refried")
    roasted = PermissibleValue(text="roasted")
    sauteed = PermissibleValue(text="sauteed")
    simmered = PermissibleValue(text="simmered")
    smoked = PermissibleValue(text="smoked")
    steamed = PermissibleValue(text="steamed")
    stewed = PermissibleValue(text="stewed")
    toasted = PermissibleValue(text="toasted")
    uncooked = PermissibleValue(text="uncooked")
    unheated = PermissibleValue(text="unheated")

    _defn = EnumDefinition(
        name="FoodCookingMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "dry-heat cooked",
            PermissibleValue(text="dry-heat cooked"))
        setattr(cls, "dry-roasted",
            PermissibleValue(text="dry-roasted"))
        setattr(cls, "moist-heat cooked",
            PermissibleValue(text="moist-heat cooked"))
        setattr(cls, "oil-roasted",
            PermissibleValue(text="oil-roasted"))
        setattr(cls, "pan-broiled",
            PermissibleValue(text="pan-broiled"))
        setattr(cls, "pan-browned",
            PermissibleValue(text="pan-browned"))
        setattr(cls, "pan-fried",
            PermissibleValue(text="pan-fried"))
        setattr(cls, "partially fried",
            PermissibleValue(text="partially fried"))
        setattr(cls, "slow-roasted",
            PermissibleValue(text="slow-roasted"))
        setattr(cls, "spit-roasted",
            PermissibleValue(text="spit-roasted"))
        setattr(cls, "stir-fried",
            PermissibleValue(text="stir-fried"))

class SkosMatchType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SkosMatchType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "skos:exactMatch",
            PermissibleValue(
                text="skos:exactMatch",
                description="""Mappings assessed to indicate that the concepts expressed in the subject and object terms can be used interchangeably following the transitive property.""",
                meaning=SKOS["exactMatch"]))
        setattr(cls, "skos:closeMatch",
            PermissibleValue(
                text="skos:closeMatch",
                description="""Mappings between the subject and object terms that convey a high degree of similarity, but are not exactly the same or interchangeable. Assignments of closeMatch should only be used when there is no appropriate broadMatch or narrowMatch to be found within the subject and object vocabulaires.""",
                meaning=SKOS["closeMatch"]))
        setattr(cls, "skos:broadMatch",
            PermissibleValue(
                text="skos:broadMatch",
                description="""Mappings between a subject and an object term, where the object term is above the subject within a concept hierarchy. A broadMatch is the inverse of a narrowMatch.""",
                meaning=SKOS["broadMatch"]))
        setattr(cls, "skos:narrowMatch",
            PermissibleValue(
                text="skos:narrowMatch",
                description="""Mappings between a subject and an object term, where the object term that is below the subject within a concept hierarchy. A narrowMatch is the inverse of a broadMatch.""",
                meaning=SKOS["narrowMatch"]))
        setattr(cls, "skos:relatedMatch",
            PermissibleValue(
                text="skos:relatedMatch",
                description="""Mappings between subject and object terms that are not broadMatch, narrowMatch, closeMatch or exactMatch but have some association.""",
                meaning=SKOS["relatedMatch"]))

class ResourceMIFCVersionTag(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ResourceMIFCVersionTag",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "v0.1.0",
            PermissibleValue(text="v0.1.0"))
        setattr(cls, "v0.2.0",
            PermissibleValue(text="v0.2.0"))
        setattr(cls, "v0.3.0",
            PermissibleValue(text="v0.3.0"))
        setattr(cls, "v0.3.1",
            PermissibleValue(text="v0.3.1"))
        setattr(cls, "v0.3.2",
            PermissibleValue(text="v0.3.2"))

class CountryCode(EnumDefinitionImpl):

    AFG = PermissibleValue(
        text="AFG",
        description="Afghanistan")
    ALA = PermissibleValue(
        text="ALA",
        description="Aland Islands")
    ALB = PermissibleValue(
        text="ALB",
        description="Albania")
    DZA = PermissibleValue(
        text="DZA",
        description="Algeria")
    ASM = PermissibleValue(
        text="ASM",
        description="American Samoa")
    AND = PermissibleValue(
        text="AND",
        description="Andorra")
    AGO = PermissibleValue(
        text="AGO",
        description="Angola")
    AIA = PermissibleValue(
        text="AIA",
        description="Anguilla")
    ATA = PermissibleValue(
        text="ATA",
        description="Antarctica")
    ATG = PermissibleValue(
        text="ATG",
        description="Antigua and Barbuda")
    ARG = PermissibleValue(
        text="ARG",
        description="Argentina")
    ARM = PermissibleValue(
        text="ARM",
        description="Armenia")
    ABW = PermissibleValue(
        text="ABW",
        description="Aruba")
    AUS = PermissibleValue(
        text="AUS",
        description="Australia")
    AUT = PermissibleValue(
        text="AUT",
        description="Austria")
    AZE = PermissibleValue(
        text="AZE",
        description="Azerbaijan")
    BHS = PermissibleValue(
        text="BHS",
        description="Bahamas")
    BHR = PermissibleValue(
        text="BHR",
        description="Bahrain")
    BGD = PermissibleValue(
        text="BGD",
        description="Bangladesh")
    BRB = PermissibleValue(
        text="BRB",
        description="Barbados")
    BLR = PermissibleValue(
        text="BLR",
        description="Belarus")
    BEL = PermissibleValue(
        text="BEL",
        description="Belgium")
    BLZ = PermissibleValue(
        text="BLZ",
        description="Belize")
    BEN = PermissibleValue(
        text="BEN",
        description="Benin")
    BMU = PermissibleValue(
        text="BMU",
        description="Bermuda")
    BTN = PermissibleValue(
        text="BTN",
        description="Bhutan")
    BOL = PermissibleValue(
        text="BOL",
        description="Bolivia")
    BIH = PermissibleValue(
        text="BIH",
        description="Bosnia and Herzegovina")
    BWA = PermissibleValue(
        text="BWA",
        description="Botswana")
    BVT = PermissibleValue(
        text="BVT",
        description="Bouvet Island")
    BRA = PermissibleValue(
        text="BRA",
        description="Brazil")
    VGB = PermissibleValue(
        text="VGB",
        description="British Virgin Islands")
    IOT = PermissibleValue(
        text="IOT",
        description="British Indian Ocean Territory")
    BRN = PermissibleValue(
        text="BRN",
        description="Brunei Darussalam")
    BGR = PermissibleValue(
        text="BGR",
        description="Bulgaria")
    BFA = PermissibleValue(
        text="BFA",
        description="Burkina Faso")
    BDI = PermissibleValue(
        text="BDI",
        description="Burundi")
    KHM = PermissibleValue(
        text="KHM",
        description="Cambodia")
    CMR = PermissibleValue(
        text="CMR",
        description="Cameroon")
    CAN = PermissibleValue(
        text="CAN",
        description="Canada")
    CPV = PermissibleValue(
        text="CPV",
        description="Cape Verde")
    CYM = PermissibleValue(
        text="CYM",
        description="Cayman Islands")
    CAF = PermissibleValue(
        text="CAF",
        description="Central African Republic")
    TCD = PermissibleValue(
        text="TCD",
        description="Chad")
    CHL = PermissibleValue(
        text="CHL",
        description="Chile")
    CHN = PermissibleValue(
        text="CHN",
        description="China")
    HKG = PermissibleValue(
        text="HKG",
        description="Hong Kong, SAR China")
    MAC = PermissibleValue(
        text="MAC",
        description="Macao, SAR China")
    CXR = PermissibleValue(
        text="CXR",
        description="Christmas Island")
    CCK = PermissibleValue(
        text="CCK",
        description="Cocos (Keeling) Islands")
    COL = PermissibleValue(
        text="COL",
        description="Colombia")
    COM = PermissibleValue(
        text="COM",
        description="Comoros")
    COG = PermissibleValue(
        text="COG",
        description="Congo (Brazzaville)")
    COD = PermissibleValue(
        text="COD",
        description="Congo, (Kinshasa)")
    COK = PermissibleValue(
        text="COK",
        description="Cook Islands")
    CRI = PermissibleValue(
        text="CRI",
        description="Costa Rica")
    CIV = PermissibleValue(
        text="CIV",
        description="Côte d'Ivoire")
    HRV = PermissibleValue(
        text="HRV",
        description="Croatia")
    CUB = PermissibleValue(
        text="CUB",
        description="Cuba")
    CYP = PermissibleValue(
        text="CYP",
        description="Cyprus")
    CZE = PermissibleValue(
        text="CZE",
        description="Czech Republic")
    DNK = PermissibleValue(
        text="DNK",
        description="Denmark")
    DJI = PermissibleValue(
        text="DJI",
        description="Djibouti")
    DMA = PermissibleValue(
        text="DMA",
        description="Dominica")
    DOM = PermissibleValue(
        text="DOM",
        description="Dominican Republic")
    ECU = PermissibleValue(
        text="ECU",
        description="Ecuador")
    EGY = PermissibleValue(
        text="EGY",
        description="Egypt")
    SLV = PermissibleValue(
        text="SLV",
        description="El Salvador")
    GNQ = PermissibleValue(
        text="GNQ",
        description="Equatorial Guinea")
    ERI = PermissibleValue(
        text="ERI",
        description="Eritrea")
    EST = PermissibleValue(
        text="EST",
        description="Estonia")
    ETH = PermissibleValue(
        text="ETH",
        description="Ethiopia")
    FLK = PermissibleValue(
        text="FLK",
        description="Falkland Islands (Malvinas)")
    FRO = PermissibleValue(
        text="FRO",
        description="Faroe Islands")
    FJI = PermissibleValue(
        text="FJI",
        description="Fiji")
    FIN = PermissibleValue(
        text="FIN",
        description="Finland")
    FRA = PermissibleValue(
        text="FRA",
        description="France")
    GUF = PermissibleValue(
        text="GUF",
        description="French Guiana")
    PYF = PermissibleValue(
        text="PYF",
        description="French Polynesia")
    ATF = PermissibleValue(
        text="ATF",
        description="French Southern Territories")
    GAB = PermissibleValue(
        text="GAB",
        description="Gabon")
    GMB = PermissibleValue(
        text="GMB",
        description="Gambia")
    GEO = PermissibleValue(
        text="GEO",
        description="Georgia")
    DEU = PermissibleValue(
        text="DEU",
        description="Germany")
    GHA = PermissibleValue(
        text="GHA",
        description="Ghana")
    GIB = PermissibleValue(
        text="GIB",
        description="Gibraltar")
    GRC = PermissibleValue(
        text="GRC",
        description="Greece")
    GRL = PermissibleValue(
        text="GRL",
        description="Greenland")
    GRD = PermissibleValue(
        text="GRD",
        description="Grenada")
    GLP = PermissibleValue(
        text="GLP",
        description="Guadeloupe")
    GUM = PermissibleValue(
        text="GUM",
        description="Guam")
    GTM = PermissibleValue(
        text="GTM",
        description="Guatemala")
    GGY = PermissibleValue(
        text="GGY",
        description="Guernsey")
    GIN = PermissibleValue(
        text="GIN",
        description="Guinea")
    GNB = PermissibleValue(
        text="GNB",
        description="Guinea-Bissau")
    GUY = PermissibleValue(
        text="GUY",
        description="Guyana")
    HTI = PermissibleValue(
        text="HTI",
        description="Haiti")
    HMD = PermissibleValue(
        text="HMD",
        description="Heard and Mcdonald Islands")
    VAT = PermissibleValue(
        text="VAT",
        description="Holy See (Vatican City State)")
    HND = PermissibleValue(
        text="HND",
        description="Honduras")
    HUN = PermissibleValue(
        text="HUN",
        description="Hungary")
    ISL = PermissibleValue(
        text="ISL",
        description="Iceland")
    IND = PermissibleValue(
        text="IND",
        description="India")
    IDN = PermissibleValue(
        text="IDN",
        description="Indonesia")
    IRN = PermissibleValue(
        text="IRN",
        description="Iran, Islamic Republic of")
    IRQ = PermissibleValue(
        text="IRQ",
        description="Iraq")
    IRL = PermissibleValue(
        text="IRL",
        description="Ireland")
    IMN = PermissibleValue(
        text="IMN",
        description="Isle of Man")
    ISR = PermissibleValue(
        text="ISR",
        description="Israel")
    ITA = PermissibleValue(
        text="ITA",
        description="Italy")
    JAM = PermissibleValue(
        text="JAM",
        description="Jamaica")
    JPN = PermissibleValue(
        text="JPN",
        description="Japan")
    JEY = PermissibleValue(
        text="JEY",
        description="Jersey")
    JOR = PermissibleValue(
        text="JOR",
        description="Jordan")
    KAZ = PermissibleValue(
        text="KAZ",
        description="Kazakhstan")
    KEN = PermissibleValue(
        text="KEN",
        description="Kenya")
    KIR = PermissibleValue(
        text="KIR",
        description="Kiribati")
    PRK = PermissibleValue(
        text="PRK",
        description="Korea (North)")
    KOR = PermissibleValue(
        text="KOR",
        description="Korea (South)")
    KWT = PermissibleValue(
        text="KWT",
        description="Kuwait")
    KGZ = PermissibleValue(
        text="KGZ",
        description="Kyrgyzstan")
    LAO = PermissibleValue(
        text="LAO",
        description="Lao PDR")
    LVA = PermissibleValue(
        text="LVA",
        description="Latvia")
    LBN = PermissibleValue(
        text="LBN",
        description="Lebanon")
    LSO = PermissibleValue(
        text="LSO",
        description="Lesotho")
    LBR = PermissibleValue(
        text="LBR",
        description="Liberia")
    LBY = PermissibleValue(
        text="LBY",
        description="Libya")
    LIE = PermissibleValue(
        text="LIE",
        description="Liechtenstein")
    LTU = PermissibleValue(
        text="LTU",
        description="Lithuania")
    LUX = PermissibleValue(
        text="LUX",
        description="Luxembourg")
    MKD = PermissibleValue(
        text="MKD",
        description="Macedonia, Republic of")
    MDG = PermissibleValue(
        text="MDG",
        description="Madagascar")
    MWI = PermissibleValue(
        text="MWI",
        description="Malawi")
    MYS = PermissibleValue(
        text="MYS",
        description="Malaysia")
    MDV = PermissibleValue(
        text="MDV",
        description="Maldives")
    MLI = PermissibleValue(
        text="MLI",
        description="Mali")
    MLT = PermissibleValue(
        text="MLT",
        description="Malta")
    MHL = PermissibleValue(
        text="MHL",
        description="Marshall Islands")
    MTQ = PermissibleValue(
        text="MTQ",
        description="Martinique")
    MRT = PermissibleValue(
        text="MRT",
        description="Mauritania")
    MUS = PermissibleValue(
        text="MUS",
        description="Mauritius")
    MYT = PermissibleValue(
        text="MYT",
        description="Mayotte")
    MEX = PermissibleValue(
        text="MEX",
        description="Mexico")
    FSM = PermissibleValue(
        text="FSM",
        description="Micronesia, Federated States of")
    MDA = PermissibleValue(
        text="MDA",
        description="Moldova")
    MCO = PermissibleValue(
        text="MCO",
        description="Monaco")
    MNG = PermissibleValue(
        text="MNG",
        description="Mongolia")
    MNE = PermissibleValue(
        text="MNE",
        description="Montenegro")
    MSR = PermissibleValue(
        text="MSR",
        description="Montserrat")
    MAR = PermissibleValue(
        text="MAR",
        description="Morocco")
    MOZ = PermissibleValue(
        text="MOZ",
        description="Mozambique")
    MMR = PermissibleValue(
        text="MMR",
        description="Myanmar")
    NAM = PermissibleValue(
        text="NAM",
        description="Namibia")
    NRU = PermissibleValue(
        text="NRU",
        description="Nauru")
    NPL = PermissibleValue(
        text="NPL",
        description="Nepal")
    NLD = PermissibleValue(
        text="NLD",
        description="Netherlands")
    ANT = PermissibleValue(
        text="ANT",
        description="Netherlands Antilles")
    NCL = PermissibleValue(
        text="NCL",
        description="New Caledonia")
    NZL = PermissibleValue(
        text="NZL",
        description="New Zealand")
    NIC = PermissibleValue(
        text="NIC",
        description="Nicaragua")
    NER = PermissibleValue(
        text="NER",
        description="Niger")
    NGA = PermissibleValue(
        text="NGA",
        description="Nigeria")
    NIU = PermissibleValue(
        text="NIU",
        description="Niue")
    NFK = PermissibleValue(
        text="NFK",
        description="Norfolk Island")
    MNP = PermissibleValue(
        text="MNP",
        description="Northern Mariana Islands")
    NOR = PermissibleValue(
        text="NOR",
        description="Norway")
    OMN = PermissibleValue(
        text="OMN",
        description="Oman")
    PAK = PermissibleValue(
        text="PAK",
        description="Pakistan")
    PLW = PermissibleValue(
        text="PLW",
        description="Palau")
    PSE = PermissibleValue(
        text="PSE",
        description="Palestinian Territory")
    PAN = PermissibleValue(
        text="PAN",
        description="Panama")
    PNG = PermissibleValue(
        text="PNG",
        description="Papua New Guinea")
    PRY = PermissibleValue(
        text="PRY",
        description="Paraguay")
    PER = PermissibleValue(
        text="PER",
        description="Peru")
    PHL = PermissibleValue(
        text="PHL",
        description="Philippines")
    PCN = PermissibleValue(
        text="PCN",
        description="Pitcairn")
    POL = PermissibleValue(
        text="POL",
        description="Poland")
    PRT = PermissibleValue(
        text="PRT",
        description="Portugal")
    PRI = PermissibleValue(
        text="PRI",
        description="Puerto Rico")
    QAT = PermissibleValue(
        text="QAT",
        description="Qatar")
    REU = PermissibleValue(
        text="REU",
        description="Réunion")
    ROU = PermissibleValue(
        text="ROU",
        description="Romania")
    RUS = PermissibleValue(
        text="RUS",
        description="Russian Federation")
    RWA = PermissibleValue(
        text="RWA",
        description="Rwanda")
    BLM = PermissibleValue(
        text="BLM",
        description="Saint-Barthélemy")
    SHN = PermissibleValue(
        text="SHN",
        description="Saint Helena")
    KNA = PermissibleValue(
        text="KNA",
        description="Saint Kitts and Nevis")
    LCA = PermissibleValue(
        text="LCA",
        description="Saint Lucia")
    MAF = PermissibleValue(
        text="MAF",
        description="Saint-Martin (French part)")
    SPM = PermissibleValue(
        text="SPM",
        description="Saint Pierre and Miquelon")
    VCT = PermissibleValue(
        text="VCT",
        description="Saint Vincent and Grenadines")
    WSM = PermissibleValue(
        text="WSM",
        description="Samoa")
    SMR = PermissibleValue(
        text="SMR",
        description="San Marino")
    STP = PermissibleValue(
        text="STP",
        description="Sao Tome and Principe")
    SAU = PermissibleValue(
        text="SAU",
        description="Saudi Arabia")
    SEN = PermissibleValue(
        text="SEN",
        description="Senegal")
    SRB = PermissibleValue(
        text="SRB",
        description="Serbia")
    SYC = PermissibleValue(
        text="SYC",
        description="Seychelles")
    SLE = PermissibleValue(
        text="SLE",
        description="Sierra Leone")
    SGP = PermissibleValue(
        text="SGP",
        description="Singapore")
    SVK = PermissibleValue(
        text="SVK",
        description="Slovakia")
    SVN = PermissibleValue(
        text="SVN",
        description="Slovenia")
    SLB = PermissibleValue(
        text="SLB",
        description="Solomon Islands")
    SOM = PermissibleValue(
        text="SOM",
        description="Somalia")
    ZAF = PermissibleValue(
        text="ZAF",
        description="South Africa")
    SGS = PermissibleValue(
        text="SGS",
        description="South Georgia and the South Sandwich Islands")
    SSD = PermissibleValue(
        text="SSD",
        description="South Sudan")
    ESP = PermissibleValue(
        text="ESP",
        description="Spain")
    LKA = PermissibleValue(
        text="LKA",
        description="Sri Lanka")
    SDN = PermissibleValue(
        text="SDN",
        description="Sudan")
    SUR = PermissibleValue(
        text="SUR",
        description="Suriname")
    SJM = PermissibleValue(
        text="SJM",
        description="Svalbard and Jan Mayen Islands")
    SWZ = PermissibleValue(
        text="SWZ",
        description="Swaziland")
    SWE = PermissibleValue(
        text="SWE",
        description="Sweden")
    CHE = PermissibleValue(
        text="CHE",
        description="Switzerland")
    SYR = PermissibleValue(
        text="SYR",
        description="Syrian Arab Republic (Syria)")
    TWN = PermissibleValue(
        text="TWN",
        description="Taiwan, Republic of China")
    TJK = PermissibleValue(
        text="TJK",
        description="Tajikistan")
    TZA = PermissibleValue(
        text="TZA",
        description="Tanzania, United Republic of")
    THA = PermissibleValue(
        text="THA",
        description="Thailand")
    TLS = PermissibleValue(
        text="TLS",
        description="Timor-Leste")
    TGO = PermissibleValue(
        text="TGO",
        description="Togo")
    TKL = PermissibleValue(
        text="TKL",
        description="Tokelau")
    TON = PermissibleValue(
        text="TON",
        description="Tonga")
    TTO = PermissibleValue(
        text="TTO",
        description="Trinidad and Tobago")
    TUN = PermissibleValue(
        text="TUN",
        description="Tunisia")
    TUR = PermissibleValue(
        text="TUR",
        description="Turkey")
    TKM = PermissibleValue(
        text="TKM",
        description="Turkmenistan")
    TCA = PermissibleValue(
        text="TCA",
        description="Turks and Caicos Islands")
    TUV = PermissibleValue(
        text="TUV",
        description="Tuvalu")
    UGA = PermissibleValue(
        text="UGA",
        description="Uganda")
    UKR = PermissibleValue(
        text="UKR",
        description="Ukraine")
    ARE = PermissibleValue(
        text="ARE",
        description="United Arab Emirates")
    GBR = PermissibleValue(
        text="GBR",
        description="United Kingdom")
    USA = PermissibleValue(
        text="USA",
        description="United States of America")
    UMI = PermissibleValue(
        text="UMI",
        description="US Minor Outlying Islands")
    URY = PermissibleValue(
        text="URY",
        description="Uruguay")
    UZB = PermissibleValue(
        text="UZB",
        description="Uzbekistan")
    VUT = PermissibleValue(
        text="VUT",
        description="Vanuatu")
    VEN = PermissibleValue(
        text="VEN",
        description="Venezuela (Bolivarian Republic)")
    VNM = PermissibleValue(
        text="VNM",
        description="Viet Nam")
    VIR = PermissibleValue(
        text="VIR",
        description="Virgin Islands, US")
    WLF = PermissibleValue(
        text="WLF",
        description="Wallis and Futuna Islands")
    ESH = PermissibleValue(
        text="ESH",
        description="Western Sahara")
    YEM = PermissibleValue(
        text="YEM",
        description="Yemen")
    ZMB = PermissibleValue(
        text="ZMB",
        description="Zambia")
    ZWE = PermissibleValue(
        text="ZWE",
        description="Zimbabwe")

    _defn = EnumDefinition(
        name="CountryCode",
    )

# Slots
class slots:
    pass

slots.food_sample_id = Slot(uri=MIFC.food_sample_id, name="food_sample_id", curie=MIFC.curie('food_sample_id'),
                   model_uri=MIFC.food_sample_id, domain=None, range=str)

slots.food_description_label = Slot(uri=MIFC.food_description_label, name="food_description_label", curie=MIFC.curie('food_description_label'),
                   model_uri=MIFC.food_description_label, domain=None, range=str)

slots.food_primary_type = Slot(uri=SCHEMA.name, name="food_primary_type", curie=SCHEMA.curie('name'),
                   model_uri=MIFC.food_primary_type, domain=None, range=Optional[str])

slots.food_description_match_type = Slot(uri=MIFC.food_description_match_type, name="food_description_match_type", curie=MIFC.curie('food_description_match_type'),
                   model_uri=MIFC.food_description_match_type, domain=None, range=Optional[Union[str, "SkosMatchType"]])

slots.food_primary_type_label = Slot(uri=MIFC.food_primary_type_label, name="food_primary_type_label", curie=MIFC.curie('food_primary_type_label'),
                   model_uri=MIFC.food_primary_type_label, domain=None, range=Optional[str])

slots.food_primary_type_scientific_name = Slot(uri=MIFC.food_primary_type_scientific_name, name="food_primary_type_scientific_name", curie=MIFC.curie('food_primary_type_scientific_name'),
                   model_uri=MIFC.food_primary_type_scientific_name, domain=None, range=Optional[str])

slots.food_primary_type_cultivar_name = Slot(uri=MIFC.food_primary_type_cultivar_name, name="food_primary_type_cultivar_name", curie=MIFC.curie('food_primary_type_cultivar_name'),
                   model_uri=MIFC.food_primary_type_cultivar_name, domain=None, range=Optional[str])

slots.food_primary_type_animal_breed_name = Slot(uri=MIFC.food_primary_type_animal_breed_name, name="food_primary_type_animal_breed_name", curie=MIFC.curie('food_primary_type_animal_breed_name'),
                   model_uri=MIFC.food_primary_type_animal_breed_name, domain=None, range=Optional[str])

slots.food_primary_type_ncbi_taxon_id = Slot(uri=MIFC.food_primary_type_ncbi_taxon_id, name="food_primary_type_ncbi_taxon_id", curie=MIFC.curie('food_primary_type_ncbi_taxon_id'),
                   model_uri=MIFC.food_primary_type_ncbi_taxon_id, domain=None, range=Optional[str])

slots.food_upc_code = Slot(uri=MIFC.food_upc_code, name="food_upc_code", curie=MIFC.curie('food_upc_code'),
                   model_uri=MIFC.food_upc_code, domain=None, range=Optional[str])

slots.food_preservation_state = Slot(uri=MIFC.food_preservation_state, name="food_preservation_state", curie=MIFC.curie('food_preservation_state'),
                   model_uri=MIFC.food_preservation_state, domain=None, range=Optional[Union[Union[str, "FoodPreservationState"], list[Union[str, "FoodPreservationState"]]]])

slots.food_storage_temperature_state = Slot(uri=MIFC.food_storage_temperature_state, name="food_storage_temperature_state", curie=MIFC.curie('food_storage_temperature_state'),
                   model_uri=MIFC.food_storage_temperature_state, domain=None, range=Optional[Union[Union[str, "FoodStorageTemperatureState"], list[Union[str, "FoodStorageTemperatureState"]]]])

slots.food_ripeness_state = Slot(uri=MIFC.food_ripeness_state, name="food_ripeness_state", curie=MIFC.curie('food_ripeness_state'),
                   model_uri=MIFC.food_ripeness_state, domain=None, range=Optional[Union[str, "FoodRipenessState"]])

slots.food_cooking_method = Slot(uri=MIFC.food_cooking_method, name="food_cooking_method", curie=MIFC.curie('food_cooking_method'),
                   model_uri=MIFC.food_cooking_method, domain=None, range=Optional[Union[Union[str, "FoodCookingMethod"], list[Union[str, "FoodCookingMethod"]]]])

slots.food_origin_country = Slot(uri=MIFC.food_origin_country, name="food_origin_country", curie=MIFC.curie('food_origin_country'),
                   model_uri=MIFC.food_origin_country, domain=None, range=Optional[Union[str, "CountryCode"]])

slots.food_acquisition_city = Slot(uri=MIFC.food_acquisition_city, name="food_acquisition_city", curie=MIFC.curie('food_acquisition_city'),
                   model_uri=MIFC.food_acquisition_city, domain=None, range=Optional[str])

slots.food_acquisition_country = Slot(uri=MIFC.food_acquisition_country, name="food_acquisition_country", curie=MIFC.curie('food_acquisition_country'),
                   model_uri=MIFC.food_acquisition_country, domain=None, range=Optional[Union[str, "CountryCode"]])

slots.food_acquisition_country_subdivision = Slot(uri=MIFC.food_acquisition_country_subdivision, name="food_acquisition_country_subdivision", curie=MIFC.curie('food_acquisition_country_subdivision'),
                   model_uri=MIFC.food_acquisition_country_subdivision, domain=None, range=Optional[str])

slots.food_acquisition_date = Slot(uri=MIFC.food_acquisition_date, name="food_acquisition_date", curie=MIFC.curie('food_acquisition_date'),
                   model_uri=MIFC.food_acquisition_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.food_acquisition_year = Slot(uri=MIFC.food_acquisition_year, name="food_acquisition_year", curie=MIFC.curie('food_acquisition_year'),
                   model_uri=MIFC.food_acquisition_year, domain=None, range=Optional[str])

slots.food_acquisition_location_type = Slot(uri=MIFC.food_acquisition_location_type, name="food_acquisition_location_type", curie=MIFC.curie('food_acquisition_location_type'),
                   model_uri=MIFC.food_acquisition_location_type, domain=None, range=Optional[Union[str, "FoodAcquisitionLocationType"]])

slots.food_acquisition_location_name = Slot(uri=MIFC.food_acquisition_location_name, name="food_acquisition_location_name", curie=MIFC.curie('food_acquisition_location_name'),
                   model_uri=MIFC.food_acquisition_location_name, domain=None, range=Optional[str])

slots.food_acquisition_latitude = Slot(uri=MIFC.food_acquisition_latitude, name="food_acquisition_latitude", curie=MIFC.curie('food_acquisition_latitude'),
                   model_uri=MIFC.food_acquisition_latitude, domain=None, range=Optional[float])

slots.food_acquisition_longitude = Slot(uri=MIFC.food_acquisition_longitude, name="food_acquisition_longitude", curie=MIFC.curie('food_acquisition_longitude'),
                   model_uri=MIFC.food_acquisition_longitude, domain=None, range=Optional[float])

slots.food_acquisition_agent_name = Slot(uri=MIFC.food_acquisition_agent_name, name="food_acquisition_agent_name", curie=MIFC.curie('food_acquisition_agent_name'),
                   model_uri=MIFC.food_acquisition_agent_name, domain=None, range=Optional[str])

slots.food_acquisition_organization = Slot(uri=MIFC.food_acquisition_organization, name="food_acquisition_organization", curie=MIFC.curie('food_acquisition_organization'),
                   model_uri=MIFC.food_acquisition_organization, domain=None, range=Optional[str])

slots.food_distributor_city = Slot(uri=MIFC.food_distributor_city, name="food_distributor_city", curie=MIFC.curie('food_distributor_city'),
                   model_uri=MIFC.food_distributor_city, domain=None, range=Optional[str])

slots.food_distributor_country = Slot(uri=MIFC.food_distributor_country, name="food_distributor_country", curie=MIFC.curie('food_distributor_country'),
                   model_uri=MIFC.food_distributor_country, domain=None, range=Optional[Union[str, "CountryCode"]])

slots.food_distributor_country_subdivision = Slot(uri=MIFC.food_distributor_country_subdivision, name="food_distributor_country_subdivision", curie=MIFC.curie('food_distributor_country_subdivision'),
                   model_uri=MIFC.food_distributor_country_subdivision, domain=None, range=Optional[str])

slots.food_label_date = Slot(uri=MIFC.food_label_date, name="food_label_date", curie=MIFC.curie('food_label_date'),
                   model_uri=MIFC.food_label_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.food_expiration_date = Slot(uri=MIFC.food_expiration_date, name="food_expiration_date", curie=MIFC.curie('food_expiration_date'),
                   model_uri=MIFC.food_expiration_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.food_sell_by_date = Slot(uri=MIFC.food_sell_by_date, name="food_sell_by_date", curie=MIFC.curie('food_sell_by_date'),
                   model_uri=MIFC.food_sell_by_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.food_category_label = Slot(uri=MIFC.food_category_label, name="food_category_label", curie=MIFC.curie('food_category_label'),
                   model_uri=MIFC.food_category_label, domain=None, range=Optional[str])

slots.food_category_type = Slot(uri=MIFC.food_category_type, name="food_category_type", curie=MIFC.curie('food_category_type'),
                   model_uri=MIFC.food_category_type, domain=None, range=Optional[str])

slots.food_additional_types = Slot(uri=MIFC.food_additional_types, name="food_additional_types", curie=MIFC.curie('food_additional_types'),
                   model_uri=MIFC.food_additional_types, domain=None, range=Optional[Union[str, list[str]]])

slots.food_brand_name = Slot(uri=MIFC.food_brand_name, name="food_brand_name", curie=MIFC.curie('food_brand_name'),
                   model_uri=MIFC.food_brand_name, domain=None, range=Optional[str])

slots.food_lot_number = Slot(uri=MIFC.food_lot_number, name="food_lot_number", curie=MIFC.curie('food_lot_number'),
                   model_uri=MIFC.food_lot_number, domain=None, range=Optional[str])

slots.food_label_weight = Slot(uri=MIFC.food_label_weight, name="food_label_weight", curie=MIFC.curie('food_label_weight'),
                   model_uri=MIFC.food_label_weight, domain=None, range=Optional[float])

slots.food_label_weight_unit = Slot(uri=MIFC.food_label_weight_unit, name="food_label_weight_unit", curie=MIFC.curie('food_label_weight_unit'),
                   model_uri=MIFC.food_label_weight_unit, domain=None, range=Optional[str])

slots.food_sample_publication_date = Slot(uri=MIFC.food_sample_publication_date, name="food_sample_publication_date", curie=MIFC.curie('food_sample_publication_date'),
                   model_uri=MIFC.food_sample_publication_date, domain=None, range=Optional[str])

slots.food_comment = Slot(uri=MIFC.food_comment, name="food_comment", curie=MIFC.curie('food_comment'),
                   model_uri=MIFC.food_comment, domain=None, range=Optional[str])

slots.food_sample_weight = Slot(uri=MIFC.food_sample_weight, name="food_sample_weight", curie=MIFC.curie('food_sample_weight'),
                   model_uri=MIFC.food_sample_weight, domain=None, range=Optional[float])

slots.food_sample_weight_unit = Slot(uri=MIFC.food_sample_weight_unit, name="food_sample_weight_unit", curie=MIFC.curie('food_sample_weight_unit'),
                   model_uri=MIFC.food_sample_weight_unit, domain=None, range=Optional[str])

slots.food_sample_digested_weight = Slot(uri=MIFC.food_sample_digested_weight, name="food_sample_digested_weight", curie=MIFC.curie('food_sample_digested_weight'),
                   model_uri=MIFC.food_sample_digested_weight, domain=None, range=Optional[float])

slots.food_sample_digested_weight_unit = Slot(uri=MIFC.food_sample_digested_weight_unit, name="food_sample_digested_weight_unit", curie=MIFC.curie('food_sample_digested_weight_unit'),
                   model_uri=MIFC.food_sample_digested_weight_unit, domain=None, range=Optional[str])

slots.component_sample_id = Slot(uri=MIFC.component_sample_id, name="component_sample_id", curie=MIFC.curie('component_sample_id'),
                   model_uri=MIFC.component_sample_id, domain=None, range=str)

slots.component_description_label = Slot(uri=MIFC.component_description_label, name="component_description_label", curie=MIFC.curie('component_description_label'),
                   model_uri=MIFC.component_description_label, domain=None, range=str)

slots.component_type = Slot(uri=MIFC.component_type, name="component_type", curie=MIFC.curie('component_type'),
                   model_uri=MIFC.component_type, domain=None, range=Optional[str])

slots.component_type_label = Slot(uri=MIFC.component_type_label, name="component_type_label", curie=MIFC.curie('component_type_label'),
                   model_uri=MIFC.component_type_label, domain=None, range=Optional[str])

slots.component_description_match_type = Slot(uri=MIFC.component_description_match_type, name="component_description_match_type", curie=MIFC.curie('component_description_match_type'),
                   model_uri=MIFC.component_description_match_type, domain=None, range=Optional[Union[str, "SkosMatchType"]])

slots.component_recorded_value = Slot(uri=MIFC.component_recorded_value, name="component_recorded_value", curie=MIFC.curie('component_recorded_value'),
                   model_uri=MIFC.component_recorded_value, domain=None, range=float)

slots.component_measurement_unit = Slot(uri=MIFC.component_measurement_unit, name="component_measurement_unit", curie=MIFC.curie('component_measurement_unit'),
                   model_uri=MIFC.component_measurement_unit, domain=None, range=str)

slots.component_data_points_number = Slot(uri=MIFC.component_data_points_number, name="component_data_points_number", curie=MIFC.curie('component_data_points_number'),
                   model_uri=MIFC.component_data_points_number, domain=None, range=int)

slots.component_record_date = Slot(uri=MIFC.component_record_date, name="component_record_date", curie=MIFC.curie('component_record_date'),
                   model_uri=MIFC.component_record_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.component_analysis_organization = Slot(uri=MIFC.component_analysis_organization, name="component_analysis_organization", curie=MIFC.curie('component_analysis_organization'),
                   model_uri=MIFC.component_analysis_organization, domain=None, range=Optional[Union[str, list[str]]])

slots.component_analysis_date = Slot(uri=MIFC.component_analysis_date, name="component_analysis_date", curie=MIFC.curie('component_analysis_date'),
                   model_uri=MIFC.component_analysis_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.component_comment = Slot(uri=MIFC.component_comment, name="component_comment", curie=MIFC.curie('component_comment'),
                   model_uri=MIFC.component_comment, domain=None, range=Optional[str])

slots.component_derivation_type = Slot(uri=MIFC.component_derivation_type, name="component_derivation_type", curie=MIFC.curie('component_derivation_type'),
                   model_uri=MIFC.component_derivation_type, domain=None, range=Optional[str])

slots.component_limit_of_quantitation = Slot(uri=MIFC.component_limit_of_quantitation, name="component_limit_of_quantitation", curie=MIFC.curie('component_limit_of_quantitation'),
                   model_uri=MIFC.component_limit_of_quantitation, domain=None, range=Optional[str])

slots.component_limit_of_blank = Slot(uri=MIFC.component_limit_of_blank, name="component_limit_of_blank", curie=MIFC.curie('component_limit_of_blank'),
                   model_uri=MIFC.component_limit_of_blank, domain=None, range=Optional[float])

slots.component_limit_of_detection = Slot(uri=MIFC.component_limit_of_detection, name="component_limit_of_detection", curie=MIFC.curie('component_limit_of_detection'),
                   model_uri=MIFC.component_limit_of_detection, domain=None, range=Optional[str])

slots.component_method_detection_limit = Slot(uri=MIFC.component_method_detection_limit, name="component_method_detection_limit", curie=MIFC.curie('component_method_detection_limit'),
                   model_uri=MIFC.component_method_detection_limit, domain=None, range=Optional[float])

slots.compound_trace_analysis_boolean = Slot(uri=MIFC.compound_trace_analysis_boolean, name="compound_trace_analysis_boolean", curie=MIFC.curie('compound_trace_analysis_boolean'),
                   model_uri=MIFC.compound_trace_analysis_boolean, domain=None, range=Optional[Union[bool, Bool]])

slots.compound_sample_aggregation_minimum_value = Slot(uri=MIFC.compound_sample_aggregation_minimum_value, name="compound_sample_aggregation_minimum_value", curie=MIFC.curie('compound_sample_aggregation_minimum_value'),
                   model_uri=MIFC.compound_sample_aggregation_minimum_value, domain=None, range=Optional[float])

slots.compound_sample_aggregation_maximum_value = Slot(uri=MIFC.compound_sample_aggregation_maximum_value, name="compound_sample_aggregation_maximum_value", curie=MIFC.curie('compound_sample_aggregation_maximum_value'),
                   model_uri=MIFC.compound_sample_aggregation_maximum_value, domain=None, range=Optional[float])

slots.compound_sample_aggregation_median_value = Slot(uri=MIFC.compound_sample_aggregation_median_value, name="compound_sample_aggregation_median_value", curie=MIFC.curie('compound_sample_aggregation_median_value'),
                   model_uri=MIFC.compound_sample_aggregation_median_value, domain=None, range=Optional[float])

slots.compound_sample_aggregation_standard_deviation = Slot(uri=MIFC.compound_sample_aggregation_standard_deviation, name="compound_sample_aggregation_standard_deviation", curie=MIFC.curie('compound_sample_aggregation_standard_deviation'),
                   model_uri=MIFC.compound_sample_aggregation_standard_deviation, domain=None, range=Optional[float])

slots.compound_analytical_measurement_protocol_url = Slot(uri=MIFC.compound_analytical_measurement_protocol_url, name="compound_analytical_measurement_protocol_url", curie=MIFC.curie('compound_analytical_measurement_protocol_url'),
                   model_uri=MIFC.compound_analytical_measurement_protocol_url, domain=None, range=Optional[str])

slots.compound_analytical_measurement_method = Slot(uri=MIFC.compound_analytical_measurement_method, name="compound_analytical_measurement_method", curie=MIFC.curie('compound_analytical_measurement_method'),
                   model_uri=MIFC.compound_analytical_measurement_method, domain=None, range=Optional[Union[str, "CompoundAnalyticalMeasurementMethod"]])

slots.compound_analytical_laboratory_name = Slot(uri=MIFC.compound_analytical_laboratory_name, name="compound_analytical_laboratory_name", curie=MIFC.curie('compound_analytical_laboratory_name'),
                   model_uri=MIFC.compound_analytical_laboratory_name, domain=None, range=Optional[str])

slots.component_quality_control_remeasurement = Slot(uri=MIFC.component_quality_control_remeasurement, name="component_quality_control_remeasurement", curie=MIFC.curie('component_quality_control_remeasurement'),
                   model_uri=MIFC.component_quality_control_remeasurement, domain=None, range=Optional[Union[bool, Bool]])

slots.compound_individual_sample_id_list = Slot(uri=MIFC.compound_individual_sample_id_list, name="compound_individual_sample_id_list", curie=MIFC.curie('compound_individual_sample_id_list'),
                   model_uri=MIFC.compound_individual_sample_id_list, domain=None, range=Optional[Union[str, list[str]]])

slots.component_atwater_protein_conversion_factor = Slot(uri=MIFC.component_atwater_protein_conversion_factor, name="component_atwater_protein_conversion_factor", curie=MIFC.curie('component_atwater_protein_conversion_factor'),
                   model_uri=MIFC.component_atwater_protein_conversion_factor, domain=None, range=Optional[float])

slots.component_atwater_fat_conversion_factor = Slot(uri=MIFC.component_atwater_fat_conversion_factor, name="component_atwater_fat_conversion_factor", curie=MIFC.curie('component_atwater_fat_conversion_factor'),
                   model_uri=MIFC.component_atwater_fat_conversion_factor, domain=None, range=Optional[float])

slots.component_atwater_carbohydrate_conversion_factor = Slot(uri=MIFC.component_atwater_carbohydrate_conversion_factor, name="component_atwater_carbohydrate_conversion_factor", curie=MIFC.curie('component_atwater_carbohydrate_conversion_factor'),
                   model_uri=MIFC.component_atwater_carbohydrate_conversion_factor, domain=None, range=Optional[float])

slots.component_protein_from_nitrogen_conversion_factor = Slot(uri=MIFC.component_protein_from_nitrogen_conversion_factor, name="component_protein_from_nitrogen_conversion_factor", curie=MIFC.curie('component_protein_from_nitrogen_conversion_factor'),
                   model_uri=MIFC.component_protein_from_nitrogen_conversion_factor, domain=None, range=Optional[float])

slots.resource_dataset_label = Slot(uri=MIFC.resource_dataset_label, name="resource_dataset_label", curie=MIFC.curie('resource_dataset_label'),
                   model_uri=MIFC.resource_dataset_label, domain=None, range=str)

slots.resource_dataset_version_number = Slot(uri=MIFC.resource_dataset_version_number, name="resource_dataset_version_number", curie=MIFC.curie('resource_dataset_version_number'),
                   model_uri=MIFC.resource_dataset_version_number, domain=None, range=int)

slots.resource_mifc_version_tag = Slot(uri=MIFC.resource_mifc_version_tag, name="resource_mifc_version_tag", curie=MIFC.curie('resource_mifc_version_tag'),
                   model_uri=MIFC.resource_mifc_version_tag, domain=None, range=Union[str, "ResourceMIFCVersionTag"])

slots.resource_contributor_orcid = Slot(uri=MIFC.resource_contributor_orcid, name="resource_contributor_orcid", curie=MIFC.curie('resource_contributor_orcid'),
                   model_uri=MIFC.resource_contributor_orcid, domain=None, range=Optional[Union[str, list[str]]])

slots.resource_organization_name = Slot(uri=MIFC.resource_organization_name, name="resource_organization_name", curie=MIFC.curie('resource_organization_name'),
                   model_uri=MIFC.resource_organization_name, domain=None, range=Optional[Union[str, list[str]]])

slots.container__foods = Slot(uri=MIFC.foods, name="container__foods", curie=MIFC.curie('foods'),
                   model_uri=MIFC.container__foods, domain=None, range=Optional[Union[Union[dict, Food], list[Union[dict, Food]]]])

slots.container__components = Slot(uri=MIFC.components, name="container__components", curie=MIFC.curie('components'),
                   model_uri=MIFC.container__components, domain=None, range=Optional[Union[Union[dict, Component], list[Union[dict, Component]]]])

slots.container__resources = Slot(uri=MIFC.resources, name="container__resources", curie=MIFC.curie('resources'),
                   model_uri=MIFC.container__resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])
