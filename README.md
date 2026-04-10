<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# MIFC

## Introduction

Welcome to the USDA [Food DataCentral (FDC)](https://fdc.nal.usda.gov/) **M**inimum **I**nformation (about any) **F**ood **C**omposition (**MIFC**) GitHub repository. The USDA FDC MIFC is a Minimum Information Standard (MIS), serving as a standardized reporting framework to structure food composition data. MIFC defines a set of reporting requirements, a "checklist" of required, recommended, and optional data attributes in a precisely specified reporting format. The MIFC data model is implemented in the [Linked Modeling Language (LinkML)](https://linkml.io/).

## Accessing and using MIFC

The excel versions of the **MIFC** schema, example data and template are available as follows:

* [MIFC_excel_schema](release/MIFC_excel_schema_v1.0.0.xlsx)
* [MIFC_example_data](release/MIFC_example_data_v1.0.0.xlsx)
* [MIFC_template](release/MIFC_template_v1.0.0.xlsx)

## Documentation Website

[https://FoodDataCentral.github.io/mifc](https://FoodDataCentral.github.io/mifc/elements)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [mifc](src/mifc)
    * [schema/](src/mifc/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/mifc/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).


## Scholarly Publication

* [Call to Action: A Need for Community-Driven Minimum Information Standards for Food Composition Data](https://doi.org/10.1016/j.ajcnut.2025.06.027), The American Journal of Clinical Nutrition, 2025-07, DOI: 10.1016/j.ajcnut.2025.06.027.

## Contact

For inquiries about this website any of it's content see https://fdc.nal.usda.gov/contact.