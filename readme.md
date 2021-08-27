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

# Classes

The structure of the wrapper follows the same structure as the API documentation
which can be downloaded here: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf

Not all API calls are supported at this time, per the documentation. I have still
written methods for all of these, but they will only be functional after they fix
the API.

Here is the documentation for each Class, which defines the inputs and outputs of each method, as well as examples.

## Search (mcaapi.Search)

### all('string')

Takes an address, parcel number, name, zip code, city, etc, and returns a JSON object for matching results.

        Example: mcaapi.Search.all('301 W Jefferson')

### subdivisions('string')    

### realProperty('string')

### bpp('string')

### mh('string')

### rentals('string')

### propertyType('string')

## Parcel (mcaapi.Parcel)

### propertyType('string')

### details('string')

### information('string')

### address('string')

### latlon('string')

### valuation('string')

### residential('string')

### comps('string')

### improvement('string')

### owner('string')

### rental('string')

### zoning('string')

### mcr('string')

### sec_twn_rng('string')

### subdivision('string')

## MapID (mcaapi.MapID)

### parcel('string')

### subdivisions('string')

### bookmap('string')

### secTwnRng('string')

### mcr('string')

## Business Personal Property/Mobile Homes (mcaapi.BPPMH)

### details('string')

### account('string')

### mhAccount('string')

### mhVIN('string')

## Exports (mcaapi.Export)

### realPropertySearch('string')

### businessPropertySearch('string')

### mobileHomeSearch('string')

### rentalPropertySearch('string')

## Property (mcaapi.Property)

## Deeds (mcaapi.Deed)

### deed('string')
