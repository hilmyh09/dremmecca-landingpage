# Jadiumrah Landing Page

Landing page statis untuk brand **Jadiumrah**.
Satu file `index.html` (Tailwind CSS via CDN + Google Fonts Inter), tanpa build step. Cukup buka `index.html` di browser.

## Positioning
- Core message: "Bukan sekadar berangkat bersama, tetapi berumrah dengan pendampingan yang lebih personal."
- USP: grup ideal 25 jamaah, maksimal 29.
- Segmen: jamaah senior, pasangan muda, keluarga, baru pertama umrah.

## Struktur
```
jadiumrah/
├── index.html          # halaman utama
└── assets/images/
    └── hero.jpg        # gambar hero (1200px, placeholder)
```

## Yang perlu dicek sebelum live
- [ ] **Nomor WhatsApp**: saat ini pakai nomor Dreammecca (`6281225740093`). Ganti semua `wa.me/...` kalau Jadiumrah pakai nomor sendiri.
- [ ] **Meta Pixel ID**: saat ini pakai Pixel Dreammecca. Ganti di `fbq('init', ...)` atau hapus bloknya.
- [ ] Ganti `assets/images/hero.jpg` dengan foto Jadiumrah.
- [ ] Ganti logo placeholder (huruf "J") dengan logo asli.

## Tracking
Setiap CTA memanggil `track(event, posisi)` ke Meta Pixel: `Lead` (hero, bottom), `Contact` (navbar, komitmen).
Semua link WhatsApp diawali tag `[LP-JADIUMRAH]`.
