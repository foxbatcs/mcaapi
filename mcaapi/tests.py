# Search
isinstance(mcaapi.Search.all('301 W Jefferson')['rp'], dict)
isinstance(mcaapi.Search.subdivisions('Phoenix')['rp'], dict)
isinstance(mcaapi.Search.realProperty('Phoenix'), dict)
isinstance(mcaapi.Search.bpp('Phoenix'), dict)
isinstance(mcaapi.Search.mh('Phoenix'), dict)
isinstance(mcaapi.Search.rentals('Phoenix'), dict)
isinstance(mcaapi.Search.propertyType('RD'), dict)

# Parcel
isinstance(mcaapi.Parcel.details('11219038A'), dict)
isinstance(mcaapi.Parcel.information('11219038A'), dict)
isinstance(mcaapi.Parcel.address('11219038A'), dict)
isinstance(mcaapi.Parcel.valuation('11219038A'), list)
isinstance(mcaapi.Parcel.residential('11219038A'), dict)
isinstance(mcaapi.Parcel.owner('11219038A'), dict)
isinstance(mcaapi.Parcel.mcr(251), list)
isinstance(mcaapi.Parcel.secTwnRng('8 1N 3E'), list)

# MapID
isinstance(mcaapi.MapID.parcel('11219038A'), list)
isinstance(mcaapi.MapID.bookmap('112', '19'), list)
isinstance(mcaapi.MapID.mcr(251), list)

# BPPMH
isinstance(mcaapi.BPPMH.details('')[''], dict)
isinstance(mcaapi.BPPMH.mhAccount('')[''], dict)
isinstance(mcaapi.BPPMH.mhVIN('')[''], dict)

#
