# Search
isinstance(mcaapi.Search.all('301 W Jefferson')['rp'], dict)
isinstance(mcaapi.Search.subdivisions('Phoenix')['rp'], dict)
isinstance(mcaapi.Search.rentals('Phoenix')['rp'], dict)

# Parcel
isinstance(mcaapi.Parcel.details('11219038A'), dict)
isinstance(mcaapi.Parcel.information('11219038A'), dict)
isinstance(mcaapi.Parcel.address('11219038A'), dict)
isinstance(mcaapi.Parcel.valuation('11219038A'), list)
isinstance(mcaapi.Parcel.residential('11219038A'), dict)
isinstance(mcaapi.Parcel.owner('11219038A'), dict)
isinstance(mcaapi.Parcel.mcr(251), list)
isinstance(mcaapi.Parcel.sec_twn_rng('11219038A'), dict)

# MapID
isinstance(mcaapi.MapID.parcel('')[''], dict)
isinstance(mcaapi.MapID.bookmap('')[''], dict)
isinstance(mcaapi.MapID.mcr('')[''], dict)

# BPPMH
isinstance(mcaapi.BPPMH.details('')[''], dict)
isinstance(mcaapi.BPPMH.mhAccount('')[''], dict)
isinstance(mcaapi.BPPMH.mhVIN('')[''], dict)

#
