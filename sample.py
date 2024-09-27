from pygsielev import ElevationExtractor

engine = ElevationExtractor(data_dir="data/")
print(engine.get_elevation(
    lon=138.727299,
    lat=35.360785,
))
