# scraping-indeed

Hallo,

Ini adalah project pertama saya. Saya tertarik dalam dunia data science khususnya pada domain data scraping dan analisis, sehingga saya membuat project pertama adalah scraping Data Analyst Jobs di Indonesia yang ada di portal kerja Indeed.com.

Untuk kodenya dapat dilihat di file niko_indeed.py. Saya menggunakan package datetime untuk menentukan waktu sekarang (hasil kolom today), requests dan bs4 untuk scraping, serta pandas untuk save hasil scraping kedalam file csv.

Yang pertama saya lakukan adalah membuat hearder dan setting url, kemudian saya test untuk respon adalah 200 yang artinya diterima dan bisa lanjut untuk scraping.

Setelah itu saya membuat List "datas" kosong untuk menampung hasil scraping, kemudian me-looping tiap halaman yang discrape dan save hasilnya di list "datas" yang sudah dibuat tadi.

Terakhis, list datas saya save menjadi file csv dengan package pandas.

Saya ucapkan maaf jika ada kesalahan atau kurang rapinya kode saya, saya juga berharap ada kritik saran atau review yang membangun. Atas perhatiannya, saya ucapkan "BIG Thanks".

Salam,
Niko Prabowo
nikoberwibowo@gmail.com
+62822-4243-8462
