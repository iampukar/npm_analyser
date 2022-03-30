# Overview
-----------------------------------------------------------------------------

npm_analyser is a Python library to monitor an npm package! 

## Package Installer 

    pip install npm-analyser==1.0.0

## Usage

    from npm_analyser import npm_analyser
    '''
      package_name -> string npm package name.
    '''
    package_details = npm_analyser(package_name)
    
    print(package_details.package_name)
    print(package_details.version)
    print(package_details.weekly_downloads)
    print(package_details.license)
    print(package_details.last_published)
    print(package_details.get_dev_dependencies)
    
**Utilities**

| Name           | Description  |
| ------------- | -----|
| package_name | Returns the npm package name! |
| version | Returns the npm package version! |
| last_published | Returns the npm package last published date! |
| total_versions | Returns the total versions of npm package! |
| number_of_dependents | Returns the total number of dependents of the npm package! |
| get_dev_dependencies | Returns the dev-dependencies of the npm package! |
| weekly_downloads | Returns the weekly downloads of the npm package! |
| license | Returns the license of the npm package! |
| unpacked_size | Returns the unpacked size of the npm package! |
| total_files | Returns the total files of the npm package! |

## Requirements

The `requirements.txt` file has details of all Python libraries for this package, and can be installed using 
```
pip install -r requirements.txt
```

## Organization

    ├── src
    │   ├── npm_analyser
              ├── init             <- init
              ├── npm_analyser     <- package source code for npm analyser
    ├── setup.py             <- setup file 
    ├── LICENSE              <- LICENSE
    ├── README.md            <- README
    ├── CONTRIBUTING.md      <- contribution
    ├── test.py              <- test cases for unit testing
    ├── requirements.txt     <- requirements file for reproducing the code package

## License

MIT

## Contributions

For steps on code contribution, please see [CONTRIBUTING](./CONTRIBUTING.md).
