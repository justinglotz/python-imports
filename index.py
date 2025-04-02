from appliances import CoffeeMaker, DishWasher, Refrigerator, Dryer, Washer, CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_washer.wash_clothes("delicates")
samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes("low")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

kenmore = CanOpener("black")
kenmore.open_can()
