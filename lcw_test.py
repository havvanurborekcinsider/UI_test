import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.title("LC Waikiki Sayfa Kontrolü")
@allure.description("Ana sayfaya gidip, 'Ev & Yasam' kategorisini kontrol eder.")
def test_lc_waikiki():
    # WebDriver başlat
    driver = webdriver.Chrome()
    print("WebDriver başlatıldı.")
    
    try:
        # LC Waikiki ana sayfasına git
        driver.get("https://www.lcwaikiki.com")
        print("LC Waikiki ana sayfasına gidildi.")
        
        # Sayfa başlığını kontrol et
        assert "LCW.com" in driver.title, "Sayfa başlığı uyuşmazlığı!"
        print("Sayfa başlığı doğru, 'LCW.com' içeriyor.")
        
        # Ana sayfada 'Ev & Yaşam' kategori butonuna tıkla
        kategoriler_button = driver.find_element(By.XPATH, "//*[@id='header__container']/header/div[3]/nav/ul/li[9]/a")
        print("Ev & Yaşam kategori butonu bulunarak tıklama yapıldı.")
        kategoriler_button.click()
        
        # Kategoriler sayfasının açıldığını doğrula
        driver.implicitly_wait(10)  # Sayfanın yüklenmesi için bekle
        current_url = driver.current_url
        assert "ev-yasam-t-5" in current_url, "Ev & Yaşam sayfası yüklenmedi!"
        print("Ev & Yaşam kategorisi sayfası başarıyla açıldı. URL kontrolü başarılı.")
    
    except Exception as e:
        allure.attach(str(e), name="Hata Mesajı", attachment_type=allure.attachment_type.TEXT)
        raise  # Hata olduğunda yeniden raise et
    
    finally:
        # Testi sonlandır ve tarayıcıyı kapat
        driver.quit()
        print("Test tamamlandı, tarayıcı kapatıldı.")
