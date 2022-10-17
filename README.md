<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://raw.githubusercontent.com/CamiloCortesM/addressValidator/main/images/logo.png" alt="Logo" width="300">
  <h3 align="center">AVMWeather</h3>
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
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project


<!-- GETTING STARTED -->
## Getting Started

### Installation

```python
pip install addressValidator
```

<!-- USAGE EXAMPLES -->
## Usage

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

<!-- ROADMAP -->
## Documentation


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
