from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Configuración
options = Options()
# Podés comentar esto si querés ver el navegador
# options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--lang=es-419')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Ir a Google Maps con búsqueda ya lista
driver.get("https://www.google.com/maps/search/empresas+Caseros+Buenos+Aires/")

time.sleep(5)

# Hacer scroll para cargar más resultados
scroll_area = driver.find_element(By.CSS_SELECTOR, "div[role='feed']")
for _ in range(15):
    driver.execute_script("arguments[0].scrollBy(0, 1000);", scroll_area)
    time.sleep(1.5)

# Obtener todos los bloques de resultados
resultados = driver.find_elements(By.CSS_SELECTOR, "div[role='article']")

print(f"🔍 Se encontraron {len(resultados)} resultados.")

empresas = []

for idx, resultado in enumerate(resultados):
    try:
        ActionChains(driver).move_to_element(resultado).click().perform()
        time.sleep(4)

        nombre = driver.find_element(By.CLASS_NAME, "DUwDvf").text

        direccion = ""
        telefono = ""
        web = ""
        whatsapp = ""
        email = ""

        # Intentar encontrar todos los bloques informativos
        info_bloques = driver.find_elements(By.CLASS_NAME, "Io6YTe")

        for bloque in info_bloques:
            texto = bloque.text.lower()
            if "dirección" in texto:
                direccion = bloque.find_element(By.XPATH, "..").text.split('\n')[-1]
            elif "teléfono" in texto:
                telefono = bloque.find_element(By.XPATH, "..").text.split('\n')[-1]
            elif "sitio web" in texto:
                web = bloque.find_element(By.XPATH, "..").text.split('\n')[-1]
            elif "whatsapp" in texto:
                whatsapp = bloque.find_element(By.XPATH, "..").text.split('\n')[-1]
            elif "@" in bloque.text:
                email = bloque.text

        print(f"✔ Empresa {idx+1}: {nombre}")
        empresas.append({
            "Nombre": nombre,
            "Dirección": direccion,
            "Teléfono": telefono,
            "Web": web,
            "WhatsApp": whatsapp,
            "Email": email
        })

    except Exception as e:
        print(f"❌ Error al procesar resultado {idx+1}: {e}")
        continue

driver.quit()

# Guardar en Excel
df = pd.DataFrame(empresas)
df.to_excel("empresas_tres_de_febrero_detallado.xlsx", index=False)
print("✅ Archivo generado: empresas_tres_de_febrero_detallado.xlsx")
