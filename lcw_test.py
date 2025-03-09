from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver baslat
driver = webdriver.Chrome()
print("WebDriver baslatildi.")

# LC Waikiki ana sayfasina git
driver.get("https://www.lcwaikiki.com")
print("LC Waikiki ana sayfasina gidildi.")

# Sayfa basligini kontrol et
assert "LCW.com" in driver.title, "Sayfa basligi uyusmazligi!"
print("Sayfa basligi dogru, 'LCW.com' iceriyor.")

# Ana sayfada 'Ev & Yasam' kategori butonuna tikla
kategoriler_button = driver.find_element(By.XPATH, "//*[@id='header__container']/header/div[3]/nav/ul/li[9]/a")
print("Ev & Yasam kategori butonu bulunarak tiklama yapildi.")

kategoriler_button.click()

# Kategoriler sayfasinin acildigini dogrula
time.sleep(3)  # Sayfanin yuklenmesi icin bekle
current_url = driver.current_url
assert "ev-yasam-t-5" in current_url, "Ev & Yasam sayfasi yuklenmedi!"
print("Ev & Yasam kategorisi sayfasi basariyla acildi. URL kontrolu basarili.")

# Testi sonlandir ve tarayiciyi kapat
driver.quit()
print("Test tamamlandi, tarayici kapatildi.")
