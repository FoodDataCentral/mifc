

# Class: PersonCollection 


_A holder for Person objects_





URI: [mifc:PersonCollection](https://w3id.org/FoodDataCentral/mifc/PersonCollection)





```mermaid
 classDiagram
    class PersonCollection
    click PersonCollection href "../PersonCollection/"
      PersonCollection : entries
        
          
    
        
        
        PersonCollection --> "*" Person : entries
        click Person href "../Person/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [entries](entries.md) | * <br/> [Person](Person.md) |  | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/FoodDataCentral/mifc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mifc:PersonCollection |
| native | mifc:PersonCollection |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonCollection
description: A holder for Person objects
from_schema: https://w3id.org/FoodDataCentral/mifc
attributes:
  entries:
    name: entries
    from_schema: https://w3id.org/FoodDataCentral/mifc
    rank: 1000
    domain_of:
    - PersonCollection
    range: Person
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: PersonCollection
description: A holder for Person objects
from_schema: https://w3id.org/FoodDataCentral/mifc
attributes:
  entries:
    name: entries
    from_schema: https://w3id.org/FoodDataCentral/mifc
    rank: 1000
    alias: entries
    owner: PersonCollection
    domain_of:
    - PersonCollection
    range: Person
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>