```mermaid
classDiagram
    class Material {
        +name: String
        +description: String
        +__str__(): String
    }

    class LaserSource {
        +name: String
        +type_of_laser: String
        +wavelength: Integer
        +__str__(): String
    }

    class LaserMarkingParameters {
        +scanning_speed: Integer
        +average_power: Decimal
        +scan_step: Float
        +pulse_duration: Float
        +pulse_repetition_rate: Integer
        +overlap_coefficient: Float
        +volumetric_density_of_energy: Float
        +color_red: Integer
        +color_green: Integer
        +color_blue: Integer
        +author: String
        +date_published: DateTime
        +research_date: DateTime
        +__str__(): String
    }

    Material --> LaserMarkingParameters : has
    LaserSource --> LaserMarkingParameters : has


```
