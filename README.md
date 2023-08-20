# Eksi-Scraping
## Ekşi Sözlük Entry Web Kazıma Aracı

Bu Python projesi, Ekşi Sözlük websitesindeki bir entry başlığındaki tüm entryleri web kazıma yöntemiyle çekmek ve elde edilen verileri bir CSV dosyasına kaydetmek amacıyla oluşturulmuştur.

## Proje Açıklaması

Bu araç, BeautifulSoup ve requests kütüphanelerini kullanarak Ekşi Sözlük websitesinden veri çekme işlemini gerçekleştirir. Verileri daha sonra bir Pandas DataFrame'ine dönüştürüp, son olarak bir CSV dosyasına kaydederek kullanıcıya erişim sağlar. İlgili csv dosyasındaki veri 3 kolondan oluşur: (username,entry,date). Entryler kronolojik olarak tutulur.

## Nasıl Kullanılır

**1.** Projeyi bilgisayarınıza indirin:

**2.** Gerekli kütüphaneleri yükleyin: (BeautifulSoup,Pandas,Requests)
``pip install -r requirements.txt``

**3.** Komut satırında proje dizininde aşağıdaki komutu kullanarak script'i çalıştırın:  
 ``python eksiScraper.py <"entry_basligi_linki">``  
**Örneğin:**  
 ``python eksiScraper.py "https://eksisozluk.com/github--1995063"``  

**4.** İşlem tamamlandığında, proje dizininde `entries.csv` adında bir CSV dosyası oluşturulacaktır. Bu dosya, çekilen verileri içerir.

## Notlar
- Bu araç, Ekşi Sözlük websitesinin yapısına bağlı olduğu için zaman içinde değişikliklere uğrayabilir. Bu durumda, kodun güncellenmesi gerekebilir.
- Web kazıma etik kurallara uymak önemlidir. Bu aracı kullanırken sık sık istek yapmaktan kaçının ve gereksiz yere yük oluşturmayın.

