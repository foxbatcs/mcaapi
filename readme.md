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
### All
Takes an address, parcel number, name, zip code, city, etc, and returns a JSON objects for matching results.

        Example: mcaapi.Search.all('301 W Jefferson')
    
## Parcel (mcaapi.Parcel)

## MapID (mcaapi.MapID)

## Business Personal Property/Mobile Homes (mcaapi.BPPMH)

## Property (mcaapi.Property)

## Exports (mcaapi.Export)

## Deeds (mcaapi.Deed)
