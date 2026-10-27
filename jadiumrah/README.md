# JadiUmrah Landing Page

Landing page statis untuk program **JadiUmrah** (bagian dari Dreammecca).
Satu file `index.html`, tanpa build step. Cukup buka `index.html` di browser.

## Struktur
```
jadiumrah/
├── index.html          # halaman utama (HTML + CSS + JS dalam satu file)
└── assets/images/
    ├── hero.jpg        # gambar hero (1200px, sudah dioptimasi)
    ├── jamaah.jpg      # gambar rombongan
    └── testi1-3.png    # screenshot testimoni
```

## Yang perlu diisi / dicek sebelum live
- [ ] **Harga paket** di section `PACKAGE` (cari `TODO: isi harga`).
- [ ] **Nomor WhatsApp**: saat ini pakai nomor Dreammecca (`6281225740093`). Ganti semua `wa.me/...` kalau JadiUmrah pakai nomor sendiri.
- [ ] **Meta Pixel ID**: saat ini pakai Pixel Dreammecca. Ganti di `fbq('init', ...)` kalau ada Pixel terpisah.
- [ ] Ganti foto hero/testimoni dengan materi JadiUmrah.

## Tracking
Setiap tombol CTA memanggil `track(event, posisi)` yang mengirim event ke Meta Pixel:
`Lead` (hero, testimoni), `Contact` (konsultasi, sticky), `InitiateCheckout` (paket).
Semua link WhatsApp diawali tag `[LP-JADIUMRAH]` supaya mudah dibedakan di inbox.
