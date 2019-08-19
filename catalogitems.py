from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogwithusers.db', connect_args={'check_same_thread': False})
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
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Catalog for Paintball
catalog1 = Categories(user_id=1, name="Paintball")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Mask", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     style="Outdoors",  price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Paintball Marker", description="with garlic and parmesan",
                     style="Outdoors", price="$499.00", categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Air Tank", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     style="Outdoors", price="$180.00", categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Padding", description="fresh baked and served with ice cream",
                     style="Outdoors", price="$20.99", categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Paintballs", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem4)
session.commit()

# Catalog for Airsoft
catalog1 = Categories(user_id=1, name="Airsoft")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Airsoft Mask", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Airsoft BB's", description="with garlic and parmesan",
                     style="Outdoors", price="$499.00", categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Airsoft Helmet", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     style="Outdoors", price="$180.00", categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Airsoft Gun", description="fresh baked and served with ice cream",
                     style="Outdoors", price="$20.99", categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Airsoft Green Gas", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem4)
session.commit()

# Catalog for Backpacking
catalog1 = Categories(user_id=1, name="Backpacking")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Backpacking Tents", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Backpack", description="with garlic and parmesan",
                     style="Outdoors", price="$499.00", categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Sleeping Bag", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     style="Outdoors", price="$180.00", categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Backpacking Sleeping Pad", description="fresh baked and served with ice cream",
                     style="Outdoors", price="$20.99", categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Backpacking Stove", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem4)
session.commit()

CatalogItem5 = CatalogItem(user_id=1, name="Water Treatment", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem5)
session.commit()

# Catalog for Fishing
catalog1 = Categories(user_id=1, name="Fishing")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Fishing Rod and Reel", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Hooks", description="with garlic and parmesan",
                     style="Outdoors", price="$499.00", categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Bait", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     style="Outdoors", price="$180.00", categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Lures", description="fresh baked and served with ice cream",
                     style="Outdoors", price="$20.99", categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Bobber", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem4)
session.commit()

CatalogItem5 = CatalogItem(user_id=1, name="Sinkers", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem5)
session.commit()

# Catalog for kayaking
catalog1 = Categories(user_id=1, name="kayak")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Paddle", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Personal flotation device", description="with garlic and parmesan",
                     style="Outdoors", price="$499.00", categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Dry Bag", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     style="Outdoors", price="$180.00", categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Signaling whistle", description="fresh baked and served with ice cream",
                     style="Outdoors", price="$20.99", categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Swimwear", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem4)
session.commit()

# Catalog for Archery
catalog1 = Categories(user_id=1, name="Archery")

session.add(catalog1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Bows", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     style="Outdoors", price="$40", categories=catalog1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Quivers", description="with garlic and parmesan",
                     style="Outdoors", price="$499.00", categories=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Arrows", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     style="Outdoors", price="$180.00", categories=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Targets", description="fresh baked and served with ice cream",
                     style="Outdoors", price="$20.99", categories=catalog1)

session.add(catalogItem3)
session.commit()

CatalogItem4 = CatalogItem(user_id=1, name="Releases", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem4)
session.commit()

CatalogItem5 = CatalogItem(user_id=1, name="Armguards", description="Made with grade A beef",
                     style="Outdoors", price="$50.00", categories=catalog1)

session.add(CatalogItem5)
session.commit()

print ("added menu items!")