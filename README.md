# API Token

Use of this library requires obtaining an API Key from
The Maricopa County Assessor's Office. This can be done by
visiting https://preview.mcassessor.maricopa.gov/contact/
and filling out the form.

Change the "Subject" Field to "API Token/Question",
provide your name, number, and a brief note. Then click
"Send Message". MCA's web developer will send you an email
shortly after with the API Key.

Once you have the token, all you need to do is `import mcaapi`. The first time
this is run, it will prompt you for the API token. Simply paste the token into
the prompt, and it will store it in a file located in the source directory of
the library.

# Quick Examples
To query an address, name, parcel number (apn), city, street, subdivision, etc, use the `Search.all()` method as follows:

```
import mcaapi
resp0 = mcaapi.Search.all('301 W Jefferson, Phoenix') #The Assessor Office's Address
resp1 = mcaapi.Search.all('Phoenix')
resp2 = mcaapi.Search.all('11219038A') #The Assessor Office's own APN
```
This will return a JSON object with limited information to your variable containing a  maximum number of items (I believe up to 100). Unfortunately, the `limit` and `offset` parameters are currently not working as per the Maricopa County Assessor API docs, which can be found [here [PDF]](https://www.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf). I have coded in the logic to support this when it is working, and will do my best to keep it updated as things change.

You can get more details for each APN, by using the `Parcel.details()` method as follows:

```
import mcaapi
resp3 = mcaapi.Parcel.details('11219038A')
```

This will provide a substantial number of details about the parcel, its location, ownership, zoning, physical features, and more.

For educational purposes, I have engineered a toy dataset of approximately ten-thousand unique parcels which can be found in the mcaapi/datasets directory.

# Classes

The structure of the wrapper follows the same structure as the API documentation
which can be downloaded here: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

Not all API calls are supported at this time, per the documentation. I have still
written methods for all of these, but they will only be functional after they fix
the API.

Here is the documentation for each Class, which defines the inputs and outputs of each method, as well as examples.

## Search (mcaapi.Search)
**Parameters**
 * `{query}` URL encoded query to search. Encoding is handled by the `urllib.parse.quote` method.

### all('query')
Takes an address, parcel number, name, zip code, city, etc, and returns a JSON object for matching results.

        Example: mcaapi.Search.all('301 W Jefferson')

### subdivisions('subdivision_name')    
Searches only subdivision names and returns a JSON object with subdivision names and parcel counts.

        Example: mcaapi.Search.subdivisions('phoenix')

### realProperty('query')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### bpp('query')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### mh('query')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### rentals('query')
Searches only rental registrations. Returns a structured JSON result set with only rental
registrations.

        Example: mcaapi.Search.rentals('phoenix')

### propertyType('query')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

## Parcel (mcaapi.Parcel)
**Parameters**
 * `{apn}` APN (Assessor Parcel Number or APN for short) must formatted with (or without) spaces, dashes, or dots.

### details('parcel_number')
Returns a JSON object with all available parcel data.

        Example: mcaapi.Parcel.details('11219038A')

### information('parcel_number')
Returns a JSON object with information specific to the property.

        Example: mcaapi.Parcel.information('11219038A')

### address('parcel_number')
Returns a JSON object with address of the property.
        Example: mcaapi.Parcel.address('11219038A')

### latlon('parcel_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### valuation('parcel_number')
Returns a JSON object with the past 5 years of valuation data from a parcel.

        Example: mcaapi.Parcel.valuation('11219038A')

### residential('parcel_number')
Returns a JSON object with all the available residential parcel data. Does not apply to
commerical, land or agriculture parcels.

        Example: mcaapi.Parcel.residential('11219038A')

### comps('parcel_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### improvement('parcel_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### owner('parcel_number')
Returns a JSON object with all available parcel data

        Example: mcaapi.Parcel.owner('11219038A')

### rental('parcel_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### zoning('parcel_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### mcr(int)
DOES NOT PROVIDE A RESPONSE WITH THE TEST MCR# (251)
Returns a JSON object ...

        Example: mcaapi.Parcel.mcr('11219038A')

### sec_twn_rng('parcel_number')
Returns a JSON object ...

        Example: mcaapi.Parcel.sec_twn_rng('11219038A')

### subdivision('parcel_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

## MapID (mcaapi.MapID)
**Parameters**
 * `{apn}` APN (Assessor Parcel Number or APN for short) must formatted with (or without) spaces, dashes, or dots.
 * `{mcr}` Maricopa County Recorder Number.
 * `{sub}` Subdivision name. Must be URL encoded.
 * `{str}` Section/Township/Range. Can be formatted with (or without) spaces, dashes, or dots. '11E01', '011E01', or '01-1E-01'
 * `{book}` Three digit book portion of an APN.
 * `{map}` Two digit map portion of an APN.

### parcel('parcel_number')
Returns a JSON array of map file names.

        Example: mcaapi.MapID.parcel('11219038A')

### subdivisions('subdivision_name')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### bookmap('book', 'map')
Returns a JSON array of map file names.

        Example: mcaapi.MapID.bookmap(112, 19)

### secTwnRng('query')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### mcr('recorder_number')
Returns a JSON array of map file names.

        Example: mccapi.MapID.mcr(251)

## Business Personal Property/Mobile Homes (mcaapi.BPPMH)
**Parameters:**
 * `{an}`   Business personal property account number.
 * `{at}`    Business personal property account type character. Must be lower case and must be a single letter of either 'c' for Commercial, 'm' for Multiple or 'l' for Lessor
 * `{ty}`    Four digit tax year. Defaults to current tax year if omitted.

### details('account_number')
Returns either account details for a single, commercial account or account details
belonging to a multiple or lessor account. Optionally supply a tax year to get a list of accounts for that tax year. Tax year does not apply to commercial accounts.

        Example: mcaapi.BPPMH.details('1003384')

### account('account_number')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### mhAccount('account_number')
Returns account details for an unsecured mobile home.

        Example: mcaapi.BPPMH.mcAccount('6214407')

### mhVIN('mh_vin')
Returns account number on a mobile home VIN.

        Example: mccapi.BPPMH.mhVIN('4C027073US3617')

## Exports (mcaapi.Export)
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### realPropertySearch('string')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### businessPropertySearch('string')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### mobileHomeSearch('string')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### rentalPropertySearch('string')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

## Property (mcaapi.Property)
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

## Deeds (mcaapi.Deed)
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

### deed('string')
Not currently supported. Please refer to the documentation: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
