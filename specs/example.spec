Specification Heading
=====================

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run
	gauge specs

Özdilekteyim İslemleri
-------------------------------
*Uygulama açılır ve uygulamanın açıldığı kontrolü yapılır
*Kategori sayfasını açıp rastgele ürün seçilir
*Ürün detay sayfasına gidilip ürün favorilere eklenir
*Login islemleri yapılır sayfada geriye dönülür
*Ürün ekleme islemleri yapılır




















//* "5" saniye bekle
//*"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]" değerini içerdiğni kontrol et
//- Uygulamanın açıldığı kontrol edilir

//* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" id'li elemante tikla
//* "3" saniye bekle

//Alışveriş sayfasının açıldıgı doğrulanır
//*"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.TextView" id'li element "Ev Tekstili" text değerini içerdiğni kontrol et
//*"3" saniye bekle

//Katogiriler Sayfası Açılır
//* "//android.widget.FrameLayout[@content-desc='Kategoriler']/android.widget.ImageView" elemente tikla
//*"3" saniye bekle
//-Katogoriler Sayfasının açıldıgı dogrulanırx
//*"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView" id'li element "Kadın" text değerini içerdiğni kontrol et
//*"3" saniye bekle

//menüden “Kadın” Seçeneğine tıklanır
//* "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView" elemente tikla
//* "3" saniye bekle

//“pantolon” kategorisi açılır
//* "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.TextView" elemente tikla
//* "3" saniye bekle

//- Sayfanın en aşagasına doğru iki kere scrol edilir.
//*Scrolldown yapılır
//* "3" saniye bekle

//- Ürünlerden rasgele bir ürün seçilir.
//* "com.ozdilek.ozdilekteyim:id/imageView" ürün seçilir
//* "3" saniye bekle

//- Ürün detay sayfası açıldığı kontrol edilir.
//*"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView" id'li element "SEPETE EKLE" text değerini içerdiğni kontrol et
//*"3" saniye bekle

//- favoriler butonuna tıklanır.
//* "com.ozdilek.ozdilekteyim:id/imgFav" id'li elemante tikla
//*"3" saniye bekle

//-Giriş yapma sayfasının açıldığı dogrulanır.
//*"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText" id'li element "E - posta Adresi" text değerini içerdiğni kontrol et
//*"3" saniye bekle

//- Kullanıcı adı alanına “text” bilgisi girilir
//* "com.ozdilek.ozdilekteyim:id/etEposta" inputuna "ozdilekappiumdeneme@gmail.com" mesajını yaz
//* "3" saniye bekle

//- Password alanına şifre yazılır
//* "com.ozdilek.ozdilekteyim:id/etPassword" inputuna "ozdilekcom" mesajını yaz
//* "3" saniye bekle

//* "com.ozdilek.ozdilekteyim:id/ivBack" id'li elemante tikla
//*"2" saniye bekle

//*"com.ozdilek.ozdilekteyim:id/ivBack" id'li elemante tikla
//*"2" saniye bekle

//* "com.ozdilek.ozdilekteyim:id/imageView" ürün seçilir
//* "2" saniye bekle

//* "com.ozdilek.ozdilekteyim:id/tvInSizeItem" ürün seçilir
//* "3" saniye bekle

//*"com.ozdilek.ozdilekteyim:id/relLayAddCartBtn" id'li elemante tikla
//*"2" saniye bekle

