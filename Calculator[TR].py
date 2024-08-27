def topla(x, y):
    """
    Bu fonksiyon, iki sayıyı toplar.
    
    Parametreler:
        x (float): İlk sayı.
        y (float): İkinci sayı.
        
    Dönüş:
        float: x ve y'in toplamı.
    """
    return x + y


def çıkarma(x, y):
    """
    Bu fonksiyon, iki sayıyı çıkarır.
    
    Parametreler:
        x (float): İlk sayı.
        y (float): İkinci sayı.
        
    Dönüş:
        float: x ve y'in farkı.
    """
    return x - y


def çarpma(x, y):
    """
    Bu fonksiyon, iki sayıyı çarpar.
    
    Parametreler:
        x (float): İlk sayı.
        y (float): İkinci sayı.
        
    Dönüş:
        float: x ve y'in çarpımı.
    """
    return x * y


def bölme(x, y):
    """
    Bu fonksiyon, iki sayıyı böler.
    
    Parametreler:
        x (float): Bölünen.
        y (float): Bölen.
        
    Dönüş:
        float: Bölüm sonucu.
    """
    if y != 0:
        return x / y
    else:
        return "Saniye 0'a bölme imkansız."


while True:
    print("1. Topla")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    islem = int(input("Lütfen yapmak istediğiniz işlem numarasını seçin: "))

    if islem == 5:
        break

    x = float(input("İlk sayıyı girin: "))
    y = float(input("Ikinci sayıyı girin: "))

    if islem == 1:
        print(f"{x} + {y} = {topla(x, y)}")
    elif islem == 2:
        print(f"{x} - {y} = {çıkarma(x, y)}")
    elif islem == 3:
        print(f"{x} * {y} = {çarpma(x, y)}")
    elif islem == 4:
        print(f"{x} / {y} = {bölme(x, y)}")
    else:
        print("Geçersiz işlem numarası. Lütfen tekrar deneyin.")
