<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://raw.githubusercontent.com/CamiloCortesM/addressValidator/main/images/logo.png" alt="Logo" width="300">
  <h3 align="center">addressValidator</h3>
<p align="center">
    <a href="https://github.com/CamiloCortesM/addressValidator/graphs/contributors"><img src="https://img.shields.io/github/contributors/CamiloCortesM/addressValidator.svg?style=flat-square" alt="Contributors"></a>
    <a href="https://github.com/CamiloCortesM/addressValidator/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/CamiloCortesM/addressValidator.svg?style=flat-square"></a>
    <a href="https://github.com/CamiloCortesM/addressValidator/stargazers"><img src="https://img.shields.io/github/stars/CamiloCortesM/addressValidator.svg?style=flat-square" alt="starts"></a>
    <a href="https://github.com/CamiloCortesM/addressValidator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CamiloCortesM/addressValidator.svg?style=flat-square" alt="Awesome"></a>
    <a href="https://pypi.org/project/addressValidator/"><img src="https://img.shields.io/badge/pypi-addressValidator-blue.svg?style=flat-square&maxAge=3600" alt="Slack"></a>
</p>
    <p align="center">
    Validate urban and rural addresses in Colombia
    <br />
    <a href="#documentation"><strong>Explore the docs»</strong></a>
    <br />
    <br />
    <a href="https://github.com/CamiloCortesM/addressValidator/issues">Report Bug</a>
    ·
    <a href="https://github.com/CamiloCortesM/addressValidator/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
    <a href="#documentation">Documentation</a>
    <ul>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <a href="#installation">Installation</a>
      </ul>
    </ul>
      <ul><a href="#usage">Usage</a></ul>
      <ul>
      <a href="#functions">functions</a>
        <ul>
        <a href="#address_validator">address_validator</a>
        </ul>
        <ul>
        <a href="#address_validator_dian">address_validator_dian</a>
        </ul>
        <ul>
        <a href="#address_validator_file">address_validator_file</a>
        </ul>
         <ul>
        <a href="#address_validator_file_dian">address_validator_file_dian</a>
        </ul>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- ROADMAP -->
## Documentation

<!-- GETTING STARTED -->
### Getting Started

#### Installation

```bash
pip install addressValidator

or

py -m pip install addressValidator
```
latest stable version `addressValidator==1.2.1`
<!-- USAGE EXAMPLES -->
### Usage

* Example 
    ```python
    from addressValidator import address_validator
    
    address = "Calle 3BC #10-2 Barrio San Juan Apartamento 201"
    if address_validator(address):
       print(address+" direccion valida")
    else:
       print(address+" direccion invalida")
    ```

_For more examples, please refer to the [Examples packages](https://github.com/CamiloCortesM/addressValidator/tree/main/examples)_

<!-- FUNCTIONS -->
### Functions
we can use 4 functions to validate both urban and rural addresses

#### address_validator

address_validator function receives as a parameter a mandatory string which will be evaluated and will return a boolean if valid or not.

```python
from addressValidator import address_validator

# address_validator(str) -> bool
address = address_validator("Calle 13B #10-3")
print(address)// #True
```
if the address is not valid it will return False

```python
from addressValidator import address_validator

# address_validator(str) -> bool
address = address_validator("Calle 13sur 13-121B")
print(address)// #False
```
#### address_validator_dian
fucntion address_validator_dian returns the address validation according to [dian nomenclature](https://www.mineducacion.gov.co/1621/articles-193290_estandar_direcciones_urbanas.pdf)

```python
from addressValidator import address_validator_dian

# address_validator_dian(str) -> bool
address = address_validator_dian("Cl 13 B 10 3")
print(address)// #True
```
if the address is not valid it will return False

```python
from addressValidator import address_validator_dian

# address_validator_dian(str) -> bool
address = address_validator_dian("Cl 13 sur 13 121 B")
print(address)// #False
```

#### address_validator_file
address_validator_file function receives a text file, does not return any value, this function creates a text file with the respective validations.
```python
from addressValidator import address_validator_file

# address_validator_file(file) -> None
with open("address.txt") as file_object:
     address_validator_file(file_object) # create output.txt

```
here we can see that we read a file called [address.txt](https://github.com/CamiloCortesM/addressValidator/blob/main/examples/address.txt) that we find in the examples folder this function will return the validations of all the strings as we can see in the [output.txt](https://github.com/CamiloCortesM/addressValidator/blob/main/examples/output.txt) file.All this for urban and rural addresses 

#### address_validator_file_dian

The function address_validator_file_dian receives a text file, creates a text file with the validations of the addresses with dian nomenclature 
```python
from addressValidator import address_validator_file_dian

# address_validator_file_dian(file) -> None
with open("addressDian.txt") as file_object:
    address_validator_file_dian(file_object) # create output.txt

```
We read the [addressDian](https://github.com/CamiloCortesM/addressValidator/blob/main/examples/addressDian.txt) file from the root path and send the document to the function and it returns the validations in an `output.txt` file. Validations with file for dian nomenclature is in the [output_dian.txt](https://github.com/CamiloCortesM/addressValidator/blob/main/examples/output_dian.txt) file

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/CamiloCortesM/addressValidator/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
