import nfl_data_py as nfl

years = [2022]
df = nfl.import_pbp_data(years, downcast=True, cache=False, alt_path=None)
print(df)
print(nfl.see_pbp_cols())