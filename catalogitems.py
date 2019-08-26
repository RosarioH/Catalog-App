from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogwithusers.db',
                       connect_args={
                           'check_same_thread': False})
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='''https://pbs.twimg.com/profile_images/2671170543/
             18debd694829ed78203a5a36dd364160_400x400.png''')
session.add(User1)
session.commit()

# Catalog for Paintball
catalog1 = Categories(user_id=1, name="Paintball")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Mask",
                           description="""The next evolution in the Mask line
                           is also the next evolution in paintball eye and
                           face protection technology.""",
                           style="Outdoors",  price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Paintball Marker",
                           description="""Once you pick-up this paintball
                           marker you will not be able to set it down as
                           the newly designed ergonomics feels amazing!""",
                           price="$499.00",
                           categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Air Tank",
                           description="""Our air tanks offer an
                           affordable option to the player who wants
                           to upgrade to a High Pressure Air system.""",
                           style="Outdoors", price="$180.00",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Padding",
                           description="""Paintball Pads are a vital piece of
                           equipment if you want to keep yourself safe and
                           protected on the field.""",
                           style="Outdoors", price="$20.99",
                           categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Paintballs",
                           description="""Are paintballs have been
                           in production for about 10 years and is
                           a great brand of premium paintballs.""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem4)
session.commit()

# Catalog for Airsoft
catalog1 = Categories(user_id=1, name="Airsoft")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Airsoft Mask",
                           description="Airsoft Protective Mask",
                           style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Airsoft BB's",
                           description="""One of the most popular BBs out in
                           the market, it's as close to a perfect 6.00mm as
                           you can get.""",
                           style="Outdoors", price="$499.00",
                           categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Airsoft Helmet",
                           description="""The added protection of the Tactical
                           Helmet allows Airsoft players a bolder style of
                           play.""",
                           style="Outdoors", price="$180.00",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Airsoft Gun",
                           description="""The perfect Basic Training entry
                           into Airsoft in a complete affordable package.""",
                           style="Outdoors", price="$20.99",
                           categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Airsoft Green Gas",
                           description="""Green Gas can for all blow
                           back pistols""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem4)
session.commit()

# Catalog for Backpacking
catalog1 = Categories(user_id=1, name="Backpacking")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Backpacking Tents",
                           description="""Keeping your backpacking tent
                           lightweight is extremely important. It is one
                           of the biggest items in your pack and
                           therefore, one of the biggest opportunities
                           to save weight.""",
                           style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Backpack",
                           description="""Zip-off daypack lets you carry
                           just the essentials for a day hike or urban
                           excursion""",
                           style="Outdoors", price="$499.00",
                           categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Sleeping Bag",
                           description="""DriDown insulation has a
                           hydrophobic finish, allowing the plumes to
                           loft better and dry faster than untreated
                           down""",
                           style="Outdoors", price="$180.00",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Backpacking Sleeping Pad",
                           description="""Exclusive Atmos foam reduces
                           weight by nearly 10 percent and boosts
                           compressibility to keep your winter
                           backpack even lighter""",
                           style="Outdoors", price="$20.99",
                           categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Backpacking Stove",
                           description="""Faster than any other
                           stove in the stove range, the Flash
                           makes quick work out of boiling
                           water for your meal, melting snow or
                           disinfecting water to drink in the
                           backcountry.""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem4)
session.commit()

CatalogItem5 = CatalogItem(user_id=1, name="Water Treatment",
                           description="""Removes particles, bacteria,
                           cysts and parasites larger than 0.2 microns,
                           including protozoa such as giardia and
                           cryptosporidia""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem5)
session.commit()

# Catalog for Fishing
catalog1 = Categories(user_id=1, name="Fishing")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Fishing Rod and Reel",
                           description="""Best rod and reel on the market""",
                           style="Outdoors", price="$40",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Hooks",
                           description="Best rod and reel on the market",
                           style="Outdoors", price="$499.00",
                           categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Bait",
                           description="""Freshwater & saltwater fishing
                           lures, soft baits, hard baits, buzzbaits, lure
                           kits & more""",
                           style="Outdoors", price="$180.00",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Lures",
                           description="""Freshwater & saltwater fishing lures,
                           soft baits, hard baits, buzzbaits, lure kits
                           & more""",
                           style="Outdoors", price="$20.99",
                           categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Bobber",
                           description="""Discover the best Fishing Corks,
                           Floats & Bobbers in Best Sellers.""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem4)
session.commit()

CatalogItem5 = CatalogItem(user_id=1, name="Sinkers",
                           description="""Discover the best Fishing Sinker,
                           Floats & Bobbers in Best Sellers.""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem5)
session.commit()

# Catalog for kayaking
catalog1 = Categories(user_id=1, name="kayak")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Paddle",
                           description="""kayak paddles keep you in
                           steady control through every twist and
                           turn.""",
                           style="Outdoors", price="$40",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Personal flotation device",
                           description="""A personal flotation device is a
                           piece of equipment designed to assist a wearer
                           to keep afloat in water.""",
                           style="Outdoors", price="$499.00",
                           categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Dry Bag",
                           description="""For over 30 years, these waterproof
                           dry bags have been the best rated dry bags on the
                           market. """,
                           style="Outdoors", price="$180.00",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Signaling whistle",
                           description="""You'll feel safer when traveling with
                           one of our rescue whistles.""",
                           style="Outdoors", price="$20.99",
                           categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Swimwear",
                           description="Best quality swimwear",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem4)
session.commit()

# Catalog for Archery
catalog1 = Categories(user_id=1, name="Archery")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Bows",
                           description="""In modern archery,
                           a compound bow is a bow that uses a levering
                           system, usually of cables and pulleys,
                           to bend the limbs.""",
                           style="Outdoors", price="$40",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Quivers",
                           description="""Archery quiver to fit any
                           bow hunter and any style of archery hunting!""",
                           style="Outdoors", price="$499.00",
                           categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Arrows",
                           description="""Shop precision Arrows""",
                           style="Outdoors", price="$180.00",
                           categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Targets",
                           description="Silhouette Reactive Shooting Target",
                           style="Outdoors", price="$20.99",
                           categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Releases",
                           description="""Archery releases and bow
                           release aids.""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem4)
session.commit()

CatalogItem5 = CatalogItem(user_id=1, name="Armguards",
                           description="""Selection of arm guards, finger
                           tabs and gloves for your bow.""",
                           style="Outdoors", price="$50.00",
                           categories=catalog1)

session.add(CatalogItem5)
session.commit()

print("added menu items!")
