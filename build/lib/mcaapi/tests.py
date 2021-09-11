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
isinstance(mcaapi.MapID.subdivisions('Phoenix'), list)
isinstance(mcaapi.MapID.bookmap('112', '19'), list)
isinstance(mcaapi.MapID.secTwnRng('8 1N 3E'), )
isinstance(mcaapi.MapID.mcr(251), list)


# BPPMH
isinstance(mcaapi.BPPMH.details('1003384'), list)
isinstance(mcaapi.BPPMH.account('101068'), set)
isinstance(mcaapi.BPPMH.mhAccount('6214407'), dict)
isinstance(mcaapi.BPPMH.mhVIN('4C027073US3617'), dict)

# Export
isinstance(mcaapi.Export.realPropertySearch('Phoenix'), list)
isinstance(mcaapi.Export.businessPropertySearch('Phoenix'), list)
isinstance(mcaapi.Export.mobileHomeSearch('Phoenix'), list)
isinstance(mcaapi.Export.rentalPropertySearch('Phoenix'), list)

# Deed
isinstance(mcaapi.Deed.deed('11219038A'), list)
