from template_method.classes import VegetarianPizza, ChickenPizza

if __name__ == '__main__':
    vege = VegetarianPizza()
    vege.make_pizza()
    print('------------------')
    chicken = ChickenPizza()
    chicken.make_pizza()
