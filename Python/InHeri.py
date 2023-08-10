# Super 부모
# Subb 자식


class ParentRestaurant:
    price = 15000
    
    def __init__(self,name,menu,recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe
        
    def __str__(self):
        return "가게이름 : {}, 가게의 메뉴 : {}, 메뉴의 조리법 :{} ".format(self.name,self.menu,self.recipe)

    def __del__(self):
        pass


class ChildRestaurant(ParentRestaurant):
    price = 2000

rest_in = ChildRestaurant("자식의가게","붕어빵","빵굽기")
print(rest_in)