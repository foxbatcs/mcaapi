from .input import *
from .library import *

def api_response(url, headers = HEAD, data = PAYLOAD):
  response = requests.request("GET", url, headers=headers, data=data)
  apiResponse = json.loads(response.text)
  #apiResponseDictKeys = list(apiResponse.keys())
  #print(apiResponseDictKeys)
  return apiResponse#, apiResponseDictKeys

class Search():
    '''
    Parameters: query
    URL encoded query to search for
    '''
    def all(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        Description: Searches all data points available. Returns a structured JSON result set with Real Property, BPP, MH, Rentals, Subdivisions, and Content along with totals found
        Path: /search/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/Phoenix
        '''
        url = url + '/search/{}?limit={}&offset={}'.format(urllib.parse.quote(query), limit, offset)
        return api_response(url, head)

    def subdivisions(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        Description: Searches only subdivision names. Returns a structured JSON result set with a list of subdivision names and parcel counts.
        Path: /search/subdivisions/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/subdivisions/phoenix
        '''
        url = url + '/search/subdivisions/{}?limit={}&offset={}'.format(urllib.parse.quote(query), limit, offset)
        return api_response(url, head)

    def realProperty(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Searches only real property parcels. Returns a structured JSON result set with only real property parcels.
        Path: /search/property/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/property/phoenix'''
        url = url + '/search/property/{}?limit={}&offset={}'.format(query, limit, offset)
        pass #return api_response(url, head)

    def bpp(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Searches only business personal property accounts. Returns a structured JSON result set with only business personal property accounts.
        Path: /search/bpp/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/bpp/phoenix'''
        url = url + '/search/bpp/{}?limit={}&offset={}'.format(query, limit, offset)
        pass #return api_response(url, head)

    def mh(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Searches only mobile home accounts. Returns a structured JSON result set with only mobile home accounts.
        Path: /search/mh/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/mh/phoenix
        '''
        url = url + '/search/mh/{}?limit={}&offset={}'.format(query, limit, offset)
        pass #return api_response(url, head)

    def rentals(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        Description: Searches only rental registrations. Returns a structured JSON result set with only rental registrations.
        Path: /search/rentals/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/rentals/phoenix
        '''
        url = url + '/search/rentals/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)

    def propertyType(type, limit = 1000, offset = 0, ):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Potential Values:
        RD = Residential
        LD = Undeveloped Land
        AG = Agriculture
        Description: Searches only on property types. Property type must be AG, CM, LD, MH, or RD.
        Path: /search/prop-type/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/prop-type/RD
        '''
        url = url + '/search/prop-type/{}?limit={}&offset={}'.format(query, limit, offset)
        pass #return api_response(url, head)

class Parcel():
    '''
    Parameters: apn
    APN (Assessor Parcel Number or APN for short) must formatted with (or without) spaces, dashes, or dots.
    '''
    def details(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object with all available parcel data. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A
        '''
        url = url + '/parcel/{}'.format(apn)
        return api_response(url, head)

    def information(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object with information specific to the property. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}/propertyinfo
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/propertyinfo
        '''
        url = url + '/parcel/{}/propertyinfo'.format(apn)
        return api_response(url, head)

    def address(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object with address of the property. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}/address
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/address
        '''
        url = url + '/parcel/{}/address'.format(apn)
        return api_response(url, head)

    def latlon(apn, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object with latitude, longitude, and address of the property. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}/propertyinfo
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/propertyinfo
        '''
        url = url + '/parcel/{}/geo'.format(apn)
        pass #return api_response(url, head)

    def valuation(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object with the past 5 years of valuation data from a parcel. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}/valuations
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/valuations
        '''
        url = url + '/parcel/{}/valuations'.format(apn)
        return api_response(url, head)

    def residential(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object with all the available residential parcel data. Does not apply to commerical, land or agriculture parcels.
        Works with parcel type(s): Residential, Commercial, Land
        Path: /parcel/{apn}
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/residential-details
        '''
        url = url + '/parcel/{}/residential-details'.format(apn)
        return api_response(url, head)

    def comps(apn, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object with the 5 most likely similar parcels. Works with parcel type(s): Residential
        Path: /parcel/{apn}/similar-parcels
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/similar-parcels
        '''
        url = url + '/parcel/{}/similar-parcels'.format(apn)
        pass #return api_response(url, head)

    def improvement(apn, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object with just the parcel improvements. Works with parcel type(s): Commercial, Land, Agriculture
        Path: /parcel/{apn}/improvements
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/improvements
        '''
        url = url + '/parcel/{}/improvements'.format(apn)
        pass #return api_response(url, head)

    def owner(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object with all available parcel data. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}/owner-details
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/owner-details
        '''
        url = url + '/parcel/{}/owner-details'.format(apn)
        return api_response(url, head)

    def rental(apn, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object with available rental data for the parcel. Works with parcel type(s): Residential, Commercial, Land
        Path: /parcel/{apn}/rental-details
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/rental-details
        '''
        url = url + '/parcel/{}/rental-details'.format(apn)
        pass #return api_response(url, head)

    def zoning(apn, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object with the zoning information for the parcel. Works with parcel type(s): Residential, Commercial, Land, Agriculture
        Path: /parcel/{apn}/zoning
        Example: https://preview.mcassessor.maricopa.gov/parcel/112-19-038A/zoning
        '''
        url = url + '/parcel/{}/zoning'.format(apn)
        pass #return api_response(url, head)

    def mcr(mcr, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/mcr/{})'.format(mcr)
        return api_response(url, head)

    def sec_twn_rng(sectwnrng, url = URL, head = HEAD):
        '''
        Description: Returns a JSON object.
        Parcel Types: Residential, Commercial, Land, Agriculture
        Path: /parcel/mcr/{mcr}
        Example: https://preview.mcassessor.maricopa.gov/parcel/mcr/251
        '''
        url = url + '/parcel/str/{}'.format(sectwnrng)
        return api_response(url, head)

    def subdivision(sub, rental = False, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object.
        Parcel Types: Residential, Commercial, Land, Agriculture
        Path: /parcel/subdivision/{sub}[/{rentals}]
        Example: https://preview.mcassessor.maricopa.gov/parcel/subdivision/24596
        Example (only rentals): https://preview.mcassessor.maricopa.gov/parcel/subdivision/24596/rentals
        '''
        if rental == False:
            url = url + '/parcel/subdivision/{}'.format(sub)
        else:
            url = url + '/parcel/subdivision/{}/rentals'.format(sub)
        pass #return api_response(url, head)

class MapID():
    '''
    Parameters:
    - apn
    APN (Assessor Parcel Number or APN for short) must formatted with (or without) spaces, dashes, or dots.
    - mcr
    MCR Number.
    - sub
    Subdivision name. Must be URL encoded.
    - str
    Section/Township/Range. Can be formatted with (or without) spaces, dashes, or dots. '11E01', '011E01', or '01-1E-01'
    - book
    Three digit book portion of an APN.
    - map
    Two digit map portion of an APN.
    '''
    def parcel(apn, url = URL, head = HEAD):
        '''
        Description: Returns a JSON array of map file names.
        Path: /mapid/parcel/{apn}
        Example: https://preview.mcassessor.maricopa.gov/mapid/parcel/112-19-038A
        '''
        url = url + '/mapid/parcel/{}'.format(apn)
        return api_response(url, head)

    def subdivisions(sub, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON array of map file names.
        Path: /mapid/sub/{sub}
        Example: https://preview.mcassessor.maricopa.gov/mapid/sub/CASA%20REAL%20PHOENIX%201A%20LOT%201-29
        '''
        url = url + '/mapid/sub/{}'.format(sub)
        pass #return api_response(url, head)

    def bookmap(book, map, url = URL, head = HEAD):
        '''
        Description: Returns a JSON array of map file names.
        Path: /mapid/bookmap/{book}/{map}
        Example: https://preview.mcassessor.maricopa.gov/mapid/bookmap/112/19
        '''
        url = url + '/mapid/bookmap/{}/{}'.format(book, map)
        return api_response(url, head)

    def secTwnRng(sec_twn_rng, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON array of map file names.
        Path: /mapid/str/{str}
        Example: https://preview.mcassessor.maricopa.gov/mapid/str/8%201N%203E
        '''
        url = url + '/mapid/str/{}'.format(sec_twn_rng)
        pass #return api_response(url, head)

    def mcr(mcr, url = URL, head = HEAD):
        '''
        Description: Returns a JSON array of map file names.
        Path: /mapid/mcr/{mcr}
        Example: https://preview.mcassessor.maricopa.gov/mapid/mcr/251
        '''
        url = url + '/mapid/mcr/{})'.format(mcr)
        return api_response(url, head)

class BPPMH():
    '''
    Parameters:
    - an
    Business personal property account number.
    - at
    Business personal property account type character. Must be lower case and must be a single letter of either 'c' for Commercial, 'm' for Multiple or 'l' for Lessor
    - ty
    Four digit tax year. Defaults to current tax year if omitted.
    '''
    def details(account_number, account_type = 'c', url = URL, head = HEAD):
        '''
        Description: Returns either account details for a single, commercial account or account details to a multiple or lessor account. Optionally supply a tax year to get a list of accounts for that tax year. Tax year does not apply to commercial accounts.
        Path: /bpp/{at}/{an}[/{ty}]
        Example: https://preview.mcassessor.maricopa.gov/bpp/c/1003384
        Example: https://preview.mcassessor.maricopa.gov/bpp/m/1056
        Example: https://preview.mcassessor.maricopa.gov/bpp/m/1056/2020
        Example: https://preview.mcassessor.maricopa.gov/bpp/l/1145
        Example: https://preview.mcassessor.maricopa.gov/bpp/l/1145/2020
        '''
        url = url + '/bpp/{}/{}'.format(account_type, account_number)
        return api_response(url, head)

    def account(account_number, account_type = 'c', url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns the account name for an individual account.
        Path: /bpp/{at}/{an}/name
        Example: https://preview.mcassessor.maricopa.gov/bpp/c/101068/name
        Example: https://preview.mcassessor.maricopa.gov/bpp/m/1056/name
        Example: https://preview.mcassessor.maricopa.gov/bpp/l/1145/name
        '''
        url = url + '/bpp/{}/{}/name'.format(account_type, account_number)
        pass #return api_response(url, head)

    def mhAccount(account_number, url = URL, head = HEAD):
        '''
        Description: Returns account details for an unsecured mobile home.
        Path: /mh/{an}
        Example: https://preview.mcassessor.maricopa.gov/mh/6214407
        '''
        url = url + '/mh/{}'.format(account_number)
        return api_response(url, head)

    def mhVIN(vin_number, url = URL, head = HEAD):
        '''
        Description: Returns account number on a mobile home VIN.
        Path: /mh/vin/{vin}
        Example: https://preview.mcassessor.maricopa.gov/mh/vin/4C027073US3617
        '''
        url = url + '/mh/vin/{}'.format(vin_number)
        return api_response(url, head)

class Export():
    '''
    CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
    Parameters: query
    URL encoded query to search for
    '''
    def RealPropertySearch(query, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a CSV (comma separated values) file with the results of a real property search.
        Path: /search/export/property/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/export/property/phoenix
        Example (with limit): https://preview.mcassessor.maricopa.gov/search/export/property/phoenix?limit=5
        Example (with limit and offset): https://preview.mcassessor.maricopa.gov/search/export/property/phoenix?limit=5&offset=5
        '''
        url = url + '/search/export/property/{}'.format(query)
        pass #return api_response(url, head)

    def BusinessPropertySearch(query, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a CSV (comma separated values) file with the results of a business personal property search.
        Path: /search/export/bpp/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/export/bpp/phoenix
        Example (with limit): https://preview.mcassessor.maricopa.gov/search/export/bpp/phoenix?limit=5
        Example (with limit and offset): https://preview.mcassessor.maricopa.gov/search/export/bpp/phoenix?limit=5&offset=5
        '''
        url = url + '/search/export/bpp/{}'.format(query)
        pass #return api_response(url, head)

    def MobileHomeSearch(query, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a CSV (comma separated values) file with the results of a mobile home search.
        Path: /search/export/mh/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/export/mh/phoenix
        Example (with limit): https://preview.mcassessor.maricopa.gov/search/export/mh/phoenix?limit=5
        Example (with limit and offset): https://preview.mcassessor.maricopa.gov/search/export/mh/phoenix?limit=5&offset=5
        '''
        url = url + '/search/export/mh/{}'.format(query)
        pass #return api_response(url, head)

    def RentalPropertySearch(query, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a CSV (comma separated values) file with the results of a real property search.
        Path: /search/export/rentals/{query}
        Example: https://preview.mcassessor.maricopa.gov/search/export/rentals/phoenix
        Example (with limit): https://preview.mcassessor.maricopa.gov/search/export/rentals/phoenix?limit=5
        Example (with limit and offset): https://preview.mcassessor.maricopa.gov/search/export/rentals/phoenix?limit=5&offset=5
        '''
        url = url + '/search/export/rentals/{}'.format(query)
        pass #return api_response(url, head)

class Property():
    '''
    CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
    Path: /search/property/
    Definitions
    BETWEEN
    Creates a between clause Example: saleyear=2000-2018
    IN
    Creates an IN clause Example: saleyear=2000,2002,2004,2006,2008
    MATCH
    Creates an exact match clause Example: saleyear=2000
    Parameters
    limit
    Sets the limit for the number of results to return (maximum of 10000 results now, but still defaults to
    1000 for performance reasons)
    offset
    Sets the offset for search
    Sorting
    ASC
    Sorts the results in ascending order
    DESC
    Sorts the results in descending
    Sortable Fields
    apn, rental, mcr, ownername, sectiontownshiprange, situsaddress, situscity, situszip,
    subdivisionname, weight, propertydescription, ownermailingaddress, propertytype, puccode, imprfcv,
    landfcv, neighborhood, marketarea, stories, landsize, saleprice, saledate, fullcashvalue,
    livablesqfootage, constructionyear, weightedage, poolarea, foreclosed, floor1sqft, floor2sqft,
    floor3sqft, basementsqft, pool, garage
    Operators
    >
    Displays results that are greater than the value to the right of the operator
    <
    Displays results that are less than the value to the right of the operator
    >=
    Displays results that are greater than or equal to the value to the right of the operator
    <=
    Displays results that are less than or equal to the value to the right of the operator
    Search Facets
    imprfcv
    Improvement full cash value - BETWEEN, IN, and MATCH
    landfcv
    Land full cash value - BETWEEN, IN, and MATCH
    stories
    Stories of a building - BETWEEN, IN, and MATCH
    landsize
    Land size - BETWEEN, IN, and MATCH
    saleprice
    Sale price - BETWEEN, IN, and MATCH
    salemonth
    Sale month - BETWEEN, IN, and MATCH
    saleyear
    Sale year - BETWEEN, IN, and MATCH
    fullcashvalue
    Full cash value (for the current valuation year) - BETWEEN, IN, and MATCH
    livablesqfootage
    Livable square footage - BETWEEN, IN, and MATCH
    constructionyear
    Construction year - BETWEEN, IN, and MATCH
    weightedage
    Weighted age - BETWEEN, IN, and MATCH
    poolarea
    Square footage of a pool - BETWEEN, IN, and MATCH
    floor1sqft
    First floor square footage- BETWEEN, IN, and MATCH
    floor2sqft
    Second floor square footage - BETWEEN, IN, and MATCH
    floor3sqft
    Third floor square footage - BETWEEN, IN, and MATCH
    basementsqft
    Basement floor square footage - BETWEEN, IN, and MATCH
    pool
    Does property have a pool - MATCH (Boolean)
    garage
    Does property have a garage - MATCH (Boolean)
    rental
    Property registered as a rental - MATCH (Boolean)
    city
    City is the property located in - IN, and MATCH
    zip
    Zip code is the property located in - IN, and MATCH
    puccode
    Property use code - IN, and MATCH
    neighborhood
    Neighborhood code - IN, and MATCH
    marketarea
    Market area code - IN, and MATCH
    '''
    pass #return api_response(url, head)

class Deed():
    '''
    Parameters: apn
    APN (Assessor Parcel Number or APN for short) must formatted with (or without) spaces, dashes, or dots.
    '''
    def deed(apn, url = URL, head = HEAD):
        '''
        CURRENTLY UNSUPPORTED: https://preview.mcassessor.maricopa.gov/file/home/MC-Assessor-2021-API-Documentation.pdf
        Description: Returns a JSON object with deed number, date, type, stat, and owner's name data.
        Path: /deeds/chain/{apn}
        Example: https://preview.mcassessor.maricopa.gov/deeds/chain/50705902
        '''
        url = url + '/deeds/chain/{}'.format(apn)
        pass #return api_response(url, head)
