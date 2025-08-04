import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple

user_profile = namedtuple("userProfile",["flavor", "aroma"])
print(user_profile)
