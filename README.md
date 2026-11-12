# Voting Ketua Kelas AiFn2 PWA

Target: https://voting-aifn2.hicall.workers.dev
Eligible: 40 mahasiswa. RUDI HARTANTO (25140200001, Fast-Track) dikecualikan sebagai pemilih dan kandidat.
Deadline server: Kamis, 12 November 2026 pukul 22.00 WIB (15.00 UTC).

## Repository baru
1. Buat repository GitHub baru, misalnya `voting-aifn2`.
2. Ekstrak ZIP dan upload seluruh isinya ke root repository.
3. Buat repository secrets dengan nilai yang sama seperti InSD2: `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`, `ADMIN_KEY`, `TURNSTILE_SECRET_KEY`.
4. Di Turnstile widget yang sama, tambahkan hostname `voting-aifn2.hicall.workers.dev` pada Hostname Management. Site Key dan Secret Key boleh tetap sama.
5. GitHub > Actions > Bootstrap and Deploy AiFn2 PWA > Run workflow. Isi Turnstile Site Key produksi.
6. Workflow otomatis membuat D1 `voting-aifn2`, migration, secrets, QA, deploy, dan commit database ID.

## PWA
Halaman dapat dipasang melalui tombol `Pasang aplikasi` di browser yang mendukung. App shell dicache, tetapi endpoint `/api/*` selalu network-only agar voting dan waktu server tidak stale.

## URL
- Pemilih: `https://voting-aifn2.hicall.workers.dev`
- Admin: `https://voting-aifn2.hicall.workers.dev/admin.html`

## Public participation and final results
- Before deadline, `/api/public-status` exposes only names and masked NIMs of students who have not submitted a ballot. Redeem alone does not count as voted.
- The public panel refreshes every 15 seconds.
- After deadline, the same endpoint exposes final totals, percentages, participation, winner, or tie status.
- Public results never expose voter-to-candidate mappings. That audit remains admin-only.


## Revisi deadline
Deadline final diubah menjadi Kamis, 12 November 2026 pukul 22.00 WIB (15.00 UTC). Cache PWA dinaikkan agar browser mengambil versi terbaru.


## Roster terbaru
Roster voting berisi 40 mahasiswa eligible. HELMI RIYADHOH dan RINI YANTI sudah ditambahkan. RUDI HARTANTO (Fast-Track) dikecualikan. Deadline tetap Kamis, 12 November 2026 pukul 22.00 WIB.


## Perbaikan pengiriman suara
Tombol Kirim suara tidak lagi terkunci permanen jika callback Turnstile terlambat. Saat diklik, aplikasi membaca token langsung dari widget, menampilkan instruksi jika verifikasi belum selesai, mencegah klik ganda saat request berjalan, dan mengaktifkan kembali tombol bila request gagal.


## Perbaikan final voting
Turnstile hanya dijalankan pada validasi NIM. Endpoint vote memakai ballot session yang sudah diverifikasi, sehingga tidak ada widget Turnstile kedua yang dapat memblokir tombol Kirim suara. TTL sesi aktif diperpanjang dari 2 menjadi 15 menit dan tetap diperbarui heartbeat setiap 30 detik.


## Perbaikan binding tombol logout
Referensi elemen logout kini selalu diambil eksplisit dengan document.getElementById('logout'), tidak lagi mengandalkan global ID browser yang bertabrakan dengan fungsi logout().
