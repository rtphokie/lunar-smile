import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)p
    from skyfield.api import load, wgs84
    from skyfield.framelib import ecliptic_frame
    import datetime as dt
    import pytz
    from skyfield import almanac
    from skyfield.api import N, W, wgs84, load

eph = load('de421.bsp')
