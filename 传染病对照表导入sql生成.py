from dask.config import update

import config
import pandas as pd

mapp=pd.read_excel('/Users/ryan/Desktop/mapping.xlsx')

print(f"shape:{mapp.shape}" )
print(mapp.columns[0])


for index,i in enumerate(mapp[mapp.columns[0]]):
    print( f"updata hbos_business.mapping set third_code='{mapp["third_code"][index]}' third_name='{mapp["third_name"][index]}' where his_name='{mapp["his_name"][index]}' and org_id='20044001' and is_deleted=0")
