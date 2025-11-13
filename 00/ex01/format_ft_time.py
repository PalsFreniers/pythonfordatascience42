import datetime as dt

print(f"Seconds since January 1, 1970: {dt.datetime.today().timestamp():,.4f} "
      + "or {dt.datetime.today().timestamp():.2E} in scientific notation")
print(dt.datetime.today().strftime('%a %d %Y'))
