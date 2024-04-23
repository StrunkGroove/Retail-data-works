TOKEN = '8433574f5c336b3bb1574ddb6b078388'
AUTHORIZATION = 'Basic NGxhcHltb2JpbGU6eEo5dzFRMyhy'

CATEGORY_ID = '409' # Миски, кормушки, поилки для грызунов и хорьков

CITIES = {
    'Moscow': '0000073738',
    'Saint Petersburg': '0000103664'
}

PARSING_ELEMENTS = [
    {
        'page': 1,
        'count': 10,
        'sign': '232bac07aca59688f111d54add5470af',
    },
    {
        'page': 2,
        'count': 10,
        'sign': 'c825d764f3c9bd977f49e710af88065b',
    },
    {
        'page': 3,
        'count': 10,
        'sign': '225087d24ccb6db2c9aadb3a7556e284',
    },
    {
        'page': 4,
        'count': 10,
        'sign': 'ec4d3d000fbb3bfa2d7d59066b221b9d',
    },
    {
        'page': 5,
        'count': 10,
        'sign': 'faa548523221d9d32162261f12a04f6d',
    },
    {
        'page': 6,
        'count': 10,
        'sign': '0769b046d58dd78fbc32fb786afafa15',
    },
    {
        'page': 7,
        'count': 10,
        'sign': '3df2b525e6e49f627cdada209912dcd1',
    },
    {
        'page': 8,
        'count': 10,
        'sign': 'dd224d454109336877893d42d8fbe222',
    },
    {
        'page': 9,
        'count': 10,
        'sign': '9da7ebfb92a674f5f95b5745d6abfc22',
    },
    {
        'page': 10,
        'count': 10,
        'sign': 'd662641e0f60f4139434aab5c873ff86',
    },
]

PRICES_PAYLOAD = [
    f'offers%5B0%5D=96604&offers%5B10%5D=34847&offers%5B11%5D=34847&offers%5B12%5D=55457&offers%5B13%5D=55457&offers%5B14%5D=41165&offers%5B15%5D=41165&offers%5B16%5D=146213&offers%5B17%5D=146213&offers%5B18%5D=34831&offers%5B19%5D=34831&offers%5B1%5D=96604&offers%5B2%5D=34849&offers%5B3%5D=34849&offers%5B4%5D=34827&offers%5B5%5D=34827&offers%5B6%5D=146418&offers%5B7%5D=146418&offers%5B8%5D=34829&offers%5B9%5D=34829&sign=7374f0d5729e05f8bda305413db4006c&token={TOKEN}',
    f'offers%5B0%5D=72339&offers%5B10%5D=105245&offers%5B11%5D=105245&offers%5B12%5D=125678&offers%5B13%5D=125678&offers%5B14%5D=138818&offers%5B15%5D=138818&offers%5B16%5D=149331&offers%5B17%5D=149331&offers%5B18%5D=151745&offers%5B19%5D=151745&offers%5B1%5D=72339&offers%5B2%5D=149329&offers%5B3%5D=149329&offers%5B4%5D=128267&offers%5B5%5D=128267&offers%5B6%5D=169797&offers%5B7%5D=169797&offers%5B8%5D=34857&offers%5B9%5D=34857&sign=255873eaeea70d5e740333d71f704eba&token={TOKEN}',
    f'offers%5B0%5D=146546&offers%5B10%5D=164911&offers%5B11%5D=164911&offers%5B12%5D=146420&offers%5B13%5D=146420&offers%5B14%5D=72343&offers%5B15%5D=72343&offers%5B16%5D=59677&offers%5B17%5D=59677&offers%5B18%5D=169795&offers%5B19%5D=169795&offers%5B1%5D=146546&offers%5B2%5D=146211&offers%5B3%5D=146211&offers%5B4%5D=34851&offers%5B5%5D=34851&offers%5B6%5D=164903&offers%5B7%5D=164903&offers%5B8%5D=164905&offers%5B9%5D=164905&sign=3651d5d2ccb817be1b31f0018c1dbde0&token={TOKEN}',
    f'offers%5B0%5D=44019&offers%5B10%5D=87235&offers%5B11%5D=87235&offers%5B12%5D=164909&offers%5B13%5D=164909&offers%5B14%5D=146544&offers%5B15%5D=146544&offers%5B16%5D=34803&offers%5B17%5D=34803&offers%5B18%5D=125680&offers%5B19%5D=125680&offers%5B1%5D=44019&offers%5B2%5D=34855&offers%5B3%5D=34855&offers%5B4%5D=34865&offers%5B5%5D=34865&offers%5B6%5D=88156&offers%5B7%5D=88156&offers%5B8%5D=59661&offers%5B9%5D=59661&sign=abbe2da27ff7a62a2832e060cf9aa1ac&token={TOKEN}',
    f'offers%5B0%5D=34801&offers%5B10%5D=146542&offers%5B11%5D=146542&offers%5B12%5D=164899&offers%5B13%5D=164899&offers%5B14%5D=154998&offers%5B15%5D=154998&offers%5B16%5D=151739&offers%5B17%5D=151739&offers%5B18%5D=87243&offers%5B19%5D=87243&offers%5B1%5D=34801&offers%5B2%5D=149333&offers%5B3%5D=149333&offers%5B4%5D=165055&offers%5B5%5D=165055&offers%5B6%5D=155000&offers%5B7%5D=155000&offers%5B8%5D=72359&offers%5B9%5D=72359&sign=4c36b9f606c6bc3df6592ab855e4bf01&token={TOKEN}',
    f'offers%5B0%5D=165057&offers%5B10%5D=34794&offers%5B11%5D=34794&offers%5B12%5D=87213&offers%5B13%5D=87213&offers%5B14%5D=164895&offers%5B15%5D=164895&offers%5B16%5D=87245&offers%5B17%5D=87245&offers%5B18%5D=127889&offers%5B19%5D=127889&offers%5B1%5D=165057&offers%5B2%5D=164901&offers%5B3%5D=164901&offers%5B4%5D=164897&offers%5B5%5D=164897&offers%5B6%5D=59615&offers%5B7%5D=59615&offers%5B8%5D=151743&offers%5B9%5D=151743&sign=145b66e4a03e05ebe1355724bade0b83&token={TOKEN}',
    f'offers%5B0%5D=34859&offers%5B10%5D=55173&offers%5B11%5D=55173&offers%5B12%5D=87223&offers%5B13%5D=87223&offers%5B14%5D=59619&offers%5B15%5D=59619&offers%5B16%5D=137655&offers%5B17%5D=137655&offers%5B18%5D=34825&offers%5B19%5D=34825&offers%5B1%5D=34859&offers%5B2%5D=155004&offers%5B3%5D=155004&offers%5B4%5D=87227&offers%5B5%5D=87227&offers%5B6%5D=170671&offers%5B7%5D=170671&offers%5B8%5D=170669&offers%5B9%5D=170669&sign=bf9d672c2ab8db5e77b3c0c2cc8ef4ad&token={TOKEN}',
    f'offers%5B0%5D=170665&offers%5B10%5D=87239&offers%5B11%5D=87239&offers%5B12%5D=159278&offers%5B13%5D=159278&offers%5B14%5D=40801&offers%5B15%5D=40801&offers%5B16%5D=155002&offers%5B17%5D=155002&offers%5B18%5D=76207&offers%5B19%5D=76207&offers%5B1%5D=170665&offers%5B2%5D=34841&offers%5B3%5D=34841&offers%5B4%5D=127891&offers%5B5%5D=127891&offers%5B6%5D=34883&offers%5B7%5D=34883&offers%5B8%5D=87231&offers%5B9%5D=87231&sign=ef8df8c02379c522cfe63ea4e9ecb63d&token={TOKEN}',
    f'offers%5B0%5D=170667&offers%5B10%5D=170663&offers%5B11%5D=170663&offers%5B12%5D=107839&offers%5B13%5D=107839&offers%5B14%5D=87255&offers%5B15%5D=87255&offers%5B16%5D=87247&offers%5B17%5D=87247&offers%5B18%5D=87233&offers%5B19%5D=87233&offers%5B1%5D=170667&offers%5B2%5D=87253&offers%5B3%5D=87253&offers%5B4%5D=34798&offers%5B5%5D=34798&offers%5B6%5D=87229&offers%5B7%5D=87229&offers%5B8%5D=164907&offers%5B9%5D=164907&sign=c40477656b88f983b2ddcc339075c901&token={TOKEN}',
    f'offers%5B0%5D=87215&offers%5B10%5D=162823&offers%5B11%5D=162823&offers%5B12%5D=162821&offers%5B13%5D=162821&offers%5B14%5D=162819&offers%5B15%5D=162819&offers%5B16%5D=162817&offers%5B17%5D=162817&offers%5B18%5D=162815&offers%5B19%5D=162815&offers%5B1%5D=87215&offers%5B2%5D=87207&offers%5B3%5D=87207&offers%5B4%5D=162831&offers%5B5%5D=162831&offers%5B6%5D=162829&offers%5B7%5D=162829&offers%5B8%5D=162825&offers%5B9%5D=162825&sign=608276282b7a0b855c9b5933eac0f70f&token={TOKEN}',
]