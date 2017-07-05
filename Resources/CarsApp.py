from PO.Cars import HomePage, TopNav, Search


def cars_home_page(setup,url):
    HomePage.CarsAppHomePage(setup).open_homepage(url)


def cars_home_page_header_menu(setup):
    TopNav.HeaderMenus(setup).cars_header_menus()


def cars_home_page_search_menu(setup):
    Search.VehicleSearch(setup).cars_search_page_menu()


def search_car_by_make(setup, input_data):
    Search.VehicleSearch(setup).search_cars(input_data)


def search_cars_by_body_style(setup,input_data):
    Search.VehicleSearch(setup).search_cars(input_data)
