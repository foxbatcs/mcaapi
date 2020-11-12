
exec(open('/content/mcaapi/input.py').read())
exec(open('/content/mcaapi/library.py').read())

class Search():
    '''
    '''
    def all(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)
    
    def subdivisions(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/subdivisions/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)
    
    def realProperty(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/property/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)
    
    def bpp(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/bpp/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)
    
    def mh(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/mh/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)
    
    def rentals(query, limit = 1000, offset = 0, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/rentals/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)

    def propertyType(type, limit = 1000, offset = 0, ):
        '''
        Potential Values: 
        RD = Residential 
        LD = Undeveloped Land
        AG = Agriculture
        '''
        url = url + '/search/prop-tpye/{}?limit={}&offset={}'.format(query, limit, offset)
        return api_response(url, head)

class Parcel():
    '''
    '''    
    def details(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}'.format(apn)
        return api_response(url, head)

    def information(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/propertyinfo'.format(apn)
        return api_response(url, head)

    def address(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/address'.format(apn)
        return api_response(url, head)

    def latlon(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/geo'.format(apn)
        return api_response(url, head)

    def valuation(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/valuations'.format(apn)
        return api_response(url, head)

    def residential(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/residential-details'.format(apn)
        return api_response(url, head)

    def comps(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/similar-parcels'.format(apn)
        return api_response(url, head)

    def improvement(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/improvements'.format(apn)
        return api_response(url, head)

    def owner(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/owner-details'.format(apn)
        return api_response(url, head)

    def rental(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/rental-details'.format(apn)
        return api_response(url, head)

    def zoning(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/{}/zoning'.format(apn)
        return api_response(url, head)

    def mcr(mcr, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/mcr/{})'.format(mcr)
        return api_response(url, head)

    def sec_twn_rng(sectwnrng, url = URL, head = HEAD):
        '''
        '''
        url = url + '/parcel/str/{}'.format(sectwnrng)
        return api_response(url, head)
    
    def subdivision(sub, rental = False, url = URL, head = HEAD):
        '''
        '''
        if rental == False:
            url = url + '/parcel/subdivision/{}'.format(sub)
        else: 
            url = url + '/parcel/subdivision/{}/rentals'.format(sub)
        return api_response(url, head)

class MapID():
    '''
    '''    
    def parcel(apn, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mapid/parcel/{}'.format(apn)
        return api_response(url, head)

    def subdivisions(sub, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mapid/sub/{}'.format(sub)
        return api_response(url, head)

    def bookmap(book, map, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mapid/bookmap/{}/{}'.format(book, map)
        return api_response(url, head)

    def secTwnRng(sec_twn_rng, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mapid/str/{}'.format(sec_twn_rng)
        return api_response(url, head)

    def mcr(mcr, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mapid/mcr/{})'.format(mcr)
        return api_response(url, head)
    
class BPPMH():
    '''
    '''
    def details(account_number, account_type = 'c', url = URL, head = HEAD):
        '''
        '''
        url = url + '/bpp/{}/{}'.format(account_type, account_number)
        return api_response(url, head)
    
    def account(account_number, account_type = 'c', url = URL, head = HEAD):
        '''
        '''
        url = url + '/bpp/{}/{}/name'.format(account_type, account_number)
        return api_response(url, head)

    def mhAccount(account_number, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mh/{}'.format(account_number)
        return api_response(url, head)

    def mhVIN(vin_number, url = URL, head = HEAD):
        '''
        '''
        url = url + '/mh/vin/{}'.format(vin_number)
        return api_response(url, head)

class Export():
    '''
    '''
    def RealPropertySearch(query, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/export/property/{}'.format(query)
        return api_response(url, head) 
    
    def BusinessPropertySearch(query, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/export/bpp/{}'.format(query)
        return api_response(url, head)
    
    def MobileHomeSearch(query, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/export/mh/{}'.format(query)
        return api_response(url, head) 
    
    def RentalPropertySearch(query, url = URL, head = HEAD):
        '''
        '''
        url = url + '/search/export/rentals/{}'.format(query)
        return api_response(url, head) 

class Property():
    '''
    '''
#Work in Progress
    pass
        
class Deed():
    def deed(apn, url = URL, head = HEAD):
        '''
        '''
      url = url + '/deeds/chain/{}'.format(apn)
      return api_response(url, head)
