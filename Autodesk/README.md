# Autodesk Recipes

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Purpose](#purpose)
- [How to contribute](#how-to-contribute)
- [Support](#support)
- [Credit](#credit)
- [License](#license)
  
## Purpose

These Autodesk recipes serve the purpose of automating the creation of packages that can easily be deployed using an MDM of choice. They currently work with (and have been tested with) the following:

* AutoCAD 2021
* Maya 2020
* Mudbox 2020
* SketchBook Pro 2021

# Usage

1. Create an override of the required *.pkg recipe
2. Add in the required product and licensing information to the override:
    1. `VERSION` should match the major version year of the app (i.e 2020 for Maya 2020).
    2. `PRODUCT_KEY` should match the product key for the app (i.e. 657L1 for Maya 2020; these can be obtained from [here](https://knowledge.autodesk.com/customer-service/download-install/activate/find-serial-number-product-key/product-key-look)</string>.
    3. `EULA_LOCALE` should match the country code of the location the app will be deployed in (i.e `GB` for Great Britain).
    4. `SERIAL_NUMBER` should match the serial number of the product, in the format `XXX-XXXXXXXX`.
    5. `LIC_SERVER` The IP address/hostname/FQDN and port of the licensing server. If left blank, the override assumes the product will be licensed as standalone.
    6. `PATH_TO_DMG` Path to the folder containing the DMG file, _not_ the DMG file itself.
3. Run the override 

## How to contribute

1. Fork this project, if required
2. Create a new branch (`git checkout -b myNewBranch`)
3. Make changes, and commit (`git commit -am "myChanges"`)
4. Push to the new branch (`git push origin myNewBranch`)
5. Create new pull request

## Support

Use at your own risk. Moof IT will accept no responsibility for loss or damage caused by these scripts. Contact Moof IT if you need a custom script tailored to your environment.

## Credit

Lorem Ipsum

## License

This work is licensed under http://creativecommons.org/licenses/by/4.0/.

These scripts may be freely modified for personal or commercial purposes but may not be republished for profit without prior consent.
