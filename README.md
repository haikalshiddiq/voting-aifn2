# Voting Ketua Kelas AiFn2 PWA

Target: https://voting-aifn2.hicall.workers.dev
Eligible: 38 mahasiswa. RUDI HARTANTO (25140200001, Fast-Track) dikecualikan sebagai pemilih dan kandidat.
Deadline server: Kamis, 19 November 2026 pukul 22.00 WIB (15.00 UTC).

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
