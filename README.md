# bestcloud_academy
Bestcloud Academy


Görev 1:

Öncelikle: export webhook_url="https://webhook.site/17b407f8-5266-4e83-8305-57d60136995e" komutunu girerek tek satırda bir environment variable tanımladım. 

Bunun olası bir bilgisayar kapanma durumunda silineceğini bildiğim için ardından

> source ~/.bashrc komutunu girdim.

Aynı zamanda /etc/environment dosyasının içine girerek webhook_url="https://webhook.site/17b407f8-5266-4e83-8305-57d60136995e yazarak kaydettim. Bilgisayarı yeniden başlattığımda printenv komutunu girdim ve tanımladığım environment variable gördüm. POST isteği denediğimde belirttiğim url'de istek geldi.

Görev 2:

Öncelikle : 

docker build -t bcfm . komutuyla image haline getirip,


docker run --env webhook_url -d -p 5000:5000 bcfm komutuyla container haline getirdim.
