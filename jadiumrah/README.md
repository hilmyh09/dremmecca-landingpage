# Jadiumrah — Landing Page (HTML Sales Page untuk Scalev)

Satu file HTML lengkap (`jadiumrah.html`) mengikuti gaya landing page Dreammecca di Scalev (hero gelap, kartu putih, tombol WhatsApp hijau, panel CTA gelap) dengan palet Jadiumrah tanpa aksen emas. Font Poppins dari Google Fonts (satu-satunya resource eksternal selain gambar). CSS dan JavaScript inline. Versi editorial (commit d4d7cb3) dan versi kolom tunggal (commit c66f0fc) tersimpan di riwayat git. Tidak memerlukan npm, build, server, framework, atau font eksternal. Sumber konten: PDF "Jadiumrah Branding dan Positioning" (Oktober 2026) dan foto dokumentasi yang diberikan pemilik.

## Struktur
```
jadiumrah/
├── jadiumrah.html            # halaman lengkap, siap diimpor ke Scalev
├── README.md
└── assets/images/
    ├── logo-cream.png            788×245    (logo resmi versi krem, latar transparan)
    ├── keluarga-kabah.jpg        1000×1333  (IMG_1160.HEIC, foto hero) — TIDAK di repo, lihat catatan
    └── og-image.jpg              1200×630   (potongan IMG_1155) — TIDAK di repo, lihat catatan

Foto jamaah sengaja tidak disimpan di repositori ini karena repo bersifat publik dan foto menampilkan wajah. Foto ada di paket ZIP yang dikirim ke pemilik, dan sudah tertanam (base64) di `jadiumrah-scalev.html` dalam paket yang sama. Untuk meninjau `jadiumrah.html` secara lokal, letakkan kedua foto itu di `assets/images/`.
```

## Menjalankan / meninjau
Buka `jadiumrah.html` langsung di browser (klik dua kali). Gambar dimuat dari folder `assets/images/` di sebelahnya.

## Konfigurasi
Semua data bisnis ada di satu objek `JADIUMRAH_CONFIG` di bagian atas `<script>` pada `jadiumrah.html`:

| Kunci | Fungsi | Status saat ini |
|---|---|---|
| `whatsapp.number` | Nomor resmi, format `62xxxxxxxxxx` tanpa `+`/spasi | `6281110066986` (dari pemilik, 28 Okt 2026). Kosongkan untuk menonaktifkan CTA |
| `whatsapp.message` | Pesan pembuka WhatsApp | Terisi sesuai brief |
| `contact.phone`, `contact.email` | Kolom "Kontak" di footer | Kosong (kolom disembunyikan) |
| `social.instagram` dst. | Kolom "Media sosial" (URL lengkap) | Kosong (kolom disembunyikan) |
| `address` | Kolom "Alamat", boleh multi-baris dengan `\n` | Kosong |
| `legal.companyName`, `legal.licenseNumber`, `legal.notes` | Baris legal di footer dan tanda centang di hero | PT. Globalindo Sukses Maksima, Izin PPIU 02200064127450010 |
| `logoUrl` | Opsional, URL HTTPS pengganti logo; jika kosong dipakai `assets/images/logo-cream.png` | Kosong (logo lokal terpasang) |
| `groupSize.target` / `max` / `confirmed` | 25 / 29 / `false`. Selama `false`, halaman memakai frasa "jumlah jamaah dalam setiap rombongan" dan **tidak** menampilkan angka | Belum dikonfirmasi |
| `imageSources` | Catatan asal setiap foto | Terisi |

Saat `whatsapp.number` diisi, semua tombol konsultasi otomatis menjadi tautan `https://wa.me/<nomor>?text=<pesan>` yang terbuka di tab baru, dan catatan "kanal sedang disiapkan" hilang.

## Mengimpor ke Scalev (HTML Mode, tipe HTML Sales Page)
1. Pastikan URL gambar sudah publik (lihat bagian berikut) dan `JADIUMRAH_CONFIG` sudah diisi.
2. Di Scalev, buat/buka halaman dengan tipe **HTML Sales Page**.
3. Buka tab **Code → Import HTML**, lalu tempel atau unggah seluruh isi `jadiumrah.html`.
4. Simpan dan buka pratinjau Scalev. Periksa: tagline dua baris, menu mobile, FAQ, dan tombol WhatsApp.
5. Di pengaturan **Security/CSP** Scalev, izinkan domain di bagian "Domain eksternal" bawah ini.

Halaman memuat font Poppins dari Google Fonts; tidak ada script tracking atau integrasi lain.

## Dua varian file
- `jadiumrah.html` (repo): path gambar relatif, untuk pengembangan.
- `jadiumrah-scalev.html` (dalam paket ZIP): gambar tertanam sebagai data URI, siap langsung diimpor ke Scalev tanpa hosting gambar. `og:image` dinonaktifkan di varian ini karena crawler media sosial butuh URL publik; isi bila sudah ada hosting.

## URL gambar untuk publikasi (jika tidak memakai varian tertanam)
`jadiumrah.html` memakai path relatif `assets/images/...`. Scalev memerlukan URL HTTPS publik. Dua pilihan:

**A. Hosting dari repositori GitHub ini (publik).** Setelah folder `jadiumrah/assets/images/` ter-push, ganti semua `assets/images/` menjadi
`https://raw.githubusercontent.com/hilmyh09/dremmecca-landingpage/<branch>/jadiumrah/assets/images/`
(gunakan `main` setelah branch digabung). Contoh satu perintah:
```
sed -i 's#assets/images/#https://raw.githubusercontent.com/hilmyh09/dremmecca-landingpage/main/jadiumrah/assets/images/#g' jadiumrah.html
```

**B. Unggah ke media library Scalev atau CDN lain**, lalu ganti ketiga `src`/`og:image` (foto hero, logo di header dan footer, og-image) dengan URL yang diberikan.

Catatan: foto menampilkan wajah jamaah. Pastikan izin penggunaan dari yang bersangkutan sudah ada sebelum dipublikasikan.

## Domain eksternal yang perlu diizinkan di Security/CSP
| Kebutuhan | Domain |
|---|---|
| Gambar (bila pilihan A) | `raw.githubusercontent.com` |
| Gambar (bila pilihan B) | domain media Scalev / CDN yang dipakai |
| Tautan tombol konsultasi | `wa.me` (hanya tautan keluar, bukan resource yang dimuat) |
| Font Poppins | `fonts.googleapis.com` (stylesheet) dan `fonts.gstatic.com` (file font) |

## Data yang masih perlu dilengkapi sebelum publikasi
- [x] **Nomor WhatsApp** → `6281110066986` sesuai arahan pemilik. Catatan: spanduk pada foto menampilkan `+62 811-1008-6986` (beda satu digit); pastikan yang dipakai memang benar.
- [ ] **Media sosial dan situs web** → spanduk menampilkan Instagram `jadiumrah.indonesia` dan `www.jadiumrah.com`; isi `social.instagram` / `social.website` setelah dikonfirmasi.
- [x] **Nama badan usaha dan izin PPIU** → terisi.
- [ ] **Alamat kantor, telepon, email** → `address`, `contact`.
- [x] **Logo resmi** → versi krem terpasang di header dan footer (`assets/images/logo-cream.png`).
- [ ] **Kebijakan kapasitas rombongan** (target 25, maksimal 29) → ubah `groupSize.confirmed` ke `true` hanya setelah ditetapkan tim.
- [ ] **Persetujuan isi "Tenang" dan "Menyenangkan"** serta alur tiga tahap: ditulis dari PDF sebagai rancangan pelayanan, perlu disetujui pemilik.
- [ ] **Izin foto** dari jamaah yang tampak di dokumentasi.
- [ ] **Domain/URL final** halaman untuk `og:url`/canonical (belum ditambahkan karena belum diketahui).

Belum ada di halaman dan sengaja tidak dibuat: testimoni, rating, jumlah alumni, harga, jadwal, fasilitas, kartu paket, formulir, script tracking.

## Landing page promo (hard selling), folder `promo/`
Tiga halaman program 2027 yang dibangun dari script iklan pemilik dengan `promo/build.py`:

| File | Program | Tanggal | Penerbangan | Harga mulai |
|---|---|---|---|---|
| `umroh-hemat-januari-2027.html` | Umroh Hemat, 9 hari | 12, 19, 26 Jan 2027 | transit: Qatar Airways / Etihad / Oman Air | Rp32,9 jt |
| `umroh-awal-ramadan-2027.html` | Umroh Awal Ramadan, 9 hari | 2, 9 Feb 2027 | Saudia Airlines direct | Rp35,9 jt |
| `umroh-syawal-2027.html` | Umroh Syawal, 9 hari | transit 15, 20 Mar · direct 12, 18 Mar 2027 | Qatar/Emirates · Saudia/Garuda | Rp30,9 jt · Rp35,9 jt |

Cara build: `python3 promo/build.py <folder_gambar> <folder_output>`. Versi di repo memakai path gambar relatif (foto jamaah tidak disimpan di repo); versi output menanamkan foto sebagai base64 JPEG/PNG dan siap diimpor ke Scalev. Setiap tombol tanggal membuka WhatsApp dengan pesan yang sudah menyebut program dan tanggalnya. Tidak ada countdown, sisa seat, atau fasilitas yang tidak disebut di script; harga selalu ditulis "mulai dari" dan diarahkan ke konfirmasi admin.
