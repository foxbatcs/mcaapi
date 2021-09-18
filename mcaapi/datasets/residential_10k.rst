.. _residential_dataset:

202109 Maricopa County 10k Residential Parcels dataset
--------------------

**Data Set Characteristics:**

    :Number of Instances: 10,390
    :Number of Attributes: 15
    :Attribute Information:
      - lot_size_sf,
      - city,
      - deed_date,
      - price_usd,
      - sale_date,
      - lat,
      - lon,
      - build_yr,
      - build_size_sf,
      - patio_ct,
      - patio_type,
      - wall_type,
      - roof_type,
      - bath_fixtures_ct,
      - parking_type

    :Missing Attribute Values:
      - price_usd           4241
      - sale_date           4235
      - parking_type         632
      - lon                   33
      - lat                   33
      - deed_date              5
      - bath_fixtures_ct       2
      - roof_type              1
      - wall_type              1
      - patio_type             1
      - patio_ct               1
      - build_size_sf          1
      - build_yr               1
      - city                   0
      - lot_size_sf            0

    :Creator: github.com/foxbatcs

    :Date: Sept, 2021

This dataset contains physical features for approximately ten-thousand residential parcels in Maricopa County that were collected via their API during September of 2021. Approximately half of the data contains Sales Prices and Sales Dates. You can find the MCA API Official Documentation here [PDF], and my Python API wrapper here. It can be installed in Python3 with pip3 install mcaapi.

**Disclaimer (In Part) from MCA:** The Assessor does not guarantee that any information provided on this website is accurate, complete, or current. In many instances, the Assessor has gathered information from independent sources and made it available on this site, and the original information may have contained errors and omissions. Errors and omissions may also have occurred in the process of gathering, interpreting, and reporting the information. Information on the website is not updated in "real time". Source

**My Disclaimer:** This data was collected using sources of public record, which may contain some sensitive identity information. Despite any sensitive information being publicly available, I have done my best to scrub those details from the set. If you notice any details that were missed, please email me at help@foxbatcs.com with a subject of "Sensitive Details Notice MCA" with a description of where the sensitive information is at in the set. I will do my best to remove it in a timely manner.

Additionally, I do not recommend using this dataset for any commercial purposes. The data was not randomly sampled, and may produce skewed models/results. This data is intended for educational purposes only, and I cannot guarantee the recency, accuracy, reliability, or liability of this information. If you would like legally certified data, please contact Maricopa County Assessor Data Sales. Thank you.
