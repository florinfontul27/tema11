
from pages import AutentificarePage, HomePage

'''
Test 3:
Deschideti https://cafeo.ro/
Click contul meu
Completati  cu o adresa de email
Click cont nou
Completati fiecare casuta, (alegeti dna sau dl, prenume nume parola, , bifati cele 3 casute
Assert pt mesul verde cu contul a fost creat
Asser ca va apare numele si prenumele acolo sus la contul meu
'''
def test_create_account(browser):
    home_page = HomePage(browser)
    customer_page = AutentificarePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    customer_page.type_email_new_account("floringabi3@gmail.com")
    customer_page.click_radio_button()
    customer_page.type_first_name("Florin")
    customer_page.type_last_name("Fontul")
    customer_page.type_password("ceamaitareparola")
    customer_page.check_the_first_box()
    customer_page.check_the_second_box()
    customer_page.click_submit_button()
    assert "Contul dumneavoastră a fost creat." in customer_page.get_succes_messge().text
    assert "Florin Fontul" in customer_page.check_if_name_is_displayed().text