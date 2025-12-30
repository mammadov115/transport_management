# Transport Management System (Odoo Modulu)

Bu modul Odoo platformasında daşınma əməliyyatlarını və logistika proseslərini effektiv şəkildə idarə etmək üçün hazırlanmışdır. Sistem vasitəsilə nəqliyyat sifarişlərini izləmək, çatdırılma marşrutlarını təyin etmək və məhsul detallarını idarə etmək mümkündür.

## Modulun Funksional İmkanları

* **Avtomatik Ardıcıllıq (Sequencing):** Hər bir nəqliyyat sifarişi üçün sistem tərəfindən unikal "Order Ref" nömrəsinin avtomatik təyin edilməsi.
* **Nəqliyyat Rejimlərinin Seçimi:** Hava, dəniz və quru yolu (Air, Sea, Land) üzrə daşınma növlərinin təsnifatı.
* **Məhsul və Kəmiyyət İdarəetməsi:** Sifariş daxilində birdən çox məhsulun, onların miqdarının və ölçü vahidlərinin (UoM) qeydiyyatı.
* **Incoterm Dəstəyi:** Beynəlxalq ticarət terminlərinin (Incoterms) qeyd olunması imkanı.
* **Marşrut Məlumatları:** Yükün çıxış və təyinat nöqtələrinin, həmçinin çatdırılma müddətinin izlənilməsi.

## Texniki Struktur

Layihə iki əsas model üzərində qurulmuşdur:

1. **Transport Management (`transport.management`):** Sifarişin ümumi məlumatlarını (daşıyıcı, marşrut, nəqliyyat növü) saxlayır.
2. **Transport Management Line (`transport.management.line`):** Sifariş daxilindəki konkret məhsulları və onların texniki göstəricilərini saxlayan alt modeldir.

## Quraşdırılma

Modulu Odoo instansiyanıza əlavə etmək üçün:

1. Repozitoriyanı yükləyin və `transport_management` qovluğunu Odoo-nun `addons` kataloquna yerləşdirin.
2. Odoo interfeysində **Settings** menyusuna daxil olaraq **Developer Mode**-u aktivləşdirin.
3. **Apps** menyusuna keçin və **Update Apps List** düyməsini sıxın.
4. Axtarış hissəsində "Transport Management" yazaraq modulu tapın və **Activate** düyməsinə klikləyin.

## İstifadə Qaydası

1. **Transport** menyusuna daxil olun və "Create" düyməsini sıxın.
2. Daşıyıcı məlumatlarını (Carrier Info), çıxış və təyinat məntəqələrini daxil edin.
3. **Products** bölməsində "Add a line" seçərək daşınacaq məhsulları, onların miqdarını və ölçü vahidlərini əlavə edin.
4. Sifarişi yadda saxladıqda sistem avtomatik olaraq unikal bir referans nömrəsi formalaşdıracaqdır.

## Tələblər

* Odoo (versiya 14.0 və ya daha yuxarı)
* Python 3.x
